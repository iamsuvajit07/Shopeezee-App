from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from shop.models import Customer


class MyRegForm(UserCreationForm):
    username = forms.CharField(
        label="Enter user name*",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )
    first_name = forms.CharField(
        label="Enter first name*",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )
    last_name = forms.CharField(
        label="Enter last name*",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )
    email = forms.CharField(
        label="Enter email-id*",
        widget=forms.EmailInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )
    mobile_number = forms.CharField(
        label="Enter mobile no.*",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )
    address_line1 = forms.CharField(
        label="Enter your address",
        widget=forms.Textarea(
            attrs={
                "class": "block w-full rounded-md resize-none border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )
    password1 = forms.CharField(
        label="Enter your password*",
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded-md  border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    class Meta:
        model = Customer
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "address_line1",
        ]


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Enter username",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )
    password = forms.CharField(
        label="Enter your password",
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )


class MyprofileForm(UserChangeForm):
    password = None

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    email = forms.CharField(
        label="Email-id",
        widget=forms.EmailInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    mobile_number = forms.CharField(
        label="Mobile no.",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )
    address_line1 = forms.CharField(
        label="Address",
        widget=forms.Textarea(
            attrs={
                "class": "block w-full rounded-md resize-none border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "address_line1",
        ]


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Enter your old password",
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    new_password1 = forms.CharField(
        label="Enter your new password",
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    new_password2 = forms.CharField(
        label="Confirm your password",
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded-md border-2 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600"
            }
        ),
    )

    class Meta:
        model = Customer
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]