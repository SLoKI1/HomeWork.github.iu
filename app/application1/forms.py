from .models import TEACHER, HEADMAN
from django.forms import ModelForm, TextInput ,Textarea, DateInput
import datetime

DTUTC = datetime.date.today()
class HEADMANForm(ModelForm):
    class Meta:
        model = HEADMAN
        fields = ['Hrealy','Hitem','Hexercise','Hdata']

        widgets = {
            'Hrealy': DateInput(attrs={
                'type': 'date',
                'placeholder': 'действительность ',
                'class': 'form-control w-25 p-2'
            }),
            'Hitem': TextInput(attrs={
                'placeholder': 'Предмет ',
                'class': 'form-control w-25 p-2'
            }),
            'Hexercise': Textarea(attrs={
                'placeholder': 'Задание ',
                'class': 'form-control w-25 p-2'
            }),
            'Hdata': TextInput(attrs={
                'value': DTUTC,
                'class': 'form-control w-25 p-2 d-none'
            })

        }


class TEACHERForm(ModelForm):
    class Meta:
        model = TEACHER
        fields = ['Trealy','Tmessage','Tdata']

        widgets = {
            'Trealy': DateInput(attrs={
                'type': 'date',
                'placeholder': 'действительность ',
                'class': 'form-control w-25 p-2 '
            }),
            'Tmessage': Textarea(attrs={
                'placeholder': 'Задание ',
                'class': 'form-control w-25 p-2 '
            }),
            'Tdata': TextInput(attrs={
                'value': DTUTC,
                'class': 'form-control w-25 p-2 d-none'
            })

        }