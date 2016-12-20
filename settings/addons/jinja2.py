# Full configuration in http://niwinz.github.io/django-jinja/latest/#_installation
INSTALLED_APPS += ('django_jinja',)  # NOQA

TEMPLATES += [  # NOQA
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja2",
            "app_dirname": "jinja2",
            "auto_reload": DEBUG,  # NOQA
        }
    },
]
