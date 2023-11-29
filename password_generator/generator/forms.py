from django import forms
from django.core.exceptions import ValidationError

class PasswordGeneratorForm(forms.Form):
  length = forms.CharField(label="Enter the total length of the password", required=True)
  uppercase = forms.CharField(label="Enter the number of Alphabets", required=True)
  special = forms.CharField(label="Enter the number of Numbers", required=True)
  numbers = forms.CharField(label="Enter the number of Special characters", required=True)

  def clean(self):
    cleaned_data = super().clean()
    length = cleaned_data.get('length')
    uppercase = cleaned_data.get('uppercase')
    special = cleaned_data.get('special')
    numbers = cleaned_data.get('numbers')

    if any(v == '' for v in [length, uppercase, special, numbers]):
      raise ValidationError('Please fill in all the fields.')
    else:
      try:
        length = int(length)
        uppercase = int(uppercase)
        special = int(special)
        numbers = int(numbers)
      except ValueError:
        raise ValidationError('Please enter only numeric values.')