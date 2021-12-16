from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    data='''<html>
    <head><title>home page</title></head>
    <body>
    <h2> welcome to my youtube clone</h2>
    <marquee> <b><h1>Task Completed Sir</h1></b> </marquee>
    </body>
    </html>
    '''
    return HttpResponse(data)

def hello(request):
    return render(request,'index.html')