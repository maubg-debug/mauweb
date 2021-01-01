from mauweb import MauWeb, Path
from mauweb.response import HttpResponse, RenderResponse, JsonResponse, FileResponse

app = MauWeb()
app.set_static('/static/', '.')

def print_received(request):
    print(request.query_string)
    return RenderResponse(
        request,
    'ejemplo.html',
    None
    )

def json_point(request):
    
    data = [{'hola': 'hey', 'tu':'yo'},
    {'nombre': 'Maubg', 'años': 12308},
    {'nombre': 'Maubg', 'años': 34},
    {'nombre': 'Maubg', 'años': 21}

    ]
    return JsonResponse(request,data)

def form(request):
    if request.method == "POST":
        age = request.post.get('age')
        return HttpResponse(request, age.file.name)
    return HttpResponse(request,"""
    <html>
    <body>
    <form method="post" action="", enctype="multipart/form-data">

    <input type="file" id="age" name="age" value="age">
    <input type="submit" value="submit">
    </form>

    </body>
    </html>
    """)

def fileRes(request):
    return FileResponse(request,"./ejemplo.css")

        
routes = [
    Path('/', print_received),
    Path('/json/', json_point),
    Path('/form/', form),
    Path('/file/', fileRes),
]

app.set_routes(routes)

if __name__=='__main__':
    app.run(app)

