from django import forms
from django.forms import ModelForm, TextInput

from comprateca.mvp.models import Article

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		exclude = ('date',)
		widgets = {
			'title':TextInput(attrs={'class':'input-form width-50','placeholder':'Titulo del Articulo'}),
			'price':TextInput(attrs={'class':'input-form width-30','placeholder':'Precio'}),
		}