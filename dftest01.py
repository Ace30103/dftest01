from http.server import HTTPServer, BaseHTTPRequestHandler

vars = {}
class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)

server = HTTPServer(('0.0.0.0',8080),MyHandler)
server.serve_forever()
