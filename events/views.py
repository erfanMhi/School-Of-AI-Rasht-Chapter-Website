from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Event, Lecture, Lecturer, Category



def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    lecturers = []
    print('event.lecture_set', event.lecture_set.all())
    print('event.lecture_set', type(event.lecture_set))
    try:
        for lecture in event.lecture_set.all(): 
            lecturers.append(lecture.lecturer)
    except TypeError:
        pass
    return render(request, 'events/event-page.html', {'event': event, 'lecturers': lecturers, 'user': request.user})

def events_page(request, page=1, category_id=None):
    if category_id is not None:
        events_list = []
        category = get_object_or_404(Category, pk=category_id)
        for event in Event.objects.all():
            if category in Event.categories.all():
                events_list.append(event)
    else:
        events_list = Event.objects.all()
    paginator = Paginator(events_list, 2)
    events = paginator.get_page(page)

    print("events_length", len(events_list))
    print("events_length", page)

    return render(request, 'events/events-page.html', {'events': events, 'user': request.user})

