from django.shortcuts import render, get_object_or_404

from .models import Event



def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event-page.html', {'event': event})
