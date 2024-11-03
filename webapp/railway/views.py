from django.shortcuts import render
from django.db import connection
# Create your views here.
# Remember to write a view for every single page, then link the function in railway/urls.py to display the view

# view for the index page
def index(request):
    example = "hello"
    # let's test the mySQL database connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, user_password FROM loginTest")
        login_info = cursor.fetchall()
    # If you want to pass data into the html files, you include them here in context. 
    # Context is in JSON so you can add multiple pieces of information
    # check index.html to see how to display the information
    context = {
        'example': example,
        'login_info': [{'username': row[0], 'user_password': row[1]} for row in login_info]
    }
    return render(request, "railway/index.html", context)