from django.shortcuts import render

def helloworld(request):
    return render(request,"helloworld/helloworld.html")

# Function below is passed also a variable, like it would be data context
def hellocareeria(request):
    name = "Simo"
    context = {'name': name }
    return render(request,"helloworld/hellocareeria.html",context)
