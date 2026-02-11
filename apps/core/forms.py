from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    subject = forms.CharField(max_length=150, label='Asunto')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')
