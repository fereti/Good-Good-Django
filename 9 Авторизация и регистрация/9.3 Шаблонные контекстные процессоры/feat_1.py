# Подвиг 1. Пусть в файле settings.py параметр TEMPLATES определен следующим образом:
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'profile.context_processors.default_data',
#             ],
#         },
#     },
# ]
# Необходимо в файле profile/context_processors.py определить контекстный процессор default_data для передачи в шаблоны следующих переменных:
#
# default_avatar: 'profile/default_avatar.jpg';
# default_auth: 'username/password'.
# P.S. На экран ничего выводить не нужно.


# ------------------- settings.py ---------------------
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
                'profile.context_processors.default_data',
            ],
        },
    },
]


# ------------------- profile/context_processors.py ---------------------
# from django.shortcuts import render

def default_data(request):
    return {
        'default_avatar': 'profile/default_avatar.jpg',
        'default_auth': 'username/password'
    }
