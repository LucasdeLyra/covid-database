import utils.utils as utils

database, cursor = utils.create_cursor()
cursor.execute('CREATE DATABASE refined;')
cursor.execute('USE refined')

#Cria Evolução
utils.create_table(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv',
    'CREATE TABLE Evolucao(ID INTEGER NOT NULL AUTO_INCREMENT, evolucao VARCHAR(16), PRIMARY KEY (ID));',
    ['evolucao'],
    'INSERT INTO refined.evolucao (evolucao) VALUES (%s)',
    'refined',
    True,
    '',
    'evolucao',
    )

#Cria tabela CEP
utils.create_table(r'stg\sup\CEP_dos_casos_confirmados_de_COVID-19_no_município_do_Rio_de_Janeiro.csv',
    'CREATE TABLE CEP(ID INTEGER NOT NULL AUTO_INCREMENT, CEP VARCHAR(16), PRIMARY KEY (ID));',
    ['cep'],
    'INSERT INTO refined.CEP (CEP) VALUES (%s)',
    'refined',
    True,
    '',
    'cep',
    )

#Cria tabela Regiao_Administrativa e salva no diretório local
utils.create_table(r'stg\sup\Limite_de_Bairros.csv',
    'CREATE TABLE Regiao_Administrativa(fk_Regiao_Administrativa_codra INTEGER PRIMARY KEY, regiao_adm VARCHAR(32))',
    ['codra', 'regiao_adm'],
    'INSERT INTO refined.Regiao_Administrativa (regiao_adm, fk_Regiao_Administrativa_codra) VALUES (%s, %s)',
    'refined',
    True,
    r'ref\RegiaoAdministrativa.csv',
    'codra'
)

#Cria tabela Regiao_de_Planejamento e salva no diretório local
utils.create_table(r'stg\sup\Limite_de_Bairros.csv',
    'CREATE TABLE Regiao_de_Planejamento(fk_Regiao_de_Planejamento_cod_rp VARCHAR(3) PRIMARY KEY, rp VARCHAR(32))',
    ['cod_rp', 'rp'],
    'INSERT INTO refined.Regiao_de_Planejamento (rp, fk_Regiao_de_Planejamento_cod_rp) VALUES (%s, %s)',
    'refined',
    True,
    r'ref\RegiaoDePlanejamento.csv',
    'cod_rp'
)

#Não tem a menor necessidade de ter feito isso, poderia ter sido com a util.create_table também que seria até mais fácil
#Cria tabela bairro
cursor.execute('CREATE TABLE bairro AS SELECT fk_Bairro_codbairro, nome, area, fk_Regiao_Administrativa_codra, fk_Regiao_de_Planejamento_cod_rp, COALESCE(bolsa_familia_sim, 0) AS bolsa_familia_sim, COALESCE(bolsa_familia_nao, 0) AS bolsa_familia_nao, COALESCE(faixa_renda_acima_1_5, 0) AS faixa_renda_acima_1_5, COALESCE(faixa_renda_baixa_renda, 0) AS faixa_renda_baixa_renda, COALESCE(faixa_renda_extrema_pobreza, 0) AS faixa_renda_extrema_pobreza, COALESCE(faixa_renda_pobreza, 0) AS faixa_renda_pobreza, COALESCE(extrema_pobreza_cadastrado, 0) AS extrema_pobreza_cadastrado, COALESCE(extrema_pobreza_sem_registro, 0) AS extrema_pobreza_sem_registro \
    FROM staging.stg_bairro AS bairro \
    left JOIN staging.stg_bolsa_familia \
    ON bairro.nome_normalized = staging.stg_bolsa_familia.localidade \
    LEFT JOIN staging.stg_faixa_de_renda_per_capta \
    ON bairro.nome_normalized = staging.stg_faixa_de_renda_per_capta.localidade \
    LEFT JOIN staging.stg_extrema_pobreza \
    ON bairro.nome_normalized = staging.stg_extrema_pobreza.localidade;')
database.commit()

#Cria tabela Unidade_de_Saude
cursor.execute('CREATE TABLE Unidades_de_Saude AS SELECT CNES, equipes, fk_Bairro_codbairro, staging.stg_unidades_de_saude.nome, endereco \
    FROM staging.stg_bairro \
    RIGHT JOIN staging.stg_unidades_de_saude \
    ON staging.stg_bairro.nome_normalized = staging.stg_unidades_de_saude.bairro;')
database.commit()

#Cria tabela Caso_de_COVID
cursor.execute('CREATE TABLE Caso_de_COVID AS SELECT staging.stg_casos_de_covid.ID, dt_notific, dt_inicio_sintomas, dt_evolucao, refined.evolucao.ID AS fk_Evolucao_ID FROM staging.stg_casos_de_covid \
    JOIN refined.evolucao \
    ON refined.evolucao.evolucao = stg_casos_de_covid.evolucao;')
database.commit()

#Cria tabela Reside_Bairro_Caso_de_COVID_CEP
cursor.execute('CREATE TABLE Resida_Bairro_Caso_de_COVID_CEP AS SELECT fk_Bairro_codbairro, refined.cep.ID AS fk_CEP_ID, staging.stg_casos_de_covid.ID AS fk_Caso_de_COVID_ID FROM staging.stg_casos_de_covid \
    LEFT JOIN refined.cep \
    ON refined.cep.cep = staging.stg_casos_de_covid.cep \
    LEFT JOIN staging.stg_bairro \
    ON staging.stg_bairro.nome_normalized = staging.stg_casos_de_covid.bairro;')
database.commit()


