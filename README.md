# mauweb
* Un web framework para python

# ¿Como se usa?

* Primero instalatelo
    ```
    pip install MauWeb
    ```
* Crea un pequeño set up
    ```python
    from mauweb import MauWeb, Path
    from mauweb.response import HttpResponse, RenderResponse, JsonResponse, FileResponse

    app = MauWeb() # Inicializacion
    app.set_static('/static/', '.') # Se usaria asi (https://github.com/maubg-debug/mauweb/blob/main/examples/ejemplo.html#L4)

    def print_received(request): # La funcion que quieras. Parametro :: request (Puedes hacer cosas como si es un 'POST' o 'GET'). Haz debuging

        print(request.query_string)
        return RenderResponse( # Todos se pueden importar como pone ariba
            request, # ¡Siempre!
            'ejemplo.html', # En este caso el archivo
            None # Context
        )
            
    routes = [
        Path('/', print_received), # Añade todos los routers
        # Para mas seguridad pon (Path('/awd/', print_received)) y Path('/algo', print_received)
        # Para un slash y sin.
    ]

    app.set_routes(routes) # Añade los routers

    if __name__=='__main__': # venga ya
        app.run(app) # Correr. Puedes poner como argumentos (ademas de app que es abligatorio) :: El puerto, el host
    ```

    * Mas ejemplos en [github](https://github.com/maubg-debug/mauweb/tree/main/examples)

# Licencia
* Miralo en nuestro [github](https://github.com/maubg-debug/mauweb/blob/main/LICENSE.md)
