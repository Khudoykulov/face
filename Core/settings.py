from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h*=9kll-r(y&g4seqi0%66^*e38042zwh8-6qtln5=avhsusb&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recognition.apps.RecognitionConfig',
    'app1.apps.App1Config',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Core.urls'

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

WSGI_APPLICATION = 'Core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 5000 * 1024 * 1024  # 50 MB


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Loyihaning asosiy katalogidagi static papkasi
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Multi-language settings

LANGUAGES = [
    ('uz', _("O'zbek")),
    ('en', _('Inglizcha')),
    ('ru', _('Ruscha')),
    # Add other languages here
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

AUTH_USER_MODEL = 'app1.User'


JAZZMIN_SETTINGS = {
    # **Asosiy sozlamalar**
    "site_title": "Davomat AI",  # Admin panelning sarlavhasi
    "site_header": "Admin Panel",  # Admin panelning yuqori qismi
    "welcome_sign": "Xush kelibsiz!",  # Admin panelining welcome xabari
    # "site_logo": "your_app/logo.png",  # Logo uchun rasm (statik faylda bo‘lishi kerak)
    # "login_logo": None,  # Kirish sahifasidagi logo (statik yo‘li)
    # "login_logo_dark": None,  # Qorong‘i rejim uchun logo

    # **Menularni sozlash**
    "site_brand": "Davomat AI",  # Sahifaning yuqori chap qismidagi brend nomi
    "search_model": "recognition.Person",  # Qidiruv oynasi uchun model
    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
        # {"model": "recognition.User"},  # Model bo‘yicha o‘tkazish
        {"app": "recognition"},  # Appga o‘tish
    ],
    "usermenu_links": [
        {"name": "Saytga o'tish", "url": "/", "new_window": True},  # Foydalanuvchi uchun yangi oyna
    ],

    # **Model ro‘yxati**
    # "hide_models": ["recognition.Person"],  # Ko‘rinmasligini xohlagan modellaringizni yashirish

    # **Tuzilgan menyular**
    "custom_links": {
        "auth": [  # App nomi (misol: `auth`)
            {"name": "Dasturchi", "url": "https://bit.ly/narzullayev", "icon": "fas fa-link", "permissions": ["auth.view_user"]},
        ],
    },

    # **UI sozlamalar**
    # "icons": {
    #     "auth": "fas fa-users-cog",  # App uchun ikonka
    #     "auth.user": "fas fa-user",  # Model uchun ikonka
    # },
    # "changeform_format": "horizontal_tabs",  # Model o‘zgarish formati: `horizontal_tabs` yoki `collapsible`

    # **Foydalanuvchi interfeysi**
    "show_sidebar": True,  # Yon menyuni ko‘rsatish
    "navigation_expanded": True,  # Yon menyu kengaygan holda ochilishi
    "hide_apps": [],  # Ko‘rinmas app'lar
    "hide_models": [],  # Ko‘rinmas modellarning ro‘yxati

    # **Footer sozlamalari**
    "copyright": "Dev Narzullayev © 2025",
    "footer_links": [
        {"name": "Qo'llab-quvvatlash", "url": "mailto:support@example.com"},
        {"name": "GitHub", "url": "https://github.com/"},
    ],

    # **Ovozalar sozlamalari**
    "related_modal_active": True,  # Modal oynalarni yoqish

    # **Qorong'i va Yorug‘lik rejimi**
    "theme": "lux",  # Bootstrap temasi (`lux`, `cyborg`, `darkly`, va hokazo)

    # **Ko'rsatish sozlamalari**
    "language_chooser": True,  # Tilni tanlash paneli
    # "order_with_respect_to": ["auth", "books", "books.author"],  # Tertibga solish

    # **Login sahifasi**
    # "custom_css": "your_app/custom.css",  # O‘z maxsus CSS faylingiz
    # "custom_js": "your_app/custom.js",  # O‘z maxsus JavaScript faylingiz
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,  # Navbar matni kichik qilish
    "body_small_text": False,  # Body matnining o‘lchami
    "brand_small_text": False,  # Brend matni kichik qilish
    "navbar_fixed": True,  # Navbarni yuqoriga qotirish
    "sidebar_fixed": True,  # Yon menyuni qotirish
    # "theme": "darkly",  # Qorong‘i rejim
    # "dark_mode_theme": "darkly",  # Qorong‘i rejim uchun mavzu
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
    },
}

# # Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.example.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'

# Django messages framework settings

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}