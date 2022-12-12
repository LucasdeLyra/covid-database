import utils.utils as utils
import pandas as pd
database, cursor = utils.create_cursor()
cursor.execute('CREATE DATABASE staging;')
cursor.execute('USE staging;')

pd.read_csv(r'raw\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv', sep=';').to_csv(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv', sep=',', index=True)
utils.normalize_casos()
utils.normalize_datas()
utils.normalize_bairro_cep()
utils.create_table(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv',
    'CREATE TABLE stg_Casos_de_COVID(ID INTEGER, dt_notific DATETIME, dt_inicio_sintomas DATETIME, dt_evolucao DATETIME, evolucao VARCHAR(16), cep VARCHAR(8), bairro VARCHAR(32))',
    [ 'dt_notific', 'dt_inicio_sintomas', 'evolucao', 'dt_evolucao', 'cep', 'ObjectId', 'nome_normalized'],
    'INSERT INTO staging.stg_Casos_de_COVID (dt_notific, dt_inicio_sintomas, evolucao, dt_evolucao, cep,  ID,  bairro) VALUES (DATE(%s), DATE(%s), %s, DATE(%s), %s, %s, %s)',
    'staging',
    True,
    r'stg\Casos.csv')


utils.clean_xls(r'raw\ExtremaPobreza.xls', r'stg\ExtremaPobreza.csv', {'Localidade': 'object', 'Quantidade Famílias Sem Registro Civil': 'int64', 'Quantidade Famílias Cadastrado': 'int64', 'Quantidade Famílias Total': 'int64'})
utils.clean_xls(r'raw\FaixaDeRendaPerCaptaAtualizado.xls', r'stg\FaixaDeRendaPerCaptaAtualizado.csv', {'Localidade': 'object', 'Quantidade Famílias Extrema Pobreza': 'int64', 'Quantidade Famílias Pobreza': 'int64', 'Quantidade Famílias Baixa Renda': 'int64', 'Quantidade Famílias Acima de 1/2 S.M': 'int64', 'Quantidade Famílias Total': 'int64'})
utils.clean_xls(r'raw\BolsaFamilia.xls', r'stg\BolsaFamilia.csv', {'Localidade': 'object', 'Quantidade Famílias Sim': 'int64', 'Quantidade Famílias Não': 'int64', 'Quantidade Famílias Total': 'int64'})
utils.normalize_bairro()
utils.create_table(r'stg\sup\Limite_de_Bairros.csv', 
    'CREATE TABLE stg_bairro(codbairro INTEGER, nome VARCHAR(32), nome_normalized VARCHAR(32), area FLOAT, codra INTEGER, cod_rp VARCHAR(4), PRIMARY KEY (codbairro))', 
    ['codbairro', 'nome', 'nome_normalized', 'área', 'codra', 'cod_rp'],
    'INSERT INTO staging.stg_bairro (area, nome, codbairro, codra, cod_rp, nome_normalized) VALUES (%s, %s, %s, %s, %s, %s)',
    'staging',
    True,
    r'stg\sup\Bairro.csv')

utils.create_table(r'stg\FaixaDeRendaPerCaptaAtualizado.csv', 
    'CREATE TABLE stg_faixa_de_renda_per_capta(localidade VARCHAR(64), faixa_renda_extrema_pobreza INTEGER, faixa_renda_pobreza INTEGER, faixa_renda_baixa_renda INTEGER, faixa_renda_acima_1_5 INTEGER, faixa_renda_extrema_total INTEGER)', 
    [],
    'INSERT INTO staging.stg_faixa_de_renda_per_capta VALUES (%s, %s, %s, %s, %s, %s)',
    'staging')

utils.create_table(r'stg\ExtremaPobreza.csv',
    'CREATE TABLE stg_extrema_pobreza(localidade VARCHAR(64), extrema_pobreza_sem_registro INTEGER, extrema_pobreza_cadastrado INTEGER, extrema_pobreza_total INTEGER)',
    [],
    'INSERT INTO staging.stg_extrema_pobreza VALUES (%s, %s, %s, %s)',
    'staging')

utils.create_table(r'stg\BolsaFamilia.csv',
    'CREATE TABLE stg_bolsa_familia(localidade VARCHAR(64), bolsa_familia_sim INTEGER, bolsa_familia_nao INTEGER, bolsa_familia_total INTEGER)',
    [],
    'INSERT INTO staging.stg_bolsa_familia VALUES (%s, %s, %s, %s)',
    'staging')

utils.normalize_unidade()
utils.create_table(r'stg\sup\Unidades_de_Saúde_Municipais.csv',
    'CREATE TABLE stg_Unidades_de_Saude(CNES INTEGER PRIMARY KEY, nome VARCHAR(64), equipes VARCHAR(32), bairro VARCHAR(32), endereco VARCHAR(64))',
    ['CNES', 'NOME', 'EQUIPES', 'BAIRRO', 'ENDERECO'],
    'INSERT INTO staging.stg_Unidades_de_Saude (CNES, nome, equipes, endereco, bairro) VALUES (%s, %s, %s, %s, %s)',
    'staging',
    True,
    r'stg\sup\Unidades_de_Saude.csv',
    'CNES'
)

