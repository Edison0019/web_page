from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """
<ul>
    <li><a href = "/">Portada</a></li>
    <li><a href = "/about/">Acerca de</a></li>
    <li><a href = "/portafolio/">Portafolio</a></li>
    <li><a href = "/contact/">Contacto</a></li>
</ul>


"""
def home(request):
    return HttpResponse(html_base +
        "<h1>mi web personal</h1><h2>portada</h2>")

def about(request):
    return HttpResponse(html_base +
        '''<h1>mi web personal</h1>
        <h2>portada</h2>
        <p>Me llamo edison y soy programador</p>
        '''
    )

def portafolio(request):
    return HttpResponse(html_base +
        '''<h1>mi web personal</h1>
        <h2>portada</h2>
        <p>he hecho trabajos de programacion y de analisis de datos</p>
        '''
    )

def contact(request):
    return HttpResponse(html_base +
        '''<h1>mi web personal</h1>
        <h2>portada</h2>
        <p>my numero es 999-999-9999 y mi correo es example@example.com</p>
        '''
    )