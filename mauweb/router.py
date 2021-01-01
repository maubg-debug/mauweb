
class Path:
    """
    Clase para sujetar caminos. facilita la comprobación de coincidencias
    """

    __slots__ = 'path', 'func'

    def __init__(self, _path: str, _func):
        self.path = _path
        self.func = _func

    
    def match(self, _path):
        # Todo: Cambiar para admitir URL dinámicas como
        # / <int: id> / al igual que lo hace django para que podamos extraer variables
        if self.path == _path:
            return True
        return False
    

class Router:
    """
    Mantiene todas las rutas en una lista. Cuando llega la conexión, se utiliza para comprobar cuál de esos
    las rutas coinciden con la URL
    """
    __slots__ = 'routes'
    def __init__(self, routes:list=None):
        self.routes:list = list(routes) if routes else []

    def add_route(self,  _path: Path):
        self.routes.append(_path)
        return True
        

    def get_route(self, path_):
        for path in self.routes:
            if path.match(path_):
                return path.func
        


