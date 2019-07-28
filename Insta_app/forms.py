from django import forms

class NewImageForm(forms.ModelForm):
  class Meta:
    model =Image
    exclude = ['user','likes','comments']