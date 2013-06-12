from django import forms
from django.forms import ModelForm, TextInput

from comprateca.mvp.models import Article

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		exclude = ('owner','date',)
		widgets = {
			'title':TextInput(attrs={'class':'input-form width-350 padding10','placeholder':'Nombre del producto'}),
			'price':TextInput(attrs={'class':'input-form width-350 padding10','placeholder':'Precio al que lo deseas', \
				'style':'position:relative;top:-20px'}),
		}