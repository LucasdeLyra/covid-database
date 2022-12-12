import pandas as pd
import os
import utils.utils as utils

database, cursor = utils.create_cursor()
#cursor.execute('CREATE DATABASE refined;')
cursor.execute('USE refined')


cursor.execute('CREATE TABLE Resida_Bairro_Caso_de_COVID_CEP AS SELECT codbairro AS fk_Bairro_codbairro, refined.cep.ID AS fk_CEP_ID, staging.stg_casos_de_covid.ID AS fk_Caso_de_COVID_ID FROM staging.stg_casos_de_covid \
    LEFT JOIN refined.cep \
    ON refined.cep.cep = staging.stg_casos_de_covid.cep \
    LEFT JOIN staging.stg_bairro \
    ON staging.stg_bairro.nome_normalized = staging.stg_casos_de_covid.bairro;')
database.commit()
