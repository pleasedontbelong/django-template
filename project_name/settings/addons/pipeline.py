# full configuration https://django-pipeline.readthedocs.io/en/latest/configuration.html

INSTALLED_APPS += ("pipeline",)  # NOQA

STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
)

PIPELINE = {
    "PIPELINE_ENABLED": True,
    "JAVASCRIPT": {
        "main": {
            "source_filenames": (
                "js/jquery.js",
            ),
            "output_filename": "js/script.js",
        }
    },
    'CSS_COMPRESSOR': None,
    'JS_COMPRESSOR': None,
}
