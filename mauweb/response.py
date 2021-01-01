from mauweb.request import Request
import json

# todo: Agregue más tipos de contenido para varios archivos
file_content_types = {
    'html': 'text/html',
    'htm':  'text/html',
    'css':  'text/css',
    'js':   'text/javascript',
    'mkv':  'video/mkv',
}

class Response:

    __slots__ = 'headers', 'status_code', 'start_response', 'content_type', 'response_content'

    def __init__(self,request: Request, status_code: str, content_type: str):
        self.headers = []
        self.status_code = status_code
        self.start_response = request.start_response
        self.content_type = content_type
        self.response_content = []
        
    def make_response(self):
        self.start_response(self.status_code, [('Content-Type', self.content_type)])
        return self.response_content         


class HttpResponse(Response):
    """
    Devuelve una respuesta http pura cuando se le da un texto como contenido
    """
    def __init__(self, request: Request, content, status_code='200 OK', content_type='text/html'):
        super().__init__( request, status_code, content_type)
        if type(content) == str:
            content = content.encode()
        self.response_content.append(content)


class RenderResponse(HttpResponse):
    """Utiliza HttpResponse para devolver la respuesta http dado un nombre de plantilla y un diccionario de contexto"""
    # Todo: Implementar una forma de renderizar contenido dinámico desde el contexto en plantillas

    def __init__(self, request: Request, filename: str, context: dict = {}):
        try:
            with open(filename, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(f'Error al abrir el archivo :: {filename}')
            raise Exception(f'No se pudo encontrar el archivo :: {filename}')
        super().__init__(request, text, '200 OK')


class JsonResponse(Response):
    """
    Devuelve la respuesta json pura cuando se le da un texto como contenido
    """
    def __init__(self, request: Request, content, status_code='200 OK', content_type='application/json'):
        content = json.dumps(content)
        super().__init__( request, status_code, content_type)
        self.response_content.append(content.encode())

class FileResponse(HttpResponse):
    def __init__(self,  request: Request, filename: str, file_root:str=""):
        try:
            with open(file_root+filename, 'rb') as f:
                content = f.read()
        except FileNotFoundError:
            print(f'Archivo no encontrado {filename}')
            raise Exception(f'No se pudo encontrar el archivo :: {filename}')
        
        content_type = file_content_types.get(filename.split('.')[-1], 'text/plain')
        
        super().__init__( request, content, '200 OK',content_type )


class ErrorResponse(Response):
    def __init__(self, request: Request, error_code: str):
        super().__init__(request, '404 No se encontro. Intenta mirar si has puesto la url bien', 'text/html')
        self.response_content.append("404 No se encontro. Intenta mirar si has puesto la url bien".encode())


class Http404(ErrorResponse):
    def __init__(self, request):
        super().__init__(request, '404 No se encontro. Intenta mirar si has puesto la url bien')

