# -*- coding: utf-8 -*-

from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
    	model = Document
    	fields = '__all__'

    docfile = forms.FileField(
        label='Select a file'
    )
