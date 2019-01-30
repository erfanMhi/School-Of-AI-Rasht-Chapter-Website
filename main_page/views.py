from django.shortcuts import render, get_object_or_404
# Create your views here.
from events.models import Event


# Create your models here.
def index(request):
    latest_event_list = Event.objects.order_by('-start_date')[:3]
    print(request.user.is_anonymous)
    print('shit')
    context = {
        'latest_event_list': latest_event_list,
        'user': request.user,
    }
    return render(request, 'main_page/index.html', context)

def not_found_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'main_page/html/404.html', context)
    


def permission_denied_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'main_page/html/403.html', context)

def server_error(request):
    context = {
        'user': request.user,
    }
    return render(request, 'main_page/html/500.html', context)