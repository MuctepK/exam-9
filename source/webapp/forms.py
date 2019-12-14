from webapp.models import Photo
from django import forms


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['img', 'signature']


class CommentForm(forms.Form):
    text = forms.CharField(max_length=1024, widget=forms.Textarea)