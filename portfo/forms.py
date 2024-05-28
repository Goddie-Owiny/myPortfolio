from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)



    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')


        if not name:
            raise forms.ValidationError('Please enter your name')
        
        if not email:
            raise forms.ValidationError('Please enter your email')
        
        if not message:
            raise forms.ValidationError('Please enter your message')

        if len(message) < 10 or len(message) > 100:
            raise forms.ValidationError('Please enter message between 10 and 100 characters')