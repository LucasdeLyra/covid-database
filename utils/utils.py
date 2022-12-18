import mysql.connector
import pandas as pd
import numpy as np
def create_cursor():
    """
    Cria um cursor da biblioteca mysql
    Return
    --------
    database :
        a database em que o cursor foi criado
    cursor:
        um cursor mysql
    """
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root', 
    )
    cursor = database.cursor()
    return database, cursor

def create_table(origin: str, create: str, nodrop: list, query: str, database:str, drop: bool=False, dest='', primary: str='', create_id: bool=False):
    """
    Cria uma tabela no mysql a partir de uma tabela de origem

    Params
    --------
        origin : str
            dado de origem
        create : str
            comando sql a ser executado para criar a tabela
        nodrop : list
            lista de colunas da tabela de origem a serem mantidas na tabela de destino
        query : str
            comando sql a ser executado para adicionar as linhas requeridas à tabela de destino
        database : str
            database na qual a tabela está
        drop : bool
            indica se deve-se ignorar alguma coluna
        dest : str
            endereco de destino da tabela nova
        primary : str
            indica a primary key da tabela nova
        create_id : bool
            indica se deve-se criar uma coluna ID
    """
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        db=database
    )
    prim = []
    cursor = mydb.cursor()
    cursor.execute(create)
    table = pd.read_csv(origin)
    print(table.columns)
    if create_id:
        table = table.rename(columns={'Unnamed: 0': 'ID'})
    if drop: 
        table = table.drop(list(set(table.columns) - set(nodrop)), axis=1)
        if dest !='':
            table.to_csv(dest, index=False)
    print(table.columns)

    for i, row in table.iterrows():
        if not primary:
            cursor.execute(query, tuple(row))

        else:
            if row[primary] not in prim:
                cursor.execute(query, tuple(row))
                prim.append(row[primary])

        mydb.commit()


def normalize_casos():
    """
    Normaliza a coluna 'evolucao' do csv indicado como input
    """
    input = pd.read_csv(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv', sep=',')
    aux = pd.DataFrame(input['evolucao'])
    aux = aux.replace('', 'Desconhecido').replace(np.nan, 'Desconhecido')
    input['evolucao'] = aux['evolucao'].str.capitalize()
    input.to_csv(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv', index=False)

def normalize_datas():
    """
    Normaliza as datas ('dt_notific', 'dt_evolucao', 'dt_inicio_sintomas') do csv indicado como input
    """
    input = pd.read_csv(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv', sep=',')
    #aux = pd.DataFrame(input[['dt_notific','dt_inicio_sintomas','dt_evolucao']])
    input['dt_notific'] = pd.to_datetime(input['dt_notific'])
    input['dt_inicio_sintomas'] = pd.to_datetime(input['dt_inicio_sintomas'])
    input['dt_evolucao'] = pd.to_datetime(input['dt_evolucao'])
    input.to_csv(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv', index=False)

def normalize_bairro_cep():
    """
    Normaliza os nomes dos bairros do csv indicado como input, afim de fazer a junção com as tabelas do CECAD depois
    """
    input = pd.read_csv(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv', sep=',')
    output = input
    output['nome_normalized'] = input['bairro_resid__estadia'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.upper().str.strip()
    output = output.replace('FREGUESIA (ILHA)', 'FREGUESIA').replace('FREGUESIA (JACAREPAGUA)', 'FREGUESIA JACAREPAGUA')
    output['bairro_resid__estadia'] = input['bairro_resid__estadia']
    output.to_csv(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv', index=False)

def normalize_bairro():
    """
    Cria uma coluna 'nome_normalized', que contém de fato os nomes normalizados dos bairros, do csv indicado como input, 
    afim de criar as tabelas de região administrativa e de planejamento.
    """
    input = pd.read_csv(r'raw\Limite_de_Bairros.csv')
    output = input
    output['nome_normalized'] = input['nome'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.upper().str.strip()
    output = output.replace('FREGUESIA (ILHA)', 'FREGUESIA').replace('FREGUESIA (JACAREPAGUA)', 'FREGUESIA JACAREPAGUA')
    output['nome'] = input['nome']
    output.to_csv(r'stg\sup\Limite_de_Bairros.csv')

def normalize_unidade():
    """
    Normaliza a coluna 'BAIRRO' do csv indicado como input
    """
    input = pd.read_csv(r'raw\Unidades_de_Saúde_Municipais.csv')
    input['BAIRRO'] = input['BAIRRO'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.upper().str.strip()
    input = input.replace('JACAREPAGUA-TAQUARA', 'TAQUARA').replace('PORTUGUESA ILHA DO GOVERNADOR', 'PORTUGUESA').replace('CIDADES DE DEUS', 'CIDADE DE DEUS').replace('JARDIM BANGU', 'BANGU')
    input.loc[303, ['BAIRRO']] = 'CACUIA'
    input.to_csv(r'stg\sup\Unidades_de_Saúde_Municipais.csv')

def clean_xls(raw, stg, header):
    """
    Transforma a html table dos dados do CECAD em um csv
    """
    origin = pd.read_html(raw)
    df = origin[0]
    df.columns = df.columns.droplevel(0)
    df.columns = list(header.keys())
    df = df.astype(header)
    df.to_csv(stg, index=False)

