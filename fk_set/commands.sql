ALTER TABLE Caso_de_COVID ADD CONSTRAINT FK_Caso_de_COVID_2 FOREIGN KEY (fk_Evolucao_ID) REFERENCES Evolucao (ID) ON DELETE CASCADE;
ALTER TABLE Bairro ADD CONSTRAINT FK_Bairro_2 FOREIGN KEY (fk_Regiao_Administrativa_codra) REFERENCES Regiao_Administrativa (fk_Regiao_Administrativa_codra) ON DELETE RESTRICT;
ALTER TABLE Bairro ADD CONSTRAINT FK_Bairro_3 FOREIGN KEY (fk_Regiao_de_Planejamento_cod_rp) REFERENCES Regiao_de_Planejamento (fk_Regiao_de_Planejamento_cod_rp) ON DELETE RESTRICT;
ALTER TABLE bairro ADD CONSTRAINT pk_Bairro PRIMARY KEY (fk_Bairro_codbairro);
ALTER TABLE Unidades_de_Saude ADD CONSTRAINT FK_Unidades_de_Saude_2 FOREIGN KEY (fk_Bairro_codbairro) REFERENCES bairro (fk_Bairro_codbairro) ON DELETE CASCADE;
ALTER TABLE Resida_Bairro_Caso_de_COVID_CEP ADD CONSTRAINT FK_Resida_Bairro_Caso_de_COVID_CEP_1 FOREIGN KEY (fk_Bairro_codbairro) REFERENCES Bairro (fk_Bairro_codbairro) ON DELETE NO ACTION;
ALTER TABLE caso_de_covid ADD CONSTRAINT pk_Caso_de_Covid PRIMARY KEY (ID);
ALTER TABLE Resida_Bairro_Caso_de_COVID_CEP ADD CONSTRAINT FK_Resida_Bairro_Caso_de_COVID_CEP_2 FOREIGN KEY (fk_Caso_de_COVID_ID) REFERENCES Caso_de_COVID (ID) ON DELETE NO ACTION;
ALTER TABLE Resida_Bairro_Caso_de_COVID_CEP ADD CONSTRAINT FK_Resida_Bairro_Caso_de_COVID_CEP_3 FOREIGN KEY (fk_CEP_ID) REFERENCES CEP (ID) ON DELETE NO ACTION;