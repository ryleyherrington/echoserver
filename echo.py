#!/usr/bin/env python
#Literally just echo's out get or post requests and values 
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class EchoHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        request_path = self.path
        print("Request\n")
        print(request_path)
        print(self.headers)
        
        self.send_response(200)
        #self.send_header("Set-Cookie", "test=localhost")
        
    def do_POST(self):
        request_path = self.path
        print("Request\n")
        print(request_path)
        
        request_headers = self.headers
        cl = request_headers.getheaders('content-length')
        if cl:
            length = int(cl[0])
        else:
            length = 0

        print(request_headers)
        print(self.rfile.read(length)) #http://docs.python.org/2/library/socketserver.html
        self.send_response(200)
    
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    print('Echoing out localhost:8080')
    server = HTTPServer(('', 8080), EchoHandler)
    server.serve_forever()
        
if __name__ == "__main__":
    main()
