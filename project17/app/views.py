from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.
def School_list_fbv(request):
    schools = School.objects.all()
    d = {'schools': schools}
    return render(request, 'School_list_fbv.html', d)


class School_List_cbv(ListView):
    model = Student
    context_object_name = 'schools'
    template_name = 'School_List_cbv.html'
    ordering = ['sname']