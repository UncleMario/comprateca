from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from comprateca.mvp.forms import ArticleForm

#Publish Article 
@login_required(login_url='/login/')
def article(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save(commit=False)
			article.owner = request.user
			article.save()
			return HttpResponseRedirect('/article/%s' % article.pk)
	else:
		form + ArticleForm()
	return render_to_response('mvp/article.html',
		{'form':form}, context_instance=RequestContext(request))


def articles(request):
	articles = Article.objects.all()
	return render_to_response('mvp/articles.html',
		{'articles':articles},context_instance=RequestContext(request))