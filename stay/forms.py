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
        super().__init__(*args, **kwargs)
        self.fields['tenant'].queryset = Tenant.objects.filter(asset__owner=owner)
