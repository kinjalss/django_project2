from django.http import HttpResponse,HttpResponseNotFound
# def handler404(request,exception):
#     return HttpResponseNotFound('404-NOT FOUND.<p>THE PAGE YOU ARE LOOKING FOR DOES NOT EXIST <br><br> button onclick="" href='';"">Go to homepage')
# def home(request):
#     return HttpResponse("Little Lemon!")

def handler404(request, exception):
    return HttpResponseNotFound("""
        <h1>404 - NOT FOUND</h1>
        <p>THE PAGE YOU ARE LOOKING FOR DOES NOT EXIST</p>
        <br>
        <button onclick="window.location.href='/'">Go to homepage</button>
    """)

def home(request):
    return HttpResponse("Little Lemon!")