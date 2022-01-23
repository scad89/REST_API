from django.contrib import admin
from .models import TaskTable
from django import forms
from ckeditor.widgets import CKEditorWidget


class TaskTableAdminForm(forms.ModelForm):
    comment = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = TaskTable
        fields = '__all__'


@admin.register(TaskTable)
class TaskTableAdmin(admin.ModelAdmin):
    form = TaskTableAdminForm
