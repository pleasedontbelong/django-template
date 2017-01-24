# full configuration https://django-pipeline.readthedocs.io/en/latest/configuration.html

INSTALLED_APPS += ("pipeline",)  # NOQA

STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
)

# To enable with jinja2 add
#
# from django_jinja.builtins import DEFAULT_EXTENSIONS
#
# "OPTIONS": {
#     "environment": "myproject.jinja2.environment",  # (optional) if you have one
#     "extensions": DEFAULT_EXTENSIONS + ["pipeline.jinja2.PipelineExtension"]
# }
# to the jinja2 settings


PIPELINE = {
    "PIPELINE_ENABLED": True,
    "JAVASCRIPT": {
        "main": {
            "source_filenames": (
                "js/jquery.js",
            ),
            "output_filename": "js/script.js",
        }
    }
}
