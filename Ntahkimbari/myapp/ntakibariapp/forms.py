from django.contrib.auth.forms import UserCreationForm
from .models import Member
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

class SignupForm(UserCreationForm): 

	types = (('M', 'Male'),('F', 'Female'))
	years = (   '1973','1974','1975','1976','1977','1978','1979',
				'1980','1981','1982','1983','1984','1985','1986',
				'1987','1988','1989','1990','1991','1992','1993',
				'1994','1995','1996','1997','1998','1999','2000',
				'2001','2002','2003','2004','2005','2006','2007',
				'2008','2009','2010','2011','2012','2013','2014',
				'2015','2016','2017','2018','2019','2020','2021',
				'2022','2023','2024','2025','2026','2027','2028',
				'2029','2030','2031','2032','2033','2034','2035',
				'2036','2037','2038','2039','2040','2041','2042',
				'2043','2044','2045','2046','2047','2048','2049',
				'2050','2051','2052','2053','2054','2055','2056',
				'2057','2058','2059','2060','2061','2062','2063',
				'2064','2065','2066','2067','2068','2069','2070',
				'2071','2072','2073','2074','2075','2076','2077',
				'2078','2079','2080','2081','2082','2084','2083',
				'2084','2085','2086','2087','2088','2089','2090',
				'2091','2092','2093','2094','2095','2096','2097',
				'2098','2099',)

	username = forms.CharField(label='Phone Number', 
		                     widget=forms.TextInput(attrs={'class':'formStyle','size':'60'})
		                )
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'formStyle','size':'60'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'formStyle','size':'60'}))
	sex = forms.MultipleChoiceField(choices=types, widget=forms.CheckboxSelectMultiple(attrs={'class':'formStyle'}))
	date_of_birth = forms.DateField(label='Date of birth',  widget=forms.SelectDateWidget(years=years, 
		attrs={'class':'formStyle'})
	)
	total_household = forms.CharField(widget=forms.NumberInput(attrs={'class':'formStyle'}),
		label='Number of people in your house'
	)

	password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'class':'formStyle','size':'60'}))
	password2 = forms.CharField(label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={'size':'60', 'class':'formStyle'}),
        help_text=_("Enter the same password as above, for verification."))

	class Meta:
		model = Member
		fields = ['first_name', 'last_name', 'username', 'sex', 'date_of_birth',
		          'total_household', 'password1', 'password2'
	    ] 

class LoginForm(forms.Form):
	phone_number = forms.CharField(max_length=60, 
		widget=forms.TextInput(attrs={'class':'formStyle', 'size':'60'}),
		help_text='Make sure to use the same number you used to register' 
		)
	password = forms.CharField(max_length=60, 
		widget=forms.PasswordInput(attrs={'class':'formStyle', 'size':'60'})
		)

class UploadProfileForm(forms.Form):
	photo = forms.ImageField(label='')