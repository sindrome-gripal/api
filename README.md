# Sindrome Gripal - OpenDataSUS
...

-----
## Requisitos

- Python >= 3.6
- virtualenv
- uvicorn


## Executando Localmente

#### Venv

```sh
python3 -m venv venv
source venv/bin/activate
make install
make run-dev
```

#### Docker
```sh
make build-run
```

#### Deploy Heroku
```sh
make deploy
```
