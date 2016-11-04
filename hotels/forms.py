from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    sujet = forms.CharField(max_length=250)
    message = forms.CharField(max_length=512, widget=forms.Textarea)