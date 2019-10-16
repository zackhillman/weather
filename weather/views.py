from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import SubscribeForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscribeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscribeForm()

    return render(request, 'index.html', {'form': form})

def thanks(request):
    return HttpResponse("Thanks for subscribing!")


