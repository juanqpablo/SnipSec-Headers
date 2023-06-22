import argparse
from urllib.parse import urlparse
import json
from lib.lib_snipsec import Snipsec
from lib.animation import Animation
import colorama
from colorama import Fore, Style

colorama.init(strip=False)

animation = Animation()


def print_banner(title=""):
    print(Fore.CYAN + """
             ██████╗███╗  ██╗██╗██████╗  ██████╗███████╗ █████╗
            ██╔════╝████╗ ██║██║██╔══██╗██╔════╝██╔════╝██╔══██╗
            ╚█████╗ ██╔██╗██║██║██████╔╝╚█████╗ █████╗  ██║  ╚═╝
             ╚═══██╗██║╚████║██║██╔═══╝  ╚═══██╗██╔══╝  ██║  ██╗
            ██████╔╝██║ ╚███║██║██║     ██████╔╝███████╗╚█████╔╝
            ╚═════╝ ╚═╝  ╚══╝╚═╝╚═╝     ╚═════╝ ╚══════╝ ╚════╝
            ████████████████████████████████████████████████████

                                    █ █ █▀▀ ▄▀█ █▀▄ █▀▀ █▀█ █▀
                                    █▀█ ██▄ █▀█ █▄▀ ██▄ █▀▄ ▄█
                                        @4r13s > v.0.0.1 Release (Beta)
    """ + Style.RESET_ALL)

def scan_headers(url=None, headers=None, method=None, body=None, request_file=None):
    sec = Snipsec()
    security_headers, recommended_values = sec.get_headers()
    headers_dict = None

    if headers is not None:
        headers_dict = sec.parse_headers(headers)

    if request_file:
        # Leer el contenido del archivo de solicitud de BurpSuite
        with open(request_file, "r") as file:
            request_content = file.read()

        # Obtener el método, los encabezados y el cuerpo del request
        request_lines = request_content.strip().split("\n")
        method = request_lines[0].split(" ")[0]
        request_headers = request_lines[1:request_lines.index("")]

        # Crear un diccionario de encabezados
        headers_dict = {}
        for line in request_headers:
            header, value = line.split(": ")
            headers_dict[header] = value

        # Obtener el cuerpo del request
        body = "\n".join(request_lines[request_lines.index("") + 1:]).strip()

        # Obtener la URL del archivo de solicitud
        url = headers_dict.get('Host') or url

    if url is None:
        raise ValueError("Debe proporcionar una URL o un archivo de solicitud")

    res = sec.snip_request(url, method, headers_dict, body)

    print_banner()
    animation.load_animation(f"Escaneando cabeceras de seguridad para <<{url}>>...")
    print("\n")
    print(" " * 12 + Fore.GREEN + "-" * 80)
    print(" " * 12 + Fore.GREEN + f">>> Resultados TARGET: <<{url}>>")
    print(" " * 12 + Fore.GREEN + "-" * 80)
    print("")

    max_length = max(len(str(i)) for i in security_headers)  # Obtiene la longitud máxima de los elementos en la lista

    # Obtener los encabezados y sus valores de configuración
    headers = res.headers.items()

   # Obtener los encabezados de seguridad y sus valores de configuración
    for header in security_headers:
        recommended_value = recommended_values.get(header, "")
        header_value = res.headers.get(header, "")

        if header_value == recommended_value:
            status = Fore.GREEN + "[ VALIDATED ]" + Style.RESET_ALL
            #INFO = "La cabecera se encuentra configurada correctamente."
        else:
            status = Fore.YELLOW + "[  WARNING  ]" + Style.RESET_ALL
            INFO = "Cabecera no configurada o no posee valores recomendados."

            if header_value!="":
                INFO += " Valor de configuración actual: " + header_value

        header_output = (
            Fore.GREEN
            + Style.BRIGHT
            + "[+]"
            + Style.RESET_ALL
            + " HEADER: "
            + header.ljust(max_length + 5)
            + Fore.WHITE
            + Style.BRIGHT
        )
        column_output = (
            "STATUS: "
            + status
            + Fore.WHITE
            + Style.BRIGHT
            + " METHOD: ["
            + Fore.CYAN
            + Style.BRIGHT
            + method.upper()
            + Style.RESET_ALL
            + Fore.WHITE
            + Style.BRIGHT
            + "]"
        )

        print(" " * 12 + header_output + column_output)
        print()
        if header_value!="":
            print(" " * 14 +   " ["
                                + Fore.BLUE
                                + Style.DIM +  Fore.WHITE
                                + "VALUE"
                                + Style.RESET_ALL
                                + Fore.WHITE
                                + Style.BRIGHT
                                + "] " + header_value)
            print()
        if header_value== "" or header_value==None:
            print(" " * 14 +    " ["
                                + Fore.CYAN
                                + Style.BRIGHT
                                + "INFO"
                                + Style.RESET_ALL
                                + Fore.WHITE
                                + Style.BRIGHT
                                + "] " + INFO)

        print()
    print("\n")
    print(" " * 12 + Fore.GREEN + ">>> Proceso finalizado")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan security headers")
    parser.add_argument("--url", type=str, help="Target URL/domain/endpoint")
    parser.add_argument("--headers", type=str, help="Headers in JSON format or as a string")
    parser.add_argument("--method", type=str, help="HTTP method for the request")
    parser.add_argument("--body", type=str, help="Request body")
    parser.add_argument("--request-file", type=str, help="Path to the BurpSuite request file (save request when copy to file)")
    args = parser.parse_args()

    # Agrega esquema "http://" si no está presente en la URL
    if not urlparse(args.url).scheme:
        args.url = "http://" + args.url

    if args.method is None:
        args.method = "GET"

    scan_headers(args.url, args.headers, args.method, args.body, args.request_file)
