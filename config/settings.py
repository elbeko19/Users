from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # local
    'users_app',
    
    # pip
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




JAZZMIN_SETTINGS = {
    "site_title": "USERS    ",
    "site_header": "Users",
    "site_brand": "Elbek",
    "order_with_respect_to": [
        "auth",
        "about",
        "about.workersmodel",
        "about.tradeunion",
        "about.about",
        "about.Statistics",
        "executive",
        "council",
        "post",
        "gallery",
        "doc",
        "doc.doccategory",
        "normative_doc",
        "vacancy",
        "affiliates",
        "teritory_division",
        "virtual_reception",
        "feedback",
        "information",
        "useful_link",
        "faq",
    ],
    "icons": {
        "auth.Group": "fas fa-user-friends",
        "auth.User": "fas fa-users",
        "about.WorkersModel": "fas fa-user-tie",
        "about.TradeUnion": "fas fa-user-tie",
        "about.About": "fas fa-info-circle",
        "about.Statistics": "fas fa-chart-pie",
        "affiliates.affiliates": "fas fa-people-arrows",
        "council.council": "fas fa-user-shield",
        "council.categorycouncil": "fas fa-align-justify",
        "doc.doc": "fas fa-file-alt",
        "doc.doccategory": "fas fa-align-justify",
        "executive.ExecutiveApparatus": "fas fa-user-tie",
        "faq.faq": "fas fa-question",
        "feedback.feedback": "fas fa-phone",
        "gallery.photogallery": "fas fa-images",
        "gallery.videogallery": "fas fa-video",
        "information.InfoCategory": "fas fa-align-justify",
        "information.executiveapparatusinformation": "fas fa-phone-volume",
        "normative_doc.NormativeDocCategory": "fas fa-align-justify",
        "normative_doc.NormativeDocument": "fas fa-print",
        "post.category": "fas fa-align-justify",
        "post.postmodel": "fas fa-newspaper",
        "teritory_division.TerritoryDivision": "fas fa-map-marked-alt",
        "useful_link.usefullink": "fas fa-handshake",
        "vacancy.vacancy": "fas fa-user-plus",
        "virtual_reception.VirtualReception": "fas fa-envelope",
    }
}