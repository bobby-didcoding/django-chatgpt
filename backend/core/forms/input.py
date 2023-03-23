# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms


class InputForm(forms.Form):
    '''
    Basic form for our animal name suggestion form and logo generator form
    '''

    input = forms.CharField(max_length=100, required=True,
      widget=forms.TextInput(attrs={
        'placeholder': 'Give me something to work on...'}))

    class Meta:
        fields = ('input',)