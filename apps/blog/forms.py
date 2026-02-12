from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comparte tu opinión...'}),
        }

    def clean_body(self):
        body = self.cleaned_data['body'].strip()
        if len(body) < 10:
            raise forms.ValidationError('El comentario es demasiado corto.')
        if len(body) > 1200:
            raise forms.ValidationError('El comentario es demasiado largo.')
        return body
