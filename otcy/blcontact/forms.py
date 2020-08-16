from django import forms


class ContactForm(forms.Form):
    Title = forms.CharField(max_length=10)
    your_name = forms.CharField(label='Your name', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=25)
    last_name = forms.CharField(label='Last Name', max_length=25)
    tel = forms.CharField(max_length=15)
    whatsapp = forms.CharField(label='Whatsapp No.',max_length=15)
    country = forms.CharField(max_length=15)
    note = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
