# full configuration https://django-pipeline.readthedocs.io/en/latest/configuration.html

INSTALLED_APPS += [
    'pipeline',
]

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# To enable with jinja2 add
# 'OPTIONS': {
#     'environment': 'myproject.jinja2.environment',
#     'extensions': ['pipeline.jinja2.PipelineExtension']
# }
# to the jinja2 env


PIPELINE = {
    'PIPELINE_ENABLED': True,
    'JAVASCRIPT': {
        'main': {
            'source_filenames': (
                'js/jquery.js',
            ),
            'output_filename': 'js/script.js',
        }
    }
}
