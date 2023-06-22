# SnipSec Headers

## Descripción

La Herramienta ***SnipSec Headers*** es una herramienta de análisis de seguridad diseñada para evaluar la configuración de las cabeceras de seguridad en aplicaciones web y APIs. Proporciona una forma rápida y sencilla de escanear y verificar la presencia y configuración adecuada de diversas cabeceras de seguridad comunes.

La herramienta utiliza la biblioteca `requests` de Python para enviar solicitudes HTTP a un objetivo especificado y analizar las cabeceras de respuesta para determinar si se cumplen las mejores prácticas de seguridad. Proporciona resultados detallados que indican qué cabeceras están presentes y cuáles no, junto con recomendaciones sobre los valores de configuración recomendados.

## Características

- Escaneo de cabeceras de seguridad en aplicaciones web y APIs.
- Comprobación de la presencia y configuración adecuada de diversas cabeceras de seguridad.
- Resultados detallados que indican qué cabeceras están presentes y cuáles no.
- Configuración personalizable para agregar nuevas cabeceras de seguridad.
- Soporte para diferentes métodos de solicitud HTTP (GET, POST, PUT, DELETE, etc.).
- Compatible con URLs y archivos de solicitud de BurpSuite.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.
3. Ejecuta la herramienta con los comandos adecuados.



### Argumentos Disponibles

- `--url URL`: Especifica la URL del objetivo para escanear las cabeceras de seguridad.

- `--headers HEADERS`: Proporciona los encabezados en formato JSON o como una cadena. Se utilizarán para realizar la solicitud.

- `--method METHOD`: Especifica el método HTTP para la solicitud. Por defecto es GET.

- `--body BODY`: Proporciona el cuerpo de la solicitud.

- `--request-file REQUEST_FILE`: Especifica la ruta al archivo de solicitud de BurpSuite. Si se proporciona este argumento, se ignorarán los argumentos URL, headers, method y body.


## Uso

Aquí se proporcionan ejemplos de cómo usar la herramienta con diferentes opciones:

```
python snipsec.py --url example.com
python snipsec.py --url example.com --headers '{"Header1": "Value1", "Header2": "Value2"}'
python snipsec.py --url example.com --method POST --body '{"key": "value"}'
python snipsec.py --request-file request.txt

Para obtener una lista completa de opciones y argumentos, ejecuta python snipsec.py --help
```


Para obtener una lista completa de opciones y argumentos, ejecuta `python snipsec.py --help`.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error, tienes una idea de mejora o deseas agregar nuevas características, siéntete libre de abrir un problema o enviar una solicitud de extracción.

## Licencia

Este proyecto está licenciado bajo la Licencia GLPv2. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

## Contacto

Si tienes alguna pregunta o consulta, no dudes en ponerte en contacto conmigo en [dev4r13s@gmail.com](mailto:dev4r13s@gmail.com).
