from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def index (request):
    return render(request, "home/index.html")

def create_company(request):
    if request.method == 'POST':
        form = forms.CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html")
    else:
        form = forms.CompanyForm()
        context = {'form': form}
    
    return render(request, 'home/create_company.html', context)

def create_contract(request):
    if request.method == 'POST':
        form = forms.ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html")
    else:
        form = forms.ContractForm()
    context = {'form': form}
    
    return render(request, 'home/create_contract.html', context)


def create_revenue(request):
    if request.method == 'POST':
        form = forms.RevenueForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html")
    else:
        form = forms.RevenueForm()
    context = {'form': form}
    
    return render(request, 'home/create_revenue.html', context)


