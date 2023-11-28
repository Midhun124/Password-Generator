from django.shortcuts import render
from django.http import HttpResponse


def generator(request):
  return HttpResponse("password generator")