from django import forms
from office import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.CompanyCategory
        fields = '__all__'
        exclude = ['EmpEntered']
        labels = {
            'name': 'اسم القطاع'
        }


class ResearchCompanyForm(forms.ModelForm):
    class Meta:
        model = models.ResearchCompany
        fields = '__all__'
        exclude = ['EmpEntered']
        labels = {
            'name': 'اسم الشركة'
        }


class CompanyCodeForm(forms.ModelForm):
    class Meta:
        model = models.CompanyCode
        fields = '__all__'
        labels = {
            'code': 'كود الشركة',
            'company': 'إختر الشركة'
        }


class RateForm(forms.ModelForm):
    class Meta:
        model = models.Rates
        fields = '__all__'
        exclude = ['EmpEntered', ]
        widgets = {
            'RecommendDate': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'id': 'RecommendDate', 'type': 'date', 'class': 'form-control',
                       'placeholder': ' تاريخ التوصية '}),
        }
        labels = {
            'ResearchCompany': 'شركة الأبحاث',
            'report': 'التقرير',
            'FairValue': 'القيمة العادلة',
            'AnalayticName': 'المحلل',
            'RecommendDate': 'تاريخ التوصية',
            'CompanyEntered': ' الشركة المدرجة',
            'MarketValue': ' السعر السوقى',
            'Recommendation': 'التوصية',
            'CurrenncyValue': 'السعر وقت التوصية',
            'is_recommended': 'مرشحة للقارئ',
            'changeFair': 'هل تاثرت القيمة العادلة؟',
            'changeMarket': 'هل تاثرت القيمة السوقية؟',

        }


class AnalystForm(forms.ModelForm):
    class Meta:
        model = models.FinicialAnalyst
        fields = '__all__'
        exclude = ('EmpEntered',)
        labels = {
            'email': 'البريد الألكترونى',
            'name': 'الأسم',
            'currentCompany': 'الشركة الحالية',
            'logo': 'الصورة',
            'tiwtterAccount': 'حساب تويتر',
            'CurrentJob': 'الوظيفة الحالية',
            'phone': 'الهاتف'
        }


class FinicalCompanyForm(forms.ModelForm):
    class Meta:
        model = models.FinicialCompany
        fields = '__all__'
        exclude = ('EmpEntered',)
        labels = {
            'name': 'اسم الشركة المدرجة',
            'category': 'القطاع ',
            'logo': 'الشعار',
            'link': 'الرابط',
            'total_arrows': 'إجمالى عدد الأسهم',
            'arrow_value': 'سعر السهم',

        }


class ExpectationForm(forms.ModelForm):
    class Meta:
        model = models.EarningsForecast
        fields = '__all__'
        exclude = ('EmpEntered',)
        labels = {
            'CompanyEntered': 'الشركة المدرجة',
            'ResearchCompany': 'شركة الأبحاث ',
            'analyst': 'إسم المحلل',
            'total_earn': 'توقعات الأرباح',
            'third2020': 'الربع الثالث 2020',
            'second2020': 'الربع الثانى 2021',
            'realEarn': 'الأرباح الفعلية',
            'report': ' التقرير',
            'is_recommended':'مرشح للقارئ'
        }
