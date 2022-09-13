# Sistema de gestión de contenido simple

Este proyecto busca crear un sistema para la administración de artículos y publicaciones.
Cosas que puedes realizar:

- Crear, leer, actualizar y borrar publicaciones. (CRUD)
- Crear, modificar y borrar usuarios.
- Agregar una imagen para cada publicación.


# Instalación

Para instalar este software necesitas:

## Revisar tu versión de python
Este proyecto fue escrito con python 3.10.5, por lo que recomiendo que lo pruebes con esta versión o una superior para evitar cualquier problema de compatiblidad.

Cómo reviso mi versión de python:

Ejecuto una terminal bash

en windows:

> python --version
> Python 3.10.5


## Instalar dependencias

Para instalar las dependencias necesitas correr `pip install`, asegurate que estas en la carpeta del proyecto y puedas ver el archivo `requirements.txt` cuando haces un `ls` o `dir`:

```bash
> pip install -r requirements.txt
```
Esto último traerá un montón de cosas en tu terminal.

Algunos sistemas operativos requerirán que utilizen pip3 en lugar de pip


### Migraciones

windows:
```bash
c:\> python mananage.py migrate
```

### Correr el test server

windows:
```bash
> python mananage.py runserver
```
windows:
```bash
c:\> py mananage.py runserver
```
Ir al localhost:8000/

para tener acceso a la aplicación

Si todo va bien, deberías poder abrir el navegador y ver la aplicación corriendo.
