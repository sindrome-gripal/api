# Sindrome Gripal - OpenDataSUS
API para visualização de dados a respeito da síndrome gripal de casos leves a moderados suspeitos de COVID-19. Para mais informações acesse a página do [OpenDataSUS](https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-api-elasticsearch).

-----
## Requisitos

- Python >= 3.6
- virtualenv
- uvicorn

## Complemento 
 - [Flutter APP](https://github.com/sindrome-gripal/app) • Run in Android and Chrome

## Executando Localmente

#### Venv
Crie um ambiente virtual e o ative.
```sh
python3 -m venv venv
source venv/bin/activate
```

Instale os pacotes e rode a aplicação.

```sh
make install
make run-dev
```

#### Docker
```sh
make build-run
```

#### Deploy on Heroku
É preciso ter o CLI do Heroku, estar logado e ter um app criado para fazer o deploy.
```sh
make deploy
```
