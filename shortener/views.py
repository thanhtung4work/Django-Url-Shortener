from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'index.html')

def create(request):
  if request.method == 'POST':
    url = request.POST['url']
    uid = str(uuid.uuid4())[:5]
    
    if url.startswith("https://"):
      url = url.replace("https://", '')
    if url.startswith("http://"):
      url = url.replace("http://", '')
    
    new_url = Url(link=url, uuid=uid)
    new_url.save()
    return HttpResponse(uid)

def redirect_to(request, id):
  url_details = Url.objects.get(uuid=id)
  return redirect(f"http://{url_details.link}")