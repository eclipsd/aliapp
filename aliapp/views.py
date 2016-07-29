from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import App, UserApp


def check_enabled(all_apps, enabled_apps):
    enabled_app_ids = [app.app.id for app in enabled_apps]
    for app in all_apps:
        app.enabled = False
        if app.id in enabled_app_ids:
            app.enabled = True
    return all_apps


@login_required
def home(request):
    enabled_apps = UserApp.objects.filter(user=request.user)
    all_apps = check_enabled(App.apps.all(), enabled_apps)
    context = {
        'all_apps': all_apps,
        'enabled_apps': enabled_apps
    }
    return render(request, 'home.html', context)


@login_required
def modify(request):
    UserApp.objects.filter(user=request.user).delete()
    for app_id in request.POST.getlist('enabled'):
        app = App.apps.get(id=app_id)
        ua = UserApp(app=app, user=request.user)
        ua.save()
    return redirect('home')


@login_required
def remove(request):
    UserApp.objects.get(id=request.POST['app_id']).delete()
    return redirect('home')
