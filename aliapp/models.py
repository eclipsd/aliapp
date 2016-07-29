from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class DefaultAppManager(models.Manager):
    def get_queryset(self):
        return super(DefaultAppManager, self).get_queryset().filter(default_status=True)


class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=25)
    default_status = models.BooleanField(default=False)
    icon = models.CharField(max_length=50)
    apps = models.Manager()
    default_apps = DefaultAppManager()

    def __str__(self):
        return 'App // {} // {}'.format(self.id, self.name)


class UserApp(models.Model):
    app = models.ForeignKey(App)
    user = models.ForeignKey(User)

    def __str__(self):
        return 'UserApp // {} // {} to {}'.format(self.id, self.app.name, self.user.username)


@receiver(post_save, sender=User)
def add_default_apps(sender, instance, created, *args, **kwargs):
    if not created:
        return False
    default_apps = App.default_apps.all()
    for app in default_apps:
        user_app = UserApp(app=app, user=instance)
        user_app.save()
    return True
