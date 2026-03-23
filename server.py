import http.server
import socketserver
import os

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.js': 'application/javascript',
    '.mjs': 'application/javascript',
    '.obj': 'text/plain',
    '.mtl': 'text/plain',
})

print(f"サーバー起動中: http://localhost:{PORT}")
print("終了するには Ctrl+C を押してください")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
