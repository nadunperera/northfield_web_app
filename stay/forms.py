from django import forms
from .models import Stay, Tenant


class StayCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Stay
        fields = ['tenant', 'checkin', 'checkout']
        widgets = {
            'checkin': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'checkout': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        tenant_id = kwargs.pop('tenant_id', None)
        super().__init__(*args, **kwargs)
        if tenant_id:
            self.fields['tenant'].queryset = Tenant.objects.filter(id=tenant_id)
        else:
            self.fields['tenant'].queryset = Tenant.objects.filter(asset__owner=owner)

    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get('checkin')
        checkout = cleaned_data.get('checkout')
        if checkout:
            if not checkout >= checkin:
                raise forms.ValidationError('Checkout date cannot be greater than Checkin date!')
