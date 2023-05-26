from django import forms
from .models import Company, Contract, Revenue

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'contract_number', 'email', 'phone']
        labels = {
            'name': 'Nombre',
            'contract_number': 'Número de contrato',
            'email': 'Correo electrónico',
            'phone': 'Teléfono'
        }

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['company', 'contract_number', 'start_date', 'end_date']
        labels = {
            'company': 'Company',
            'contract_number': 'Contract Number',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }

class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ['company', 'year', 'amount']
        labels = {
            'company': 'Company',
            'year': 'Year',
            'amount': 'Amount',
        }
