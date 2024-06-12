from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.views.generic import FormView

# Create your views here.

def insert_school_byfbv(request):
    ESFO = SchoolForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid:
            SFDO.save()
            return HttpResponse('insert_school_byfbv is done')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_school_byfbv.html',d)


class Insert_School_bycbv(FormView):
    template_name = 'insert_school_bycbv.html'
    form_class = SchoolForm
    
    def form_valid(self, form):
        form.save()
        return HttpResponse('Insert_School_bycbv is done')
    