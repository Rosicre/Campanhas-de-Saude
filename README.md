# ⚕️ Saúde + Solidária

Este projeto foi desenvolvido como parte da disciplina Projeto Integrador IV: Desenvolvimento de sistemas orientado a dispositivos móveis e baseados na web.

<div align="center">
  
[![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?logo=html5&logoColor=white)](#)
[![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=fff)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Flask](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff)](#)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)

</div>

## Dependências

- [Docker](https://docs.docker.com/guides/getting-started/)
- [Docker Compose](https://docs.docker.com/compose/)

## Configurando o ambiente

- Clone o repositório
- Crie um arquivo .env na raíz do repositório com as seguintes variáveis de ambiente configuradas (modifique usuários, senhas e chaves de acordo):

  ```env
  FLASK_APP=run.py
  FLASK_CONFIG=production
  SECRET_KEY=<flask-secret-key>
  POSTGRES_USER=flask_app
  PGUSER=${POSTGRES_USER}
  POSTGRES_PASSWORD=<super-secret-password>
  POSTGRES_HOST=db
  POSTGRES_PORT=5432
  POSTGRES_DB=saude_solidaria
  DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
  PGADMIN_DEFAULT_EMAIL=<admin@pgadmin.com>
  PGADMIN_DEFAULT_PASSWORD=<password>
  TZ=America/Sao_Paulo
  ```

## Executando a aplicação

Dentro de `/deploy` execute o Docker Compose com

```bash
docker compose up -d
```

Acesse o web GUI a partir da porta mapeada no host em `http://localhost:8888/`.

## Banco de dados

![MER](./docs/assets/MER.png)

## Colaboradores

<div align="center">
    <table style="width: 100%; border-collapse: collapse; text-align: center;">
    <tr>
        <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;">
            <img src="https://avatars.githubusercontent.com/u/74667067?v=4" alt="jvitor-alol" style="display: block; margin: 0 auto; width: 100px; height: 100px;">
            <a href="https://github.com/jvitor-alol" target="_blank"><p>jvitor-alol</p></a>
        </td>
        <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;">
            <img src="https://avatars.githubusercontent.com/u/85653011?v=4" alt="Lynn-Noob" style="display: block; margin: 0 auto; width: 100px; height: 100px;">
            <a href="https://github.com/Lynn-Noob" target="_blank"><p>Lynn-Noob</p></a>
        </td>
        <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;">
            <img src="https://avatars.githubusercontent.com/u/95151247?v=4" alt="Guilherme-Soares05" style="display: block; margin: 0 auto; width: 100px; height: 100px;">
            <a href="https://github.com/Guilherme-Soares05" target="_blank"><p>Guilherme-Soares05</p></a>
        </td>
        <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;">
            <img src="https://avatars.githubusercontent.com/u/94906196?v=4" alt="Rosicre" style="display: block; margin: 0 auto; width: 100px; height: 100px;">
            <a href="https://github.com/Rosicre" target="_blank"><p>Rosicre</p></a>
        </td>
    </tr>
    <tr>
        <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;">
            <img src="https://avatars.githubusercontent.com/u/142458518?v=4" alt="mirelaads" style="display: block; margin: 0 auto; width: 100px; height: 100px;">
            <a href="https://github.com/mirelaads" target="_blank"><p>mirelaads</p></a>
        </td>
        <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;">
            <img src="https://avatars.githubusercontent.com/u/102329062?v=4" alt="medinaandre" style="display: block; margin: 0 auto; width: 100px; height: 100px;">
            <a href="https://github.com/medinaandre" target="_blank"><p>medinaandre</p></a>
        </td>
        <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;">
            <img src="https://avatars.githubusercontent.com/u/86894587?v=4" alt="dkexs" style="display: block; margin: 0 auto; width: 100px; height: 100px;">
            <a href="https://github.com/dkexs" target="_blank"><p>dkexs</p></a>
        </td>
        <td style="padding: 20px; border: 1px solid #ddd; vertical-align: middle;">
            <img src="https://avatars.githubusercontent.com/u/60987344?v=4" alt="PedroBrito22" style="display: block; margin: 0 auto; width: 100px; height: 100px;">
            <a href="https://github.com/PedroBrito22" target="_blank"><p>PedroBrito22</p></a>
        </td>
    </tr>
  </table>
</div>
