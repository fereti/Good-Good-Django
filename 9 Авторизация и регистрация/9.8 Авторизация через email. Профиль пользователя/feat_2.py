# Подвиг 2. Пусть в файле users/authentication.py приложения users объявлен следующий класс аутентификации через ВКонтакте:
#
# # -------------- authentication.py -----------------------
# from django.contrib.auth.backends import BaseBackend
#
# class VKAuthBackend(BaseBackend):
#     "Бэкенд авторизации через ВК"
#
# # -------------- settings.py -----------------------
#
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
# ]
# Добавьте в список AUTHENTICATION_BACKENDS бэкенд VKAuthBackend так, чтобы он использовался в первую очередь.


# -------------- authentication.py -----------------------
# from django.contrib.auth.backends import BaseBackend

class VKAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None


# -------------- settings.py -----------------------

AUTHENTICATION_BACKENDS = [
    'users.authentication.VKAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]
