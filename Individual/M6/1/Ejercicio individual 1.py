from http.server import BaseHTTPRequestHandler, HTTPServer

#Django es una herramienta, es un framework todo en uno pilas incluidas capaz de contruir aplicaciones web veloces
#y seguras en poco tiempo. las principales caracteristicas de Django son su manejo de requests y el uso de ORM para
#gestion de datos.

#Existen formas de hacer aplicaciones web en python sin django, se puede hacer directamente gracias a la libreria http.server
#u otros medios, tambien existen otros frameworks en python como flask o fastAPI


#Para levantar un servidor sin django se puede usar el siguiente script
class HttpRequest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) #respuesta a entregar
        self.send_header('Content-type', 'text/html') #tipo de contenido
        self.end_headers() #cierre de header
        self.wfile.write(b"<h1>Hola, Soy un servidor</h1>") #contenido del paquete

def run(server_class=HTTPServer, handler_class=HttpRequest, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server listening on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

#para crear un proyecto django primero se instala django utilizando pip install django, una vez instalado django
#se utiliza django-admin startproject <nombre_proyecto> lo cual creara los archivos necesarios para trabajar 
#con django