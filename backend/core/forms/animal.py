# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms


class AnimalForm(forms.Form):
    '''
    Basic form for our animal name suggestion form
    '''

    breed = forms.CharField(max_length=100, required=True,
      widget=forms.TextInput(attrs={
        'placeholder': 'Enter breed of animal'}))

    class Meta:
        fields = ('breed',)