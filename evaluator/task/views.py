from django.shortcuts import render
from django.views.generic import TemplateView


class InputView(TemplateView):
    template_name = 'input.html'


class ResultView(TemplateView):
    template_name = 'result.html'