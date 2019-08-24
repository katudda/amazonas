from django import forms
from apps.catalogs.models import Comment

class CommentForm(forms.ModelForm):
    author = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Comment
        fields = ('author', 'text',)