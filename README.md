# Pure_butter_web
The pure butter application is a django application that allows a user to search for product substitutes using the OpenFoodFacts api.

# How do we set it up?
```
git clone https://github.com/hugoduchene/Pure_butter_web.git

Create a virtual environment :  python3 -m venv venv
Activate this virtuel environment : venv\Scripts\activate
pip install -r requirements.txt

```
For this to work you will need to install postgresql but if you already have postgresql go to myapp/Pure_butter_web/settings :

```
Change : DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': <yourdb>,
        'USER': <yourUsername>,
        'PASSWORD': <yourPassword>,
        'HOST': '',
        'PORT': '5432',
    }
}
```
