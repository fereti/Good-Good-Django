# Подвиг 2. Объявите в программе класс формы UploadDocumentForm, не связанной с моделью, содержащей одно поле:
# doc_upload: загрузка произвольных файлов (FileField), обязательное, название "Выберите документ


from django import forms


class UploadDocumentForm(forms.Form):
    doc_upload = forms.FileField(label="Выберите документ")
