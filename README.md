# Property Project

## Tecnologias usadas:
  - Python3.8
  - Unittest
  - Virtualenv
  - MYSQL
  - AWS SAM
  - AWS Lambda
  - AWS Api gateway

## Como se realizo
### Infraestructura y despliegle
El proyecto se realizo usando algunos servicios de AWS, no se utiliza ningun framework mas que SAM(serverless application model), este se usa con el fin de desplegar el proyecto en un infraestructura sin servidor, este tipo de infraestuctura nos proveen ventajas como mejor escalabilidad, costo-eficiencia, reducciion tiempo de desarrollo y configuracion, entre otros.

Se hace uso del servicio lambda de aws, ideal para ejecutar microservicios o tareas que consuman poco tiempo y recursos. Para disponer de un endpoint se uso el servico api gateway de aws, este se encarga de recibir el request y ejecutar por medio de un evento el lambda, pasado los datos del request.

### Estructura del proyecto
    .
    ├── app.py                          # contiene los handler del los lambda
    ├── README.md                       
    ├── resources                       # contiene algunos recursos del proyecto
    ├── services                        # contiene la logica de los microservicios
    │   ├── habi_db.py            # se encarga de la conexion a la base de datos
    │   └── property_service.py   # contiene la logica de micro sercivisio de property
    └── tests                           # 
        └── test.py                     # contiene las pruebas

### Pruebas unitarias


## Configuracion de ambiente local


## Ejecutar pruebas


## Mejoras sugeridas