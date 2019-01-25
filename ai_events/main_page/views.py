from django.shortcuts import render, get_object_or_404
# Create your views here.
from events.models import Event


# Create your models here.
def index(request):
    latest_event_list = Event.objects.order_by('-start_date')[:3]
    context = {
        'latest_event_list': latest_event_list,
    }
    return render(request, 'main_page/index.html', context)