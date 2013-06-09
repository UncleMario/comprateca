import urllib

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django_facebook.api import get_persistent_graph, require_persistent_graph
from django_facebook.decorators import facebook_required_lazy, facebook_required
from django_facebook.utils import next_redirect, parse_signed_request

from comprateca.mvp.forms import ArticleForm
from comprateca.mvp.models import Article


#Publish Article 
@facebook_required(scope='publish_stream')
@login_required(login_url='/login/')
def article(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save(commit=False)
			article.owner = request.user
			article.save()

			#Publish on wall user
			fb = get_persistent_graph(request)  
			message = article.get_wall_message()
			fb.set('me/feed', message=message)  
			messages.info(request, 'Publicar en tu muro esta Compra')  

			return HttpResponseRedirect('/mvp/article/%s' % article.pk)
	else:
		form = ArticleForm()
	return render_to_response('mvp/article.html',
		{'form':form}, context_instance=RequestContext(request))


def articles(request):
	articles = Article.objects.all()
	return render_to_response('mvp/articles.html',
		{'articles':articles},context_instance=RequestContext(request))


@login_required(login_url='/login/')
def my_publications(request):
	articles = Article.objects.filter(owner=request.user)
	return render_to_response('mvp/my_publications.html',
		{'articles':articles},context_instance=RequestContext(request))


def view_article(request,articleID):
	article = get_object_or_404(Article, pk=articleID)
	return render_to_response('mvp/view_article.html',
		{'article':article},context_instance=RequestContext(request))

def search(request):
	q = urllib.unquote(request.GET.get('q',''))
	q = q.strip()
	if q != '':
		results = Article.objects.filter(title__icontains= q)
		total = results.count()
	return render_to_response('mvp/results.html', 
		{'results':results, 'total':total, 'article' : q}, context_instance=RequestContext(request))


#Test FacebookUserConverter Model 
def test_open_facebook(request):
	from django_facebook.api import FacebookUserConverter

	fb = get_persistent_graph(request)  

	instace = FacebookUserConverter(fb)

	#Get Friends
	return HttpResponse(instace.get_friends())









