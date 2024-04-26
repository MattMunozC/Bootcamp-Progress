Existen distintos tipos de solicitudes, los principales son GET y POST.
la principal diferencia es el proposito de ambas semanticas, GET entrega los datos atraves de la URL (Consulta URI)
por lo que la cantidad de datos que puede entregar son limitados, visibles y preferentemente de naturaleza poco 
sensible, por lo que general se utiliza para solicitar informacion del servidor, POST, por otro lado, entrega los 
datos en el cuerpo de la solicitudad por lo que son privados, ilimitados y se espera que por aqui se entregue la
información delicada, por lo mismo, por este medio se sube infomación al servidor

Si se desea utilizar un formulario para generar datos se puede utilizar django.forms.Form:

Pasos a seguir:
1.Crear un archivo forms.py en la raiz de la aplicacion

mi_app/
    __init__.py
    admin.py
    apps.py
    forms.py    # <- Aqui
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
project/
    __pycache__/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py

2.Se importa django.forms
3.Dentro del archivo se crea una clase hijo de forms.Form
4.Se agregan los datos que se desean dentro la clase
5.Se importa el formulario a la vista y se le entrega dentro del contexto al html
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
6.Para crear un modelo se crea una clase hijo de models.Model y se rellena con los atributos del modelo
7.Se crea la migración con el comando python manage.py makemigrations
8.Se migra con el comando python manage.py migrate
9.Ahora se puede utilizar en modelo importandolo a la vista 
    import mi_app.models import [modelo]
    
