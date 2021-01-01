"""
Tiene la clase base que junta todas las piezas
proporcionando una interfaz simple para la programación
"""

from mauweb.router import Router, Path
from mauweb.response import Response, FileResponse, Http404
from mauweb.response import Request

import os
from wsgiref.simple_server import make_server

class MauWeb:
    def __init__(self, **kwargs):
        self.router = Router()
        self.static_dir = None  # Mira el DIR del static
        self.static_path = None # Especifica el prefijo del archivo

    def set_static(self, static_path, static_dir):
        # Funciones para los statico (css, js, .mp4, etc)
        self.static_dir  = static_dir
        self.static_path = static_path
        
    
    def serve_static(self,request : Request):
        """Una vista para servir archivos estáticos que solo se agrega cuando el usuario establece las variables estáticas"""
        new_path = request.path[len(self.static_path)::] # conseguir el path actual
        return FileResponse(request, os.path.join(self.static_dir, new_path))


    def set_routes(self, routes : list):
        for path in routes:
            self.router.add_route(path)


    def __call__(self, environ, start_response):
        try:
            request = Request(environ, start_response)
            if self.static_path != None and  request.path.startswith(self.static_path):
                response = self.serve_static(request)
                return response.make_response()
            else:
                func = self.router.get_route(request.path)
                if func is not None:
                    response: Response = func(request)
                    return response.make_response()  
                else:
                    print(f'Ruta no encontrada :: {request.path}')
        except Exception as e:
            print(e)

        response =  Http404(request)
        return response.make_response()

    def run(self, _app, puerto: str = "127.0.0.1", host: int=8000):
        server = make_server(puerto, host, _app)
        print(f"Servidor creado en http://{puerto}:{host}")
        server.serve_forever()