from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# resquest -> handler

def say_hello(request):
    return render(request,'hello.html')

@csrf_exempt
def open_form(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        print("Data recebida:", data)

        return JsonResponse({'status': 'sucesso', 'data': data})
    elif request.method == 'GET':
        return render(request, 'formulario.html')
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

def handle_post(request):
    return