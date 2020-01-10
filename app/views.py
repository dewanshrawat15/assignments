from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponse, JsonResponse

from .models import Project
from .forms import ProjectForm
# Create your views here.

@login_required
def project(request):
	username = request.user
	projectsByUser = Project.objects.filter(author=username).order_by('-submitted_Date_Time')
	return render(request, 'app/list.html', {'projects': projectsByUser})

@login_required
def project_new(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.author = request.user
			project.save()
			return redirect('project')
	else:
		form = ProjectForm()
	return render(request, 'app/new_project.html', {'form': form})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'app/project_details.html', {'project': project})