from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import RequestFactory
import nose.tools as nt

from aliapp import views
from aliapp.models import App, UserApp


TEST_APP = {
    'name': 'test_basic',
    'description': 'Basic Description',
    'color': 'Red'
}

TEST_USER = {
    'username': 'test_user',
    'password': 'password',
    'email': 'test@test.com'
}


class TestSimple(object):
    def setup(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(**TEST_USER)

    def test_home(self):
        request = self.factory.get('/')
        request.user = self.user
        response = views.home(request)
        nt.eq_(response.status_code, 200)

    def test_modify(self):
        request = self.factory.get('/modify')
        request.user = self.user
        response = views.modify(request)
        nt.eq_(response.status_code, 302)

    def test_remove(self):
        ua = UserApp.objects.filter(user=self.user)[0]
        request = self.factory.post('/remove', {'app_id': ua.app.id})
        request.user = self.user
        response = views.remove(request)
        nt.eq_(response.status_code, 302)

    def test_modifications(self):
        request = self.factory.post('/modify', {'enabled': '1'})
        request.user = self.user
        response = views.modify(request)
        nt.eq_(response.status_code, 302)

    def test_enabled(self):
        all_apps = App.apps.all()
        user_apps = UserApp.objects.filter(user=self.user)
        enriched = views.check_enabled(all_apps, user_apps)
        for app in enriched:
            nt.ok_(hasattr(app, 'enabled'))

    def teardown(self):
        self.user.delete()
