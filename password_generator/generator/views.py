from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import PasswordGeneratorForm
import random



def generator(request):
  form = PasswordGeneratorForm(request.POST or None)
  password = ''

  if form.is_valid():
    try:
      length = int(form.cleaned_data.get('length', '12'))
      no_alphabets = int(form.cleaned_data.get('uppercase', '0'))
      no_numbers = int(form.cleaned_data.get('special', '0'))
      no_symbols = int(form.cleaned_data.get('numbers', '0'))
    except ValueError:
      form.add_error(None, 'Please enter only numeric values.')
      return render(request, 'generator.html', {'form': form, 'password': password})

    # Check the sum of the number of alphabets, numbers, and special characters is less than or equal to the total length of the password.
    if no_alphabets + no_numbers + no_symbols > length:
      form.add_error(None, 'The total length is less than the sum of alphabets, numbers, and symbols. Please try again.')
    else:
      password_list = []
      no_lowercase = no_alphabets // 2
      no_uppercase = no_alphabets - no_lowercase

      # fill the random selection of Characters
      password_list += [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(no_lowercase)]
      password_list += [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(no_uppercase)]
      password_list += [random.choice('!@#$%^&*()?') for _ in range(no_symbols)]
      password_list += [random.choice('0123456789') for _ in range(no_numbers)]

      # Fill the rest of the password length with lowercase letters
      password_list += [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length - len(password_list))]

      random.shuffle(password_list)
      password = ''.join(password_list)

      form = PasswordGeneratorForm()    

  return render(request, 'generator.html', {'form': form, 'password': password})