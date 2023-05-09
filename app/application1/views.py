from django.shortcuts import render , redirect
from .models import TEACHER, HEADMAN
from .forms import HEADMANForm, TEACHERForm
from django.views.generic import DetailView ,DeleteView



class BLANCHEADMAN(DetailView):
    model = HEADMAN
    template_name = 'application1/BLANCHEADMAN.html'
    context_object_name = 'headman'

class DELETHEADMAN(DeleteView):
    model = HEADMAN
    success_url = '/HomeWork/Look/'
    template_name = 'application1/DELET.html'


class BLANCTEACHER(DetailView):
    model = TEACHER
    template_name = 'application1/BLANCTEACHER.html'
    context_object_name = 'teacher'

class DELETTEACHER(DeleteView):
    model = TEACHER
    success_url = '/HomeWork/Look/'
    template_name = 'application1/DELET.html'

def home(request):
    return render(request,'application1/Home.html')
def HTLook(request):
    TEACHERdef = TEACHER.objects.all()
    HEADMANdef = HEADMAN.objects.all()
    return render(request,'application1/HTLook.html', {'TEACHERdef': TEACHERdef ,'HEADMANdef': HEADMANdef})

def HTAddT(request):

    error = ''
    if request.method == 'POST':
        form = TEACHERForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/HomeWork/Look')
        else:
            error = 'Форма заполнена неверно!!!'


    form1 = TEACHERForm()

    formDate1 = {
        'form1':form1
    }

    return render(request,'application1/HTAddT.html',formDate1)

def HTAddH(request):
    error = ''
    if request.method == 'POST':
        form = HEADMANForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/HomeWork/Look')
        else:
            error = 'Форма заполнена неверно!!!'


    form = HEADMANForm()

    formDate = {
        'form':form
    }

    return render(request,'application1/HTAddH.html',formDate)