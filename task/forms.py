from django import forms
from .models import TaskModel
from category.models import TaskCategory

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'

    categories = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
