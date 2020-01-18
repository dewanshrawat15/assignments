from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponse, JsonResponse

from .models import Project
from .forms import ProjectForm
# Create your views here.

def project(request):
	username = request.user
	if username.is_anonymous:
		projectsByUser = Project.objects.all().order_by('-submitted_Date_Time')
		stat = False
	else:
		projectsByUser = Project.objects.filter(author=username).order_by('-submitted_Date_Time')
		stat = True
	return render(request, 'app/list.html', {'projects': projectsByUser, 'loginStat': stat})

@login_required
def project_new(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			project = form.save(commit=False)
			project.author = request.user
			project.save()
			return redirect('project')
	else:
		form = ProjectForm()
	return render(request, 'app/new_project.html', {'form': form})

@login_required
def project_delete(request, pk):
	project = get_object_or_404(Project, pk=pk)
	if request.user == project.author:
		project.delete()
		return redirect('project')
	else:
		return HttpResponse("Access Denied")

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user.is_anonymous:
    	stat = False
    else:
    	if request.user == project.author:
    		stat = True
    	else:
    		stat = False
    return render(request, 'app/project_details.html', {'project': project, 'loginStat': stat})