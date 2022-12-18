import os
import pandas as pd
import utils

database, cursor = utils.create_cursor()
#Para executar o comando abaixo é necessário que altere o campo secure_file_priv my.ini de seu MySQL
#ache o local onde está sua secure_file_priv através de @@GLOBAL.secure_file_priv

#Salva a tabela bairro no diretório local
cursor.execute(fr"SELECT * FROM refined.bairro INTO OUTFILE '{repr(os.getcwd())[1:-1]}\\stg\\bairro.csv' FIELDS ENCLOSED BY '' TERMINATED BY ',' ESCAPED BY '' LINES TERMINATED BY '\r\n'")
finaldados = pd.read_csv(r'.\stg\bairro.csv', names = ['fk_Bairro_codbairro','nome','area','fk_Regiao_Administrativa_codra','cod_rp','bolsa_familia_sim','bolsa_familia_nao','faixa_renda_acima_1_5','faixa_renda_baixa_renda','faixa_renda_extrema_pobreza','faixa_renda_pobreza','extrema_pobreza_cadastrado','extrema_pobreza_sem_registro'])
finaldados.to_csv(r'.\ref\bairro.csv', header=True, index=False)

#Salva tabela Unidade_de_Saude no diretório local
cursor.execute(fr"SELECT * FROM refined.Unidades_de_Saude INTO OUTFILE '{repr(os.getcwd())[1:-1]}\\stg\\Unidades_de_Saude.csv' FIELDS ENCLOSED BY '' TERMINATED BY ',' ESCAPED BY '' LINES TERMINATED BY '\r\n'")
finaldados = pd.read_csv(r'.\stg\Unidades_de_Saude.csv', names = ['CNES','NOME','EQUIPES','ENDERECO','BAIRRO'])
finaldados.to_csv(r'.\ref\Unidades_de_Saude.csv', header=True, index=False)

#Salva tabela CEP no diretório local
cursor.execute(fr"SELECT * FROM refined.CEP INTO OUTFILE '{repr(os.getcwd())[1:-1]}\\stg\\CEP.csv' FIELDS ENCLOSED BY '' TERMINATED BY ',' ESCAPED BY '' LINES TERMINATED BY '\r\n'")
finaldados = pd.read_csv(r'.\stg\CEP.csv', names = ['ID','CEP'])
finaldados.to_csv(r'.\ref\CEP.csv', header=True, index=False)

#Salva a tabela Caso_de_COVID no repositório local
cursor.execute(fr"SELECT * FROM refined.Caso_de_COVID INTO OUTFILE '{repr(os.getcwd())[1:-1]}\\stg\\Caso_de_COVID.csv' FIELDS ENCLOSED BY '' TERMINATED BY ',' ESCAPED BY '' LINES TERMINATED BY '\r\n'")
finaldados = pd.read_csv(r'.\stg\Caso_de_COVID.csv', names = ['ID','dt_notfic','dt_inicio_sintomas','dt_evolucao','fk_Evolucao_ID'])
finaldados.to_csv(r'.\ref\Caso_de_COVID.csv', header=True, index=False)

#Salva tabela evolucao no diretório local
cursor.execute(fr"SELECT * FROM refined.evolucao INTO OUTFILE '{repr(os.getcwd())[1:-1]}\\stg\\evolucao.csv' FIELDS ENCLOSED BY '' TERMINATED BY ',' ESCAPED BY '' LINES TERMINATED BY '\r\n'")
finaldados = pd.read_csv(r'.\stg\evolucao.csv', names = ['ID','CEP'])
finaldados.to_csv(r'.\ref\evolucao.csv', header=True, index=False)

#Salva tabela Reside_Bairro_Caso_de_COVID_CEP no diretório local
cursor.execute(fr"SELECT * FROM refined.Resida_Bairro_Caso_de_COVID_CEP INTO OUTFILE '{repr(os.getcwd())[1:-1]}\\stg\\Resida_Bairro_Caso_de_COVID_CEP.csv' FIELDS ENCLOSED BY '' TERMINATED BY ',' ESCAPED BY '' LINES TERMINATED BY '\r\n'")
finaldados = pd.read_csv(r'.\stg\Resida_Bairro_Caso_de_COVID_CEP.csv', names = ['fk_Bairro_codbairro','fk_CEP_ID','fk_Caso_de_COVID_ID'])
finaldados.to_csv(r'.\ref\Resida_Bairro_Caso_de_COVID_CEP.csv', header=True, index=False)