from django import forms
from datetime import date


class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Имя автора")
    last_name = forms.CharField(label="Фамилия автора")
    date_of_birth = forms.DateField(label="Дата рождения",
                                    initial=format(date.today()), # Чтобы даты при первой загрузке имели значение
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'})) # этот виджет -  календарь, в котором можно выбрать нужную дату
    date_of_death = forms.DateField(label="Дата смерти",
                                    initial=format(date.today()), # Чтобы даты при первой загрузке имели значение
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'})) # этот виджет - календарь, в котором можно выбрать нужную дату

# Все, что необходимо сделать внутри создаваeмого класса, - это добавить класс Meta и связать его с моделью. А затем в поле
# fields указать доля модели данных, которые необходимо включить в форму.
# ПРИМЕР :
from django.forms import ModelForm
from .models import Book

class BookModelForm(ModelForm):
    class Meta:
        model = Book
      # fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']
# В качестве примера приведем синтаксис кода, который мы могли бы использовать
# для изменения параметров поля для ввода аннотации к книге
        fields = ['summary', ]
        labels = {'summary': ('Аннотация'), }
        help_texts = {'summary': ('Не более 1000 символов'), }








