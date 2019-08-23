from django.shortcuts import render


def main(request):
  template = 'index.pug'
  return render(request, template, {})

