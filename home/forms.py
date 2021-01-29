from django import forms

class ContactForm(forms.Form):
    """ Form for contact page - sent with emailjs """

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField()
    phone_number = forms.CharField()
    message = forms.CharField(required=True,
        widget=forms.Textarea(),
    )

    class Meta: 
        fields = [
            'name',
            'email',
            'phone_number',
            'subject',
            'message'
        ]
    
    
