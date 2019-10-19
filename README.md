# API Gateway

API Gateway para os microserviços do QR-Comer

## Instalação e Configuração

### Pré-requisitos

 - É necessário ter o DOcker e o docker-compose instalados
 - Caso ainda não exista, é preciso criar uma network no docker usando o comando ```docker network create qr-comer``` 

 ### Como usar

  - Clone o repositório
  - Rode ```docker-compose up```
  - Este container está rodando na porta 5002 do __localhost__

    #### Como criar uma rota

    Para se comunicar com outros serviços devem ser utilizadas as variáveis de ambiente, são elas

    - ORDERS_PATH
    - PAYMENT_PATH
    - RESTAURANT_PATH
    - USERS_PATH

    Uma requisição deve ser feita da seguinte forma:

    ```
    import os

    response = requests.get("%s/nome_do_endpoit" % os.getenv('ORDERS_PATH'))
    ```
    

