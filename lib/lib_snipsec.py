import requests
import json


class Snipsec:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Snipsec/1.0",
        }

    def get_headers(self):
        headers = []
        recommended_values = {}
        with open("./dictionary/template_web.json", "r") as file:
            template_data = json.load(file)
            web_headers = template_data.get("web", {})
            headers = list(web_headers.keys())
            for header, data in web_headers.items():
                recommended_values[header] = data.get("recommended_value", "")
        return headers, recommended_values



    def parse_headers(self, headers):
        if isinstance(headers, dict):
            return headers

        try:
            if isinstance(headers, str):
                headers_dict = json.loads(headers)
            else:
                headers_dict = json.loads(headers[0])
            return headers_dict
        except ValueError:
            raise ValueError("Formato JSON inválido para los encabezados.")


    def snip_request(self, url, method, headers=None, body=None):
        if headers is not None:
            headers_dict = self.parse_headers(headers)
            self.headers.update(headers_dict)

        if method.upper() == "GET":
            response = requests.get(url, headers=self.headers)
        elif method.upper() == "POST":
            response = requests.post(url, headers=self.headers, data=body)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=self.headers, data=body)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=self.headers)
        else:
            raise ValueError(f"Método HTTP inválido: {method}")

        return response
