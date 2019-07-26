from django.shortcuts import render
from django.http import HttpResponse,Http404


# Create your views here.
def index(request):
  return render (request,'index.html')

def user_profile(request):  
  current_user = request.user
  profiles = Profile.objects.filter(user_id=current_user.id)[0:1]
  posts = Image.objects.filter(user_id=current_user.id)

  return render(request,'insta.html',{"profile_pic":profiles,"posts":posts})
