Para ambiente linux.

Com o docker e docker-compose instaldo, ou caso não tenha siga os passo nos links -> 
[link 1](https://docs.docker.com/engine/install/) 
e 
[link 2](https://docs.docker.com/compose/install/)

Primeiro passo, altere o arquivo env.exemplo para .env;


Para rodar ao banco de dados, no docker-compose.yml para subir um container, no terminal.

    $ docker compose up db-patient -d


É necessario incluir na raiz do projeto um arquivo `.env` com as seguintes informações ou alterar o arquivo .env.exemplo para .env:
    
    DB_URL=postgresql+psycopg://postgres:postgres@127.0.0.1:5432/dbp


Mas caso tenho o postgres instalado localmente é necessario informar informar no .env usuario, senha, host, porta e databasenanme na variavel DB_URL:
    
    - exemplo: DB_URL=postgresql+psycopg://{usuario}:{senha}@{host}:{porta}/{databasenanme}


Caso não inclua o .env, sera criado um banco sqlite -> backend_test.db


Para rodar a aplicação, mas será necessario ter o python instalado, de preferencia a versão 3.12:
    
    1-Craindo o ambiente:
        $ python -m venv .venv

    2-Ativando o ambiente no linux:
        $ source .venv/bin/activate

    3-Instalando os requisitos:
        $ pip install -r requierements.txt

    4-Rodar a migração de dados:
        $ alemcic upgrade head

    5-Rodar a aplicação, (sera http://127.0.0.1:8000/):
        $ uvicorn src.application.server:app --reload
        ou
        $ python main.py

    6-Teste unitario:
        $ pytest

    7-Documentação da api:
        http://127.0.0.1:8000/api/v1/redoc
        http://127.0.0.1:8000/api/v1/docs

Endpoints:
    
    Cadastrar patient:
        - http://127.0.0.1:8000/api/v1/patients
        - Metodo `POST`
        - dados body:
                        {
                          "name": "Jane Smith",
                          "birth_date": "1990-05-15",
                          "address": "123 Flower Street",
                          "phone": "(11) 91234-5678",
                          "email": "jane.smith@example.com",
                          "medical_history": "Patient with a history of hypertension."
                        }
        - Retorna:
            status: 201
            body: {         
                          "id": 1,
                          "name": "Jane Smith",
                          "birth_date": "1990-05-15",
                          "address": "123 Flower Street",
                          "phone": "(11) 91234-5678",
                          "email": "jane.smith@example.com",
                          "medical_history": "Patient with a history of hypertension."
                        }

    Editar patient:
        - http://127.0.0.1:8000/api/v1/patients/{id}
        - {id} é identificador unico de cada patient
        - Metodo `PUT`
        - dados body:
                        {
                          "id": 1,
                          "name": "Jane Smith 10",
                          "birth_date": "1991-05-15",
                          "address": "123 Flower Street",
                          "phone": "(11) 91234-5678",
                          "email": "jane.smith@example.com",
                          "medical_history": "Patient with a history of hypertension."
                        }
        - Retorna:
            status: 200
            body: {
                          "name": "Jane Smith 10",
                          "birth_date": "1991-05-15",
                          "address": "123 Flower Street",
                          "phone": "(11) 91234-5678",
                          "email": "jane.smith@example.com",
                          "medical_history": "Patient with a history of hypertension."
                        }

    Listar patients:
            - http://127.0.0.1:8000/api/v1/patients
            - Metodo `GET`
            - query param:
                - page: integer
                - limit: integer
            - Retorna:
                status: 200
                body: {
                        "data": [
                            {
                                "id": 1,
                                "name": "Jane Smith 10",
                                "age": 34,
                                "phone": "(11) 91234-5678",
                                "email": "jane.smith@example.com",
                                "last_visit_summary": "Visit on 2023-05-17: General check-up, blood pressure 120/80"
                            },
                            {
                                "id": 2,
                                "name": "Jane Smith 5",
                                "age": 34,
                                "phone": "(11) 91234-5678",
                                "email": "jane.smith@example.com",
                                "last_visit_summary": "Visit on 2023-02-15: General check-up, blood pressure 120/80"
                            }
                        ],
                        "page": 1,
                        "count": 12,
                        "limit": 2
                    }

    Cadastrar visit:
            - http://127.0.0.1:8000/api/v1/visits
            - Metodo `POST`
            - dados body:
                            {
                              "patient_id": 1,
                              "visit_date": "2023-06-17",
                              "summary": "General check-up, blood pressure 120/70"
                            }
            - Retorna:
                status: 201
                body: { 
                          "id": 1,
                          "patient_id": 4,
                          "visit_date": "2023-06-17",
                          "summary": "General check-up, blood pressure 120/70"
                        }
