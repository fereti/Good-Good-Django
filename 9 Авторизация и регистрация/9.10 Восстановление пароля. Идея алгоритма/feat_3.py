# Подвиг 3. С помощью стандартной функции send_mail() фреймворка Django:
#
# from django.core.mail import send_mail
# выполните отправку следующего сообщения:
#
# E-mail отправителя: balakirev@sitewomen.ru;
# список E-mail получателей: sergey@supermail.com
# тема письма: "Django 4";
# текст письма: "Спасибо Django, что ты есть!";
# В программе нужно только вызвать функцию send_mail() для отправки указанного письма, больше ничего.


from django.core.mail import send_mail

send_mail(
    "Django 4",
    "Спасибо Django, что ты есть!",
    "balakirev@sitewomen.ru",
    ["sergey@supermail.com"],
)
