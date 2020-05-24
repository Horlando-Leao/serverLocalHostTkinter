import os
import platform
import sys
from datetime import datetime
import time
from threading import Thread

try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from socketserver import TCPServer as Server
    #mostrar em tela
    protocolo = print(('[TCP] IMPORT - ({})'.format(Server)))
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server
    #mostrar em tela
    procolo = print(('[HTTP] IMPORT - ({})'.format(Server)))
    