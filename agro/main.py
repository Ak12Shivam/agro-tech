import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}/index.html from templates/")
        webbrowser.open(f"http://localhost:{PORT}/index.html")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
