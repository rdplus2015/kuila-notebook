from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# Form for user sign-up
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Email field required for user sign-up

    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ('email', 'password1', 'password2')  # Fields to include in the form

    def save(self, commit=True):
        # Save the user instance with the provided email
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()  # Save the user to the database
        return user

# Form for updating user information
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ('email', )  # Fields to include in the form for updating
