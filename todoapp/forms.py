from django import forms
from todoapp.models import TodoModel


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        clean_field = super(TodoForm, self).clean()
        title = clean_field.get('title')

        if not title :
            raise forms.ValidationError('You have to fill the form correctly.')
