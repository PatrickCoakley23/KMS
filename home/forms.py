from django import forms

class ContactForm(forms.Form):
    """ Form for contact page - sent with emailjs """

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField()
    phone_number = forms.CharField(required=False)
    message = forms.CharField(required=True,
        widget=forms.Textarea(),
    )
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'subject': 'Subject',
            'message': 'Enter Message',
        }

        label = {
            'name': 'Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'subject': 'Subject',
            'message': 'Message',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

