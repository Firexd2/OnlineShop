from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from Authentication.validator import validate_email_on_unique


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200,
                             help_text='Будет отправлено письмо для подтверждения почты',
                             validators=[validate_email_on_unique])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('Ваш профиль не активирован. Пожалуйста, проверьте вашу почту!')



