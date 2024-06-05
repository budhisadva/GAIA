from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def base(request):
    users = User.objects.all().exclude(id=request.user.id)
    print(users)
    return render(request, 'Administracion.html', {
        'usuarios': users
    })
