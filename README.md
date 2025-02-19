<div id="doc-header" align="center">
<h1>
⚕️ Campanhas de Saúde ⚕️
</h1>

<p>
    <img alt="Status Em Desenvolvimento" src="https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-orange">
</p>

<p>
    <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/jvitor-alol/Saude-Solidaria?color=%2304D361">
    <img alt="Repository size" src="https://img.shields.io/github/repo-size/jvitor-alol/Saude-Solidaria"> 
    <a href="https://github.com/jvitor-alol/Saude-Solidaria/commits/main/">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/jvitor-alol/Saude-Solidaria">
    </a>
</p>
</div>

## 💻 Sobre o projeto

Projeto desenvolvido como parte da disciplina Projeto Integrador V: Análise de Soluções Integradas para Organizações.

<div id="tech-stack" align="center">
  <img src="src/assets/images/html5_logo.svg" alt="HTML" style="width: 40px; height: 30px;">
  <img src="src/assets/images/css3_logo.svg" alt="CSS" style="width: 40px; height: 30px;">
  <img src="src/assets/images/js_logo.svg" alt="JavaScript" style="width: 40px; height: 30px;">
  <img src="src/assets/images/python_logo.svg" alt="Python" style="width: 40px; height: 30px;">
  <img src="src/assets/images/flask_logo.svg" alt="Flask" style="width: 40px; height: 30px;">
  <img src="src/assets/images/postgres_logo.svg" alt="Postgres" style="width: 40px; height: 30px;">
  <img src="src/assets/images/docker_logo.svg" alt="Docker" style="width: 40px; height: 30px;">
</div>

## 🔘 Objetivo do projeto

Este projeto tem como objetivo promover campanhas de conscientização sobre temas de saúde pública que afetam diretamente a qualidade de vida da população. Focamos em divulgar informações relevantes e acessíveis sobre os seguintes tópicos:

AIDS: Orientação sobre prevenção, diagnóstico e convivência com o HIV/AIDS.  
Campanha do Sono: Destacar a importância do sono para a saúde física e mental, incentivando hábitos saudáveis.  
Câncer de Pele: Conscientizar sobre os riscos da exposição ao sol e a necessidade de proteção adequada.  
Dengue: Informar sobre a prevenção, combate ao mosquito Aedes aegypti e o impacto da doença.  
Gripe e COVID-19: Esclarecer sobre a importância da vacinação, prevenção e cuidados com essas infecções respiratórias.  
Saúde Mental: Promover a importância do bem-estar emocional e como buscar ajuda em momentos de necessidade.

## 🎨 Layout

O layout da aplicação está disponível no Figma:

[![Made by Cubos Academy](https://img.shields.io/badge/Acessar%20Layout%20-Figma-%2304D361)](https://www.figma.com/files/project/77994470/%F0%9F%93%84-Templates-para-Projetos%2C-Eventos-e-Cursos?fuid=1110596132085818429)

## 🎲 Banco de Dados

O SGBD escolhido foi o PostgreSQL, ideal para aplicações que requerem alta conformidade com padrões SQL, extensibilidade, suporte a dados complexos e alta confiabilidade.

Abaixo se encontra um diagrama que descreve todas as entidades e relacionamentos definidas nos `models` da aplicação.

![MER](./docs/assets/MER.png)

## ⚙️ Dependências

- [Docker](https://docs.docker.com/guides/getting-started/)
- [Docker Compose](https://docs.docker.com/compose/)

## 🔨 Configurando o ambiente

- Clone o repositório

- Crie um arquivo .env na raíz com as seguintes variáveis de ambiente configuradas (modifique usuários, senhas e chaves de acordo):

  ```env
  FLASK_APP=run.py
  FLASK_CONFIG=production
  SECRET_KEY=< flask-secret-key >
  POSTGRES_USER=flask_app
  PGUSER=${POSTGRES_USER}
  POSTGRES_PASSWORD=< super-secret-password >
  POSTGRES_HOST=db
  POSTGRES_PORT=5432
  POSTGRES_DB=saude_solidaria
  DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
  PGADMIN_DEFAULT_EMAIL=< admin@pgadmin.com >
  PGADMIN_DEFAULT_PASSWORD=< password >
  TZ=America/Sao_Paulo
  ```

## 🛣️ Executando a aplicação

- Dentro de `/deploy` execute o Docker Compose com

```bash
docker compose up -d
```

Acesse a interface web da aplicação através da porta mapeada no host em http://localhost:8888/.

👥 Colaboradores

<div align="center"> <table style="width: 100%; border-collapse: collapse; text-align: center;"> <tr> <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;"> <img src="https://avatars.githubusercontent.com/u/95151247?v=4" alt="Guilherme-Soares05" style="display: block; margin: 0 auto; width: 100px; height: 100px;"> <a href="https://github.com/Guilherme-Soares05" target="_blank"><p>Guilherme-Soares05</p></a> </td> <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;"> <img src="https://avatars.githubusercontent.com/u/94906196?v=4" alt="Rosicre" style="display: block; margin: 0 auto; width: 100px; height: 100px;"> <a href="https://github.com/Rosicre" target="_blank"><p>Rosicre</p></a> </td> <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;"> <img src="https://avatars.githubusercontent.com/u/142458518?v=4" alt="mirelaads" style="display: block; margin: 0 auto; width: 100px; height: 100px;"> <a href="https://github.com/mirelaads" target="_blank"><p>mirelaads</p></a> </td> <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;"> <img src="https://avatars.githubusercontent.com/u/86894587?v=4" alt="dkexs" style="display: block; margin: 0 auto; width: 100px; height: 100px;"> <a href="https://github.com/dkexs" target="_blank"><p>dkexs</p></a> </td> </tr> <tr> <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;"> <img src="https://avatars.githubusercontent.com/u/60987344?v=4" alt="PedroBrito22" style="display: block; margin: 0 auto; width: 100px; height: 100px;"> <a href="https://github.com/PedroBrito22" target="_blank"><p>PedroBrito22</p></a> </td> <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;"> <img src="https://avatars.githubusercontent.com/u/115372931?v=4" alt="Rafaelaacg" style="display: block; margin: 0 auto; width: 100px; height: 100px;"> <a href="https://github.com/Rafaelaacg" target="_blank"><p>Rafaelaacg</p></a> </td> <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;"> <img src="https://avatars.githubusercontent.com/u/78533414?v=4" alt="Yoommi" style="display: block; margin: 0 auto; width: 100px; height: 100px;"> <a href="https://github.com/Yoommi" target="_blank"><p>Yoommi</p></a> </td> <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;"> <img src="https://avatars.githubusercontent.com/u/69800107?v=4" alt="timlagolg" style="display: block; margin: 0 auto; width: 100px; height: 100px;"> <a href="https://github.com/timlagolg" target="_blank"><p>timlagolg</p></a> </td> </tr> </table> </div>
