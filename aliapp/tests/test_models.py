import nose.tools as nt
from django.contrib.auth.models import User

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


class TestApp(object):
    def setup(self):
        self.app = App(**TEST_APP)
        self.app.save()

    def test_str(self):
        expected = 'App // {} // {}'.format(self.app.id, self.app.name)
        nt.eq_(str(self.app), expected)

    def test_name(self):
        nt.eq_(self.app.name, 'test_basic')


class TestUserApp(object):
    def setup(self):
        self.app = App(**TEST_APP)
        self.app.save()
        self.user = User.objects.create_user(**TEST_USER)
        self.ua = UserApp(app=self.app, user=self.user)
        self.ua.save()

    def test_str(self):
        expected = 'UserApp // {} // {} to {}'.format(self.ua.id, self.app.name,
                                                      self.user.username)
        nt.eq_(str(self.ua), expected)

    def teardown(self):
        self.user.delete()
        self.ua.delete()


class TestDefaultUserApps(object):
    def setup(self):
        self.app = App(**TEST_APP)
        self.app.save()
        self.user = User.objects.create_user(**TEST_USER)

    def test_apps(self):
        ua = UserApp.objects.filter(user=self.user)
        nt.eq_(len(ua), 2)

    def teardown(self):
        self.user.delete()


class TestOmitUpdate(object):
    def setup(self):
        self.user = User.objects.create_user(**TEST_USER)

    def test_update(self):
        before = UserApp.objects.all()
        self.user.first_name = 'Test'
        self.user.save()
        after = UserApp.objects.all()
        nt.eq_(len(before), len(after))

    def teardown(self):
        self.user.delete()
