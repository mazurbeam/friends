from django.shortcuts import render, redirect
from .models import User, Friend
import datetime
# Create your views here.
def checkUser(request):
	try:
		if request.session['f_name'] < 3:
			return False
		else:
			return True
	except:
		return False

def index(request):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    context = {
        'users': User.objects.all()
    }
    return render(request, 'friends/index.html', context)

def findfriend(request):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    context = {
        'users': User.objects.all().exclude(id=request.session['user_id'])
    }
    return render(request, 'friends/addfriend.html', context)

def addfriend(request, id):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    friend = Friend.objects.create()
    friend.save()
    friend.users = [id, request.session['user_id']]

    return redirect('/friends/findfriend')

def viewfriends(request):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    context = {
        "friends": Friend.objects.exclude(id=request.session['user_id'])

    }

    return render(request, 'friends/friends.html', context)

def remove(request,id):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    Friend.objects.get(id=id).delete()
    return redirect('/friends/viewfriends')
