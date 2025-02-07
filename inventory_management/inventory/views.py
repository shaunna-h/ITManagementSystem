from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from.models import InventoryItem

# Basic homepage
class Index (TemplateView):
    template_name = 'inventory/index.html'

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')
        return render(request, 'inventory/dashboard.html', {'items' : items})

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form' : form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('index')
        
        return render(request, 'inventory/signup.html', {'form' : form})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'inventory/logout.html', {})