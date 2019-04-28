from django import forms
from .models import Bill, Service


class BillCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ['service', 'name', 'bill_from', 'bill_to', 'discount', 'discount_end']
        widgets = {
            'bill_from': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'bill_to': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'discount_end': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        service_id = kwargs.pop('service_id', None)
        super().__init__(*args, **kwargs)
        if service_id:
            self.fields['service'].queryset = Service.objects.filter(id=service_id)
        else:
            self.fields['service'].queryset = Service.objects.filter(asset__owner=owner)

    def clean(self):
        cleaned_data = super().clean()
        bill_from = cleaned_data.get('bill_from')
        bill_to = cleaned_data.get('bill_to')

        if not bill_to >= bill_from:
            raise forms.ValidationError('Bill-to date cannot be greater than Bill-from date!')
