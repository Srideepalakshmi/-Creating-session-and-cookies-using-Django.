from django.shortcuts import render, redirect
from django.http import HttpResponse

# Session-based login
def session_page(request):
    return render(request, 'ex5app/session.html')

def session_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # Create a session
        request.session['username'] = username
        request.session['email'] = email
        return render(request, 'ex5app/session_welcome.html', {'username': username})
    return redirect('session_page')

# Cookie-based login
def cookie_page(request):
    return render(request, 'ex5app/cookie.html')

def cookie_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        mobile = request.POST['mobile']
        # Create a cookie
        response = render(request, 'ex5app/cookie_welcome.html', {'username': username})
        response.set_cookie('username', username)
        response.set_cookie('mobile', mobile)
        return response
    return redirect('cookie_page')
