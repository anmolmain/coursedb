from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')  # Redirect to a list view or wherever you want
    else:
        form = PDFDocumentForm()
    return render(request, 'upload_pdf.html', {'form': form})




def home(request):
    return render(request, 'home.html')

def login(request):
    try:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Invalid Credential")
                return redirect("login")
        else:
            return render(request, "login.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("login")

# Register view to register user
def register(request):
    try:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exist")
                    return redirect("register")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email already registered")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1,
                    )
                    user.save()
                    return redirect("login")
            else:
                messages.info(request, "Password not matches")
                return redirect("register")
        else:
            return render(request, "register.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("register")

# Logout view to logout user
def logout(request):
    try:
        auth.logout(request)
        return redirect("/")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("/")

def courses(request):
    return render(request, 'courses.html')

def codeeditor(request):
    return render(request, 'codeeditor.html')

def pricing(request):
    return render(request, 'pricing.html')

def contactus(request):
    return render(request, 'contactus.html')

def css(request):
    return render(request, 'css.html')

def html(request):
    return render(request, 'html.html')

def Javascript(request):
    return render(request, 'Javascript.html')

def Bootstrap(request):
    return render(request, 'Bootstrap.html')

def ExpressJs(request):
    return render(request, 'express.html')

def React(request):
    return render(request, 'react.html')

def NodeJs(request):
    return render(request, 'nodejs.html')

def MongoDB(request):
    return render(request, 'mongodb.html')


