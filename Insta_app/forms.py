from django import forms
from .models import Image, Comments
class SubscribeForm(forms.Form):
   name = forms.CharField(label='First Name', max_length=30)
   email = forms.EmailField(label = 'Email')
class NewProfileForm(forms.ModelForm):
   class Meta:
       model = Image
       exclude = ['poster', 'post_date']
       widgets = {
           'tags': forms.CheckboxSelectMultiple(),
       }
class NewCommentForm(forms.ModelForm):
   class Meta:
       model = Comments
       fields = ('comment',)