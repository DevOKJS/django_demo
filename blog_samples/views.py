from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog_samples/index.html")


def post(request):
    return render(request, "blog_samples/post.html")

def contact(request): 
    return render(request, "blog_samples/contact.html")