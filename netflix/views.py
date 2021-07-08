from django.shortcuts import render

# Create your views here.
def index(request):
  title = 'Netflic clone Homepage'

  return render(request, 'index.html', {'title':title})