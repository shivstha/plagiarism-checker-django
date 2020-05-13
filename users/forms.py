from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = {'email', 'username', 'first_name', 'last_name', }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = {'email', 'username', 'first_name', 'last_name',  }


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        firstname_widget = forms.TextInput(attrs={'type': 'text',
                                              'placeholder':
                                                  _('First name'),})

        lastname_widget = forms.TextInput(attrs={'type': 'text',
                                                  'placeholder':
                                                      _('Last name'),})

        self.fields['first_name'] = forms.CharField(required=True, label=_("First name"),
                                                    widget=firstname_widget)
        self.fields['last_name'] = forms.CharField(required=True, label=_("Last name"),
                                                   widget=lastname_widget)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.

        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user



