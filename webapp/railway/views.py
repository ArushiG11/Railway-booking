from django.shortcuts import render
from django.db import connection
# Create your views here.
# Remember to write a view for every single page, then link the function in railway/urls.py to display the view

# view for the index page

def index(request):
    example = "hello"
    login_info = None
    context = {}

    if request.method == 'POST':
        
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # let's test the mySQL database connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM loginTest WHERE username = %s AND user_password = %s",
                        [username, password])
                login_info = cursor.fetchall()
            # If you want to pass data into the html files, you include them here in context. 
            # Context is in JSON so you can add multiple pieces of information
            # check index.html to see how to display the information

            if login_info:
                message = "Log in successful!"
            else:
                message = "Invalid credentials"
    
            context['message'] = message
            #return render(request, "railway/index.html", context)
        
        elif 'logout' in request.POST:
            context['message'] = "Successfully logged out."
            
    return render(request, "railway/index.html", context)


