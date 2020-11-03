# Fuego de Quasar

---

## Requisitos

- [Python 3.8](https://www.python.org/downloads/)
- [Postman](https://www.postman.com/downloads/)

## Instalar dependencias
Dentro del repositorio:
```sh
> pip install requirements.txt
```

## Ejecución
Dentro del repositorio:
```sh
> python main.py
```
La aplicación se ejecuta por defecto en el puerto 5000.

## Endpoints

### POST /api/v1/topsecret/
El request deberá tener el siguiente formato:
```
{
    "satellites": [
        {
            "name": "kenobi",
            "distance": 584.5,
            "message": ["este", "", "", "mensaje", ""]
        },
        {
            "name": "skywalker",
            "distance": 226.1,
            "message": ["", "es", "", "", "secreto"]
        },
        {
            "name": "sato",
            "distance": 500.0,
            "message": ["este", "", "un", "", ""]
        }
    ]
}
```
_Es importante que respeten los nombres de los satélites._

La respuesta, en caso de ser correcta, tendrá el siguiente formato:
```
{
    "message": "este es un mensaje secreto",
    "position": {
        "x": 0.0,
        "y": 102.8
    }
}
```

En el caso de que la posición o el mensaje no puedan ser determinados, responderá de la siguiente manera:
```
{
    "info": "Message or position cannot be determined",
    "message": "Resource not found"
}
```

En el caso de que el JSON sea inválido, responderá se la siguiente manera:
```
{
    "info": "Invalid JSON",
    "message": "Bad request"
}
```

### POST /api/v1/topsecret_split/<nombre_satelite>
El request deberá tener el siguiente formato:
```
{
    "distance": 500.0,
    "message": ["este", "", "un", "", ""]
}
```
_<nombre_satelite> deberá ser reemplazo por: **kenobi**, **skywalker**, o **sato**._

La respuesta, en caso de ser correcta, tendrá el siguiente formato:
```
{
    "distance": 500.0,
    "message": [
        "este",
        "",
        "un",
        "",
        ""
    ]
}
```

En el caso de que el nombre sea inválido, responderá se la siguiente manera:
```
{
    "info": "Invalid name",
    "message": "Bad request"
}
```

En el caso de que el JSON sea inválido, responderá se la siguiente manera:
```
{
    "info": "Invalid JSON",
    "message": "Bad request"
}
```

### GET /api/v1/topsecret_split
Es necesario que, para obtener una respuesta correcta, se hayan cargado los datos de los sátelites mediante el método POST del mismo endpoint.

La respuesta, en caso de ser correcta y tener los datos necesarios, tendrá el siguiente formato:
```
{
    "distance": {
        "x": 0.0,
        "y": 102.8
    },
    "message": "este es un mensaje secreto"
}
```

En el caso de que la posición o el mensaje no puedan ser determinados, responderá de la siguiente manera:
```
{
    "info": "Message or position cannot be determined",
    "message": "Resource not found"
}
```

En el caso de que falten datos de los satélites, responderá se la siguiente manera:
```
{
    "info": "Information is missing",
    "message": "Bad request"
}
```

#### Link de utilidad

[Geogebra](https://www.geogebra.org/calculator)
