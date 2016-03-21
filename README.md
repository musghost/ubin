# [ubin] (http://ubin.mx/)
Primera comunidad Inmobiliaria.

# Requerimientos 

- Python 2.7 
- Postgres 9.3.9 > 9.3.10
- Django 1.8.4
- Django Rest Framework 3.2.3
 
La lista de los requerimientos se pueden ver [aquí](https://github.com/devMellow/ubin/blob/master/ubin_rest/requirements.txt).

# Instalar requerimientos.

```
$ install -r requirements.txt

```

# Correr el proyecto 

Para correr el proyecto es necesario:
- Tene una base de datos en postgres con el nombre de ***ubinrest***.
- La base de datos ***ubinrest*** debe pertenecer a el usuario especificado en settings.
- El usuario debe tener la cotraseña especificada en settings.
- Correr las migraciones:

```
$ ./manage.py migrate

```
- Correr el proyecto:

```
$ ./manage.py runserver

```

# Actualizar migraciones
Cuando se modifiqué un modelo es necesario :
- Actualizar migraciones.
```
$ ./manage.py makemigrations apprest

```
- Correr migraciones.

```
$ ./manage.py migrate

```
# [Documentación API RESTful UBIN] (http://api.ubin.mx/api/v1/docs/)
Para poder tener acceso a la documentación es necesario autenticarse, para ello se debe hacer lo siguiente:

- Pedir un usuario con el role de administrador para poder revisar la documentacion.
- [Loguearse] (http://api.ubin.mx/api/v1/admin/login/)
- Igresar a [http://api.ubin.mx/api/v1/docs/](http://api.ubin.mx/api/v1/docs/)

En caso de que no este logueado como administrador, no podrá accesar a la documentación.

# Mejoras a relizar
- Virtualización de ambiente de desarrollo.
- Portabilidad de configuraciones.
- Enviroments.

# Contributors
- Andrés Cidel.
- Gloria Palma.



