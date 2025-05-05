#!/usr/bin/python3

import os
from http.cookies import SimpleCookie
from datetime import datetime, timedelta
import platform

#Lê cookies existentes

cookie = SimpleCookie(os.environ.get("HTTP_COOKIE"))

#Define novos cookies

lastsFor = (datetime.utcnow()+timedelta(days=7)).strftime("%a, %d-%B%Y &H:%M:%S GMT")
cookie["user-session"]="usuario123456789"
cookie["user-session"]["expires"]= lastsFor
cookie["user-session"]["path"]= "/"

cookie["sistema"]= platform.system()
cookie["navegador"]= os.environ.get("HTTP_USER_AGENT", "desconhecido")
cookie["referencia"]=os.environ.get("HTTP_REFERER", "desconhecido")
cookie["modo_escuro"]= "desconhecido"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cookie["ultima_visita"]=timestamp

print("Content-Type: text/html")
for morsel in cookie.values():
    print(f"Set-Cookie:{morsel.OutputString()}")
    print() #separa os headers do HTML

#HTML da resposta

print("<html><head><meta charset=\"UTF-8\"><\head><body><h1>Cookie de Gustavo Ribeiro definido com sucesso!!</h1><h3>Funções</h3><p>Esse cookie salva informações como o nome do usuário, última visita, navegador e sistema operacional. O cookie tem duração de 7 dias</p></body></html>")