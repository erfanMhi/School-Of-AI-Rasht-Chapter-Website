import json


from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.core.exceptions import PermissionDenied
from django.utils import timezone

# Create your views here.
from events.models import Event
from .models import Profile, UserRegistration
from events.models import Lecturer, Category, Event, Lecture
from django.contrib.auth.models import User
from dateutil.parser import parse
# Create your views here.

def register_validation(user_json):
    if 'username' in user_json and \
        'password' in user_json and \
        'fullname' in user_json and \
        'email' in user_json:
        return True
    return False

def signup_user(request):
    print('signup now') 
    # try:
    if request.method == 'POST':
        print('Raw Data: "%s"' % json.loads(request.body))
        user_json = json.loads(request.body)
        if register_validation(user_json):
            if ' ' in user_json['fullname']:
                first_name, last_name = user_json['fullname'].split(' ', 1)
            else:
                first_name = user_json['fullname']
                last_name = ''
            
            user = User.objects.create_user(username=user_json['username'],
                                            email=user_json['email'],
                                            password=user_json['password'],
                                            first_name=first_name, last_name=last_name)
            return HttpResponse("OK")
    # except Exception:
    #     pass

    return HttpResponseForbidden()


def login_user(request):
    print('login_user')
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'main_page/index.html', {})
@login_required
def logout_user(request):
    pass


@login_required
def profile(request):
    print('request.user', request.user)
    user = request.user
    print(request.method)
    if request.method == 'POST':
        print('Raw Data: "%s"' % json.loads(request.body))

        user_json = json.loads(request.body)
        print('birthdate', user_json['birthdate'])
        print('birthdate', parse(user_json['birthdate']))
        if True:
            if ' ' in user_json['fullname']:
                user.first_name, user.last_name = user_json['fullname'].split(' ', 1)
            else:
                user.first_name = user_json['fullname']
                user.last_name = ''
            if 'email' in user_json:
                user.email = user_json['email']
            if 'province' in user_json:
                user.profile.province = user_json['province']
            if 'city' in user_json:
                user.profile.city = user_json['city']
            if 'mobile' in user_json:
                user.profile.mobile = user_json['mobile']
            if 'birthdate' in user_json:
                user.profile.birthdate = parse(user_json['birthdate'])
            user.save()
            return HttpResponse("OK")
    # myDate.strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def profile_photo(request):
    print("profile_photo")
    user = request.user
    print(request.method)
    if request.method == 'POST':
        if True:
            user.profile.photo_url = request.FILES['file']
            user.save()
            return JsonResponse({'photo_url': user.profile.photo_url.url})
    return HttpResponseForbidden()

def validate_event(event_attr, event_files):
    return True

@login_required
def create_event(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            res = request.POST
            files = request.FILES
            if validate_event(res, files):
                categories = []
                for category in res['categories'].split():
                    category_object = Category.objects.filter(name = category)
                    if category_object.count():
                        categories.append(category_object.first())
                    else:
                        categories.append(Category(name=category))
            
                event = Event(title=res['title'], start_date=parse(res['start_date']), 
                                finish_date=parse(res['finish_date']), organizer=res['organizer'], 
                                place=res['place'], cover_url=files['cover_url'],
                                logo_url=files['logo_url'], description=res['description'])
                print(files)
                print(res)
                print("files['lecturer_photo']",files['lecturer_photo'])
                lecturer = Lecturer(name=res['name'], resume_url=files['resume_url'],
                                        photo_url=files['lecturer_photo'])

                lecture = Lecture(title=res['lecture_title'])
                event.save()
                lecturer.save()
                lecture.lecturer = lecturer
                lecture.event = event
                lecture.save()
                for category in categories:
                    category.save()
                    event.categories.add(category)
                return render(request, 'users/create_event.html', {'user': request.user, 'succeed': True})
            else:
                return render(request, 'users/create_event.html', {'user': request.user, 'not_valid': True})
        else:
            return render(request, 'users/create_event.html', {'user': request.user})
    else:
        raise PermissionDenied

        

@login_required
def notifications(request):
    user = request.user
    if user.is_staff:
        user_requests = UserRegistration.objects.filter(user=request.user.profile)
        return render(request, 'users/notifications.html', {'user': request.user, 'user_requests': user_requests})
    else:
        raise PermissionDenied

@login_required
def join_requests(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            data = json.loads(request.body)
            event_request = UserRegistration.objects.get(pk=int(data['request_id']))
            print(event_request)
            if data['reg_status'] == 'd':
                event_request.reg_status = 'd'
                event_request.save()
                return HttpResponse("OK")
            elif data['reg_status'] == 'a':
                event_request.reg_status = 'a'
                event_request.save()
                return HttpResponse("OK")
            return  Http404()  
            
        else:
            user_requests = UserRegistration.objects.filter(reg_status='r')
            return render(request, 'users/join_requests.html', {'user': request.user, 'user_requests': user_requests})
    else:
        raise PermissionDenied
        
@login_required
def lecture_request(request):
    user = request.user
    if user.is_staff:
        return render(request, 'users/lecture_requests.html', {'user': request.user})
    else:
        raise PermissionDenied

@login_required
def event_sign_up(request):

    print(request.method)
    if request.method == 'POST':
        event =  Event.objects.get(pk=int(json.loads(request.body)['event_id']))
        if True:
            if not UserRegistration.objects.filter(event=event, user=request.user.profile).count():
                UserRegistration(user=request.user.profile, event=event, reg_status='r', date_joined=timezone.now()).save()
            print("hello")
            # UserRegistration(user=request.user.profile, event=event, reg_status='r').save()
            # user.save()
            return HttpResponse("OK")
    # myDate.strftime("%Y-%m-%d %H:%M:%S")
    return Http404()


@login_required
def event_management(request):
    
    if request.user.is_staff:
        if request.method == 'POST':
            data = json.loads(request.body)
            event = Event.objects.get(pk=int(data['event_id']))
            if data['decision'] == 'remove':
                event.delete()
            return HttpResponse("OK")
        else:
            events =  Event.objects.all()
            return render(request, 'users/events_management.html', {'user': request.user, 'events': events})
    raise PermissionDenied

@login_required
def event_update(request, event_id):
        if request.user.is_staff:
            if request.method == 'POST':
                res = request.POST
                files = request.FILES
                if validate_event(res, files):
                    print(files)
                    print(res)
                    print("files['lecturer_photo']",files['lecturer_photo'])
                    categories = []
                    for category in res['categories'].split():
                        category_object = Category.objects.filter(name = category)
                        if category_object.count():
                            categories.append(category_object.first())
                        else:
                            categories.append(Category(name=category))
                    event = get_object_or_404(Event, pk=event_id)
                    event.title=res['title']; event.start_date=parse(res['start_date'])
                    event.finish_date=parse(res['finish_date']); event.organizer=res['organizer']
                    event.place=res['place']; event.cover_url=files['cover_url']
                    event.logo_url=files['logo_url']; description=res['description']
                    lecture = event.lecture_set.all()[0]
                    lecture.title = res['lecture_title']
                    print(lecture.lecturer)
                    print(lecture.lecturer.photo_url)
                    lecture.lecturer.name = res['name']
                    lecture.lecturer.resume_url = files['resume_url']
                    lecture.lecturer.photo_url = files['lecturer_photo']
                    event.save()
                    lecture.save()
                    lecture.lecturer.save()

                    for category in categories:
                        category.save()
                        print(category)
                        print(Category.objects.filter(name=category.name))
                        if not Category.objects.filter(name=category.name).count():
                            event.categories.add(category)
                    return render(request, 'users/update_event.html', {'user': request.user, 'succeed': True,
                                                                        'event': event, 'finish_date': res['finish_date'],
                                                                        'categories': categories, 'lecture': lecture,
                                                                        'start_date':res['start_date']})
            else:
                event = get_object_or_404(Event, pk=event_id)
                categories = [category.name for category in event.categories.all()]
                lecture = event.lecture_set.all()[0]
                start_date = event.start_date.strftime('%Y-%m-%dT%H:%M')
                finish_date = event.finish_date.strftime('%Y-%m-%dT%H:%M')
                return render(request, 'users/update_event.html', {'user': request.user, 'event': event,
                                                                     'categories': categories, 'lecture': lecture,
                                                                     'start_date': start_date, 'finish_date': finish_date })
        raise PermissionDenied