from django.shortcuts import render
from event.models import Event
from django import forms
from django.views.decorators.csrf import csrf_exempt

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


def myevent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            form = EventForm()
            return render(request, 'event.html', {'form': form})
    else:
        form = EventForm()
    return render(request, 'event.html', {'form': form})
