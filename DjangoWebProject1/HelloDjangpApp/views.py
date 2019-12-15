from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()

    return render(request,
        "HelloDjangpApp\index.html",
        {
            'title':"Hello Django",
            'message':"Hello Django",
            'content':" on " + now.strftime("%A, %d %B, %Y at %X")
        }
)


#def index(request):
#    now = datetime.now()

#    html_content = "<html><head><title>Hello, Django</title></head><body>"
#    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "</body></html>"

#    return HttpResponse(html_content)