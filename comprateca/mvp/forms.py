from django import forms
from django.forms import ModelForm

from comprateca.mvp.models import Article

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		exclude = (date,)