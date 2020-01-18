from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'short_description', 'long_description', 'languages_or_Frameworks_used', 'project',)