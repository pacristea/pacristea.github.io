from django.shortcuts import render, redirect
from booking.models import Service, Mani, Extra
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ManiForm, ExtraForm, PediForm

extra_form = ExtraForm()
template = 'booking_service_detail.html'

# Create your views here.
def booking_index(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'booking_index.html', context)



def booking_service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    choose_form = [
        ManiForm, PediForm
    ]
    chosen = service.pk-1

    if request.method == 'POST':
        service_form = choose_form[chosen](request.POST)
        extra_filter = ['M', 'P', 'K']
        
        extra_form.fields['extra_title'].queryset = Extra.objects.filter(relation=extra_filter[chosen])
        
        return render(request, template, {
        'service': service,
        'chosen': extra_filter[chosen],
        'service_form': service_form,
        'extra_form': extra_form,
    })

    service_form = choose_form[chosen]()
    context = {
        'service': service,
        'service_form': service_form,
    }
    return render(request, template, context)