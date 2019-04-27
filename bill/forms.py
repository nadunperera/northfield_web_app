from django import forms
from .models import Bill, Service


class BillCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ['service', 'name', 'bill_from', 'bill_to', 'discount', 'discount_end']
        widgets = {
            'bill_from': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'bill_to': forms.DateTimeInput(attrs={'class': 'datetime-input'}),

        }

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(asset__owner=owner)
