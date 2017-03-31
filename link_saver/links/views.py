from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import link
from .forms import create_form
# Create your views here.


def link_create(request):
	form = create_form(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("list")
	context = {
		"form" : form,
	}

	return render (request, "link_create.html", context)





def link_list(request):
	queryset = link.objects.all()
	context = {
		"queryset" : queryset,
		"title" : "All Links"
	}
	return render(request, "index.html", context)