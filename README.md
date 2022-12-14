<div id="topo"></div>

📜 Índice
===

* [Sobre o projeto](#about)
* [Pré-requisitos](#install)
* [Configuração](#setup)
* [Execução](#exe)

## 💻 Sobre o projeto <a name="about"></a>

**Trabalho final de Banco de dados** trata-se de um projeto que visa estruturar em um banco de dados SQL e exibir de forma interativa os seguintes dados referentes à cidade do Rio de Janeiro:

1. [CECAD](https://cecad.cidadania.gov.br/sobre.php)
2. [Casos de covid](https://www.data.rio/datasets/PCRJ::cep-dos-casos-confirmados-de-covid-19-no-munic%C3%ADpio-do-rio-de-janeiro-1/about)
3. [Unidades de saúde](https://www.data.rio/datasets/PCRJ::unidades-de-sa%C3%BAde-municipais-1/about)

## 🔨 Pré-requisitos <a name="install"></a>

Para executar o projeto você precisará ter instaladas as seguintes ferramentas:

### Ferramentas
- [Python3](https://www.python.org/downloads/)
- [MySQL](https://www.mysql.com/)

<p align="right"><a href="#top">Voltar ao topo</a></p>

## 🔧 Configuração <a name="setup"></a>
### Depois de instalar as ferramentas anteriores

1. No terminal, executar o seguinte comando:

   ```.env
   git clone https://github.com/LucasdeLyra/covid-database.git
   ```
2. No diretório raiz do projeto, utilizar o comando a seguir:
   - Instalação dos pacotes

      ```bash
      pip install -r requirements.txt
      ```

<p align="right"><a href="#top">Voltar ao topo</a></p>

## 🚀 Execução <a name="exe"></a>
- No diretório raiz do projeto, utilizar o comando a seguir:

   ```bash
   python main.py
   ```

<p align="right"><a href="#top">Voltar ao topo</a></p>
