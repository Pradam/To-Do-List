from django.forms import ModelForm
from .models import (ToDoWork,)


class ToDoWorkForm(ModelForm):
    """Form to Create ToDoWork."""

    class Meta:
        model = ToDoWork
        fields = ('name', 'created_by', 'description',
                  'list_date', 'completed',)

    def __init__(self, *args, **kwargs):
        super(ToDoWorkForm, self).__init__(*args, **kwargs)
        for field in self.Meta.fields:
            if field == 'completed':
                pass
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'})
                self.fields[field].required = True
