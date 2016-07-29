# aliapp
## **Ali**ce's **App**s
A Django project for simple display and retrieval of apps on a per-user basis.

### Getting Started
Regardless of environment, you'll want to set up a few basic dependencies:
* Python 2.7 (with `requirements.txt` installed)
* Postgres

#### Migrations
To seed the database with the test users and apps requested, run the migrations.

```bash
python manage.py migrate
```

#### Run the tests
The tests included use `nose` as the test runner via `django-nose`. To run the tests included:

```bash
python manage.py test
```

### Environments
While the app is built to be run anywhere, two configurations are present for Production (Heroku) and local development.

#### Production
The app is deployed to [Heroku](https://glbrc.herokuapp.com) and includes a Procfile and integration with WhiteNoise for static assets.

To run the app in production mode, use `heroku local web`.

#### Development
To run in development mode, prefix the typical `runserver` command with the `ALIAPP_ENV` environment variable.

```bash
ALIAPP_ENV=dev python manage.py runserver
