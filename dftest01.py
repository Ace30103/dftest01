from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request made")
        self.send_response(200) #200, OK
        self.send_header('content-type','application/json') #return type is a json / dictionary
        self.end_headers()
        self.wfile.write('{"out":0}'.encode())
         #the data that DF gets
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print("{post_body}")

server = HTTPServer(('0.0.0.0',8080),MyHandler)
server.serve_forever()
