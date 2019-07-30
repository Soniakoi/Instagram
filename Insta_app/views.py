from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Image,Comments
from .forms import NewProfileForm,NewCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
  images = Image.objects.all()
  return render (request,'index.html',{'images':images})


def user_profile(request):
  current_user = request.user
  profiles = Profile.objects.filter(user_id=current_user.id)[0:1]
  posts = Image.objects.filter(id=current_user.id)  

  return render(request,'insta.html',{"profile":profiles,"posts":posts})

def feeds(request):  
  comments= Comments.objects.all()
  profiles = Profile.objects.all()
  posts = Image.objects.all()

  return render(request,'feeds.html',{"posts":posts,"profiles":profiles,"comments":comments})

def search(request):
  if 'user' in request.GET and request.GET['user']:
      s_term=request.GET.get("user")
      found=Image.search_users(s_term)
      message=f'{s_term}'

      return render(request,'search.html',{'message':message,'founds':found,"term":s_term})
  else:
      message="You did not search any user please input a user name"
      return render(request,"search.html",{"message":message})

@login_required(login_url='/accounts/login')
def comments(request):
  current_user=request.user
  if request.method == 'POST':
    form = NewCommentForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = current_user
      post.save()
    return redirect('feed')

  else:
    form = NewCommentForm()
  return render(request,'comment.html',{"form":form})


@login_required(login_url='/accounts/login')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewImageForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = current_user
      post.save()
    return redirect('userProfile')

  else:
    form = NewImageForm()
  return render(request,'new_post.html',{"form":form})

@login_required(login_url='/accounts/login')
def profile(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      profile_pic = form.cleaned_data['Profile']
      # bio = form.cleaned_data['bio']
      Profile.objects.filter(user=current_user).update()
      profile.save()
    return redirect('userProfile')

  else:
    form = NewProfileForm()
  return render(request,'profile.html',{"form":form})


 