# PROYECTO: API DE TAREAS

## DESCRIPCIÓN

__API DE PAGOS__ en la versión actual, permite el registro de usuarios y agregar pagos de diferentes servicios de streaming. Unicamente se pueden realizar dichas funcionalidades cuando un usuario esta logueado.

### Credenciales de prueba

Si desea ver la funcionalidades del projecto como administrador puede utilizar las credenciales mencionadas líneas abajo. Se le pide a los desarrolladores hacer el uso correcto en base a las indicaciones aqui mencionadas para verificar las funcionalidades sin cambiar los datos ya registrados.

```sh 
email: jhonny.jql1210@gmail.com 
Password: jhonny_jhonny123
```

Si desea visualizar el proyecto desde una aplicación frontend puede visitar la siguiente dirección:

- __url:__  `"https://pagos-fronted.netlify.app/"`


## INFORMACIÓN DE USO

__API DE PAGOS__ es un producto gratuito y está abierto para su libre uso. Se le pide a los desarrolladores hacer el uso correcto en base a las indicaciones aqui mencionadas.

Siendo necesario estar registrado y logueado para poder visualizar las funcionalidades del proyecto, aqui se mencionan los endpoints para dichas acciones.

## REGISTRO DE USUARIO

- __Base url:__  `"https://portfolio-v2-production-c48c.up.railway.app/users/signup/"`


## LOGIN DE USUARIO

- __Base url:__  `"https://portfolio-v2-production-c48c.up.railway.app/users/login/"`



## DOCUMENTACIÓN DEL PROYECTO

Para visualizar la documentación dirijase a la siguiente url:

- __url:__  `"https://pagos-api-production.up.railway.app/swagger/"`


## CLONACIÓN DE PROYECTO

Para interatuar con el presente proyecto se debe tener en cuenta la versión de python instalada Python 3.9.7. Así tambien, deberá seguir las siguientes indicaciones:

- Clonar el repositorio:
```sh
$ git clone 
```

- Instalar un ambiente virtual
```sh
$ python -m venv venv
```

- Activar el ambiente virtual
```sh
$ source venv/Scripts/activate    --> Windows
$ source venv/bin/activate        --> Linux
```

- Instalar requerimientos:
```sh
$ pip install -r requirements.txt
```

- Ejecutar el proyecto:
```sh
$ cd projectName
```
Debe verificar que se encuentre en la carpeta que contiene el archivo manage.py. Luego debe ingresar el siguiente comando en la terminal
```sh
$ py manage.py runserver
```


### SOBRE EL PROYECTO:

- Lenguaje de programación: __Python__
- Versión de lenguaje: __Python 3.9.7__
- Framework utilizado: __DJango Rest Framework__
- Motor de base de datos: __MySQL__