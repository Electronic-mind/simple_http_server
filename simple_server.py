from http.server import HTTPServer, BaseHTTPRequestHandler

class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"GET request, \nPath: {self.path}\nHeader:\n{self.headers}\n")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"POST request, \nPath: {self.path}\nHeaders:\n{self.headers}\n\nBody:\n{post_data.decode('utf-8')}\n")
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
    
def run(server_class=HTTPServer, handler_class=CustomRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"My Server starting on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    httpd.server_close()
    print('My Server stopping httpd...\n')



if __name__ == '__main__':
    run()