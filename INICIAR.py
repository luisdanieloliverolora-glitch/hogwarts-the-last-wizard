import http.server, socket, os, webbrowser
from pathlib import Path
os.chdir(Path(__file__).resolve().parent)
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    try:
        s.connect(("192.0.2.1",80)); ip=s.getsockname()[0]
    except OSError: ip="127.0.0.1"
server=http.server.ThreadingHTTPServer(("0.0.0.0",8000),http.server.SimpleHTTPRequestHandler)
print("En iPhone/iPad abre Safari: http://"+ip+":8000",flush=True)
webbrowser.open("http://localhost:8000")
server.serve_forever()
