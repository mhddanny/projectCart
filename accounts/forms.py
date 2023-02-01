from django import forms
from . models import Account

class RegisterForm(forms.ModelForm):
    # first_name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         "class": "form-control",
    #         "placeholder": "First Name",
    #         }
    #     ))
    # last_name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class' :'form-control',
    #         'placeholder': 'Last Name',
    #     }
    # ))
    # email = forms.EmailField(widget=forms.EmailInput(
    #     attrs={
    #         'class' :'form-control',
    #         'placeholder': 'Enter Password',
    #         "unique":True,
    #     }
    # ))
    # phone_number = forms.CharField(widget=forms.NumberInput(
    #     attrs={
    #         'class' :'form-control',
    #         'placeholder': 'Phone Number',
    #     }
    # ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' :'form-control',
            'placeholder': 'Enter Password'
        }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' :'form-control',
            'placeholder': 'Confirm Password'
        }
    ))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match.!"
            )

    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'