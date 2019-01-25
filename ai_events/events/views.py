from django.shortcuts import render, get_object_or_404

from .models import Event

def index(request):
    latest_event_list = Event.objects.order_by('-start_date')[:3]
    context = {
        'latest_event_list': latest_event_list,
    }
    return render(request, 'events/index.html', context)

def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/html/event-page.html', {'event': event})
