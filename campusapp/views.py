from django.shortcuts import render
from .models import Event
from .forms import RegistrationForm


def home(request):

    query = request.GET.get('q')
    category = request.GET.get('category')

    events = Event.objects.all()

    if query:
        events = events.filter(title__icontains=query)

    if category:
        events = events.filter(category__icontains=category)

    return render(request, 'home.html', {'events': events})


def event_detail(request, id):

    event = Event.objects.get(id=id)

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            registration = form.save(commit=False)

            registration.event = event

            registration.save()

            return render(request, 'success.html')

    else:

        form = RegistrationForm()

    return render(request, 'detail.html', {
        'event': event,
        'form': form
    })


def about(request):
    return render(request, 'about.html')


def gallery(request):

    events = Event.objects.all()

    return render(request, 'gallery.html', {
        'events': events
    })
def contact(request):
    return render(request, 'contact.html')