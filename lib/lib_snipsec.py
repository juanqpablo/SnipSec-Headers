import requests as rq

class Snipsec:

    """
    - Método que realiza request para obtener los headers
    """
    def snip_request(self, URL):
        res = rq.get(URL)

        return res


    def get_headers(self):
        with open( "./dictionary/list-headers.txt", "r") as file:
            # Leer las líneas del archivo
            lines = file.readlines()
            # Obtener los encabezados (líneas que tienen el formato "Header: valor")
            headers = [line.rstrip() for line in lines]
        return headers
