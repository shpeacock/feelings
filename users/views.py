# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.

def dashboard(request):
    return render(request, 'users/dashboard.html')

class LogoutView(LoginRequiredMixin,FormView):
    form_class = forms.LogoutForm
    template_name = 'users/logout.html'

    def form_valid(self, form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))
