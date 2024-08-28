from django import forms
from .models import ModelTest

class MonFormulaire(forms.Form):
    champ_form = forms.CharField(max_length=128)

class MonFormulaireModelTest(forms.ModelForm):
    class Meta:
        model=ModelTest
        fields = "__all__"
        #fields=['mon_champ']