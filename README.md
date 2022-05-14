# Instrucciones
En la terminal correr '''docker-compose up --build''' en el root del directorio. 

## Comandos de Postman GET
http://0.0.0.0:5001/  
http://0.0.0.0:5001/get_info  

## Comandos de Postman POST
http://0.0.0.0:5001/validate_data  
http://0.0.0.0:5001/make_prediction  

### Body (JSON): 
   
{  
    "active": true,  
    "balance": 1564.48,  
    "email": "leanne.perry@gmail.com",  
    "age": 21,  
    "name": "Leanne Perry",
    "gender": "female"  
}

## GITHUB repo
https://github.com/jimmymef/docker_dummy_model