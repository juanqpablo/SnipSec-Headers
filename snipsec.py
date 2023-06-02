from lib.lib_snipsec import Snipsec
from lib.animation import Animation
import colorama
from colorama import Fore
from colorama import Style
import argparse, time
from tabulate import tabulate

colorama.init(strip=False)


animation = Animation()

#---------------------------------------------------------------------------
#                             Print banner
#---------------------------------------------------------------------------
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



URL = "example.com"
#url_list = "./dictionary/list-headers.txt"
sec = Snipsec()
#security_headers =  ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options', 'Referrer-Policy', 'Feature-Policy']
security_headers = sec.get_headers()
res = sec.snip_request(URL)

print_banner()
animation.load_animation("Escaneando cabeceras de seguridad para <<"+URL+"+>>...")
print_banner()
print(" " * 12 + Fore.GREEN + "-"*80)
print(" " * 12 + Fore.GREEN + ">>> Resultados TARGET: <<"+URL+">>")
print(" " * 12 + Fore.GREEN + "-"*80)
print("")

max_length = max(len(str(i)) for i in security_headers)  # Obtiene la longitud máxima de los elementos en la lista

present_headers = []
missing_headers = []

# Obtener los encabezados y sus valores de configuración
headers = res.headers

for header in security_headers:
    if header in headers:
        present_headers.append(header)
        status = Fore.GREEN + "[ VALIDATED ]" + Style.RESET_ALL
        header_value = headers[header]
    else:
        missing_headers.append(header)
        status = Fore.YELLOW + "[  WARNING  ]" + Style.RESET_ALL
        header_value = "N/A"

    header_output = (
        Fore.GREEN
        + Style.BRIGHT
        + "[+]"
        + Style.RESET_ALL
        + " HEADER: "
        + str(header).ljust(max_length + 5)
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
        + "GET"
        + Style.RESET_ALL
        + Fore.WHITE
        + Style.BRIGHT
        + "]"
    )

    print(" " * 12 + header_output + column_output)
    print()
    print(" " * 14 + "- VALUE: " + header_value)
    print()

print("\n")
print(" " * 12 + Fore.GREEN + ">>> Proceso finalizado")
