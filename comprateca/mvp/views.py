from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django_facebook.api import get_persistent_graph, require_persistent_graph
from django_facebook.decorators import facebook_required_lazy, facebook_required
from django_facebook.utils import next_redirect, parse_signed_request

from comprateca.mvp.forms import ArticleForm


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

			return HttpResponseRedirect('/article/%s' % article.pk)
	else:
		form = ArticleForm()
	return render_to_response('mvp/article.html',
		{'form':form}, context_instance=RequestContext(request))


def articles(request):
	articles = Article.objects.all()
	return render_to_response('mvp/articles.html',
		{'articles':articles},context_instance=RequestContext(request))