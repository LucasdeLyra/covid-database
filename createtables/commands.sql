CREATE TABLE Bairro (
    codbairro INTEGER PRIMARY KEY,
    nome VARCHAR(32),
    area FLOAT,
    faixa_renda_extrema_pobreza INTEGER,
    faixa_renda_pobreza INTEGER,
    faixa_renda_baixa_renda INTEGER,
    faixa_renda_acima_1_5 INTEGER,
    bolsa_familia_sim INTEGER,
    bolsa_familia_nao INTEGER,
    extrema_pobreza_cadastrado INTEGER,
    extrema_pobreza_sem_registro  INTEGER,
    fk_região_administrativa_codra INTEGER,
    fk_região_de_planejamento_cod_rp INTEGER
);
 
ALTER TABLE Bairro ADD CONSTRAINT FK_Bairro_3
    FOREIGN KEY (fk_Região_de_Planejamento_cod_rp)
    REFERENCES Região_de_Planejamento (cod_rp)
    ON DELETE RESTRICT;
 
ALTER TABLE Unidades_de_Saude ADD CONSTRAINT FK_Unidades_de_Saude_2
    FOREIGN KEY (fk_Bairro_codbairro)
    REFERENCES Bairro (codbairro)
    ON DELETE CASCADE;
 
ALTER TABLE Resida_Bairro_Caso_de_COVID_CEP ADD CONSTRAINT FK_Resida_Bairro_Caso_de_COVID_CEP_1
    FOREIGN KEY (fk_Bairro_codbairro)
    REFERENCES Bairro (codbairro)
    ON DELETE NO ACTION;
 
ALTER TABLE Resida_Bairro_Caso_de_COVID_CEP ADD CONSTRAINT FK_Resida_Bairro_Caso_de_COVID_CEP_2
    FOREIGN KEY (fk_Caso_de_COVID_ID)
    REFERENCES Caso_de_COVID (ID)
    ON DELETE NO ACTION;
 
ALTER TABLE Resida_Bairro_Caso_de_COVID_CEP ADD CONSTRAINT FK_Resida_Bairro_Caso_de_COVID_CEP_3
    FOREIGN KEY (fk_CEP_ID)
    REFERENCES CEP (ID)
    ON DELETE NO ACTION;