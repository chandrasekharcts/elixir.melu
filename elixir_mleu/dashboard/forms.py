from django import forms
from dashboard.models import user_details, question_list
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class update_editorForm(forms.ModelForm):
    update_message = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = user_details
        fields = ['update_message']

class conquest_questionForm(forms.ModelForm):
    question = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = question_list
        fields = ['question']
