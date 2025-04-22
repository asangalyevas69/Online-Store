from django.shortcuts import render
from django.views.generic import  ListView

def home(requests):
    # context = {
    #     'categories': Category.objects.all(),
    #     'tags': Tag.objects.all(),
    #     'publications': Publication.objects.all().order_by('-created')[:5]
    # }

    return render(request=requests, template_name='index.html')


