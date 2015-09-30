from django import forms
from django.forms import ModelForm, Form
from finance.models import Transaction
from household.models import Inhabitant


class TransactionForm(Form):
    description = forms.CharField()
    date = forms.DateField()
    amount = forms.DecimalField()
    paid_by = forms.ModelChoiceField(queryset=Inhabitant.objects.all())
    paid_for = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              queryset=Inhabitant.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['paid_by'].queryset = Inhabitant.objects.filter(household=user.inhabitant.household)
        self.fields['paid_for'].queryset = Inhabitant.objects.filter(household=user.inhabitant.household)
