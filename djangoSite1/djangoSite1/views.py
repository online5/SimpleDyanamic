from django.shortcuts import render
from datetime import datetime
from .models import Articles

def index(request):

    context = {
    'current_date':datetime.now(),
    'title':'Home'
    }
    return render(request,'index.html',context)

def about(request):
    context = {
    'current_date':datetime.now(),
    'title':'About'
    }
    return render(request,'about.html',context)

def news(request):


    articles = get_articles()
    populate_db()

    context = {
    'articles':articles,
    'current_date':datetime.now(),
    'title':'News'
    }
    return render(request,'news.html',context)



def get_articles():
    articles = Articles.objects.all()
    return articles

def populate_db():
    if Articles.objects.count() == 0:
        Articles(title = "Hustle", content = "I didn't Hustle Harder with discipline and stragetically").save()
        Articles(title = "Health", content = "I didn't work Harder on my health with discipline and stragetically").save()
        Articles(title = "Career", content = "I didn't work harder on my career with discipline").save()
