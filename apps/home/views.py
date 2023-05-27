from django.shortcuts import render, redirect
from . import forms
from django.db.models import Sum
from .models import Company, Revenue, NPT



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

def create_npt(request):
    if request.method == 'POST':
        form = forms.NPTForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html")
    else:
        form = forms.NPTForm()
    context = {'form': form}

    return render(request, 'home/create_npt.html', context)



# def index(request):
#     companies = Company.objects.all()
#     revenue_list = Revenue.objects.values('company__name', 'amount', 'year')
#     total_revenue = Revenue.objects.aggregate(Sum('amount'))['amount__sum']
#     total_npt = NPT.objects.aggregate(total=Sum('cantidad_npt'))['total']
#     return render(request, 'home/index.html', {'companies': companies, 'revenue_list': revenue_list, 'total_revenue': total_revenue, 'total_npt': total_npt})


def index(request):
    companies = Company.objects.all()
    total_npt = NPT.objects.aggregate(total=Sum('cantidad_npt'))['total']
    total_revenue = Revenue.objects.aggregate(Sum('amount'))['amount__sum']

    for company in companies:
        revenue_list = Revenue.objects.filter(company=company).order_by('-amount').values('year', 'amount')
        company.revenue_list = revenue_list
        company.total_revenue = Revenue.objects.filter(company=company).aggregate(Sum('amount'))['amount__sum']
        company.year_npt_totals = NPT.objects.filter(company=company).values('year').annotate(total_npt=Sum('cantidad_npt'))

    return render(request, 'home/index.html', {'companies': companies, 'total_npt': total_npt, 'total_revenue': total_revenue})

