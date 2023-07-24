from django.urls import reverse
from django.template import loader
from .models import SparePart
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    spare_parts = SparePart.objects.all().values()
    template = loader.get_template('home.html')

    context = {
        'spare_part':spare_parts
    }

    return HttpResponse(template.render(context,request))

def add(request):
    addSparePart = loader.get_template('addSparePart.html')
    return HttpResponse(addSparePart.render({},request))

def addSparePart(request):
    a = request.POST['part_name']
    b = request.POST['part_number']
    c = request.POST['arrival_date']
    d = request.POST['total_initial_stock_quantity']
    e = request.POST['country_of_origin']
    f = request.POST['branch_name']
    g = request.POST['category']

    spare_part = SparePart(part_name=a,part_number=b,arrival_date=c,total_initial_stock_quantity=d,
                           country_of_origin=e,branch_name=f,category=g
                           )
    spare_part.save()
    return HttpResponseRedirect(reverse('home'))