import os
from http.cookies import SimpleCookie
from datetime import datetime, timedelta
import platform

#Lê cookies existentes

cookie = SimpleCookie(os.environ.get("HTTP_COOKIE"))

#Define novos cookies

lastsFor = (datetime.now(datetime.timezone.utc)+timedelta(days=7)).strftime("%a, %d-%b%Y &H:%M:%S GMT")
cookie["user-session"]="usuario123456789"
cookie["user-session"]["expires"]= lastsFor
cookie["user-session"]["path"]= "/"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cookie["ultima_visita"]=timestamp
cookie["referencia"]=os.environ.get("HTTP_REFERER", "desconhecido")
cookie["navegador"]= os.environ.get("HTTP_USER_AGENT", "desconhecido")
cookie["sistema"]= platform.system
cookie["modo_escuro"]= "desconhecido"

print("Content-Type: text/html")
for morsel in cookie.values():
    print(f"Set-Cookie:{morsel.OutputString()}")
    print() #separa os headers do HTML

#HTML da resposta

print("<html><body><h1>Cookie de Gustavo Ribeiro definido com sucesso</h1></body></html>")