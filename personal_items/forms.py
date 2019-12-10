from django.forms import ModelForm, HiddenInput, TextInput, forms

from personal_items.models import PersonalThing


class PersonalThingForm(ModelForm):

    class Meta:
        model = PersonalThing
        fields = (
            'nomenclature',
            'unit',
            'quantity',
            'cost',
        )
        widgets = {
            'nomenclature': HiddenInput(),
            'unit': HiddenInput(),
            'quantity': TextInput(attrs={
                'class': 'input input_quantity',
                'placeholder': 'количество',
            }),
            'cost': TextInput(attrs={
                'class': 'input input_cost',
                'placeholder': 'стоимость',
            }),
        }