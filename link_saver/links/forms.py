from django import forms
from .models import link

class create_form(forms.ModelForm):
	links = forms.RegexField(regex=r"\w\w\w\.\w+\.\.*", 
			error_messages={'invalid': ("Not a valid url")})

	links = forms.RegexField(regex=r"https|http\://\w+\.\.*", 
			error_messages={'invalid': ("Not a valid url")})

	links = forms.RegexField(regex=r"\w+\.\w+", 
			error_messages={'invalid': ("Not a valid url")})

	class Meta():
		model = link
		fields = [
			"links"
		]



