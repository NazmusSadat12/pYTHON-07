from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return HttpResponse("<h1> blog home page <h1>")


blog_post = [

    {

        "title": "Apartment sales slow for rising prices",
        "content": "An assessment of the Real Estate & Housing Association of Bangladesh (REHAB) shows that the cost of rod required per square feet increased by Tk 130, cement Tk 24.75, sand Tk 28.12 and stone chips Tk 78.75",
        "author": "DR JHON",
        "Date": "18 october 2023",
    },

]




def home(request):
    return render(request, 'blog/home.html',context={"blog_post": blog_post})




def about (request):
    return render(request, 'blog/about.html',context={"title": "About page "})






