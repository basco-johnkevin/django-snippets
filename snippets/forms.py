from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from tags.models import ApprovedTag

from .models import Snippet


class CreateSnippetForm(forms.ModelForm):

    tags = forms.MultipleChoiceField(required=False)

    submit_label = None

    DEFAULT_SUBMIT_LABEL = 'Submit'

    def __init__(self, *args, **kwargs):
        super(CreateSnippetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', self.get_submit_label()))

        self.fields['tags'].choices = ApprovedTag.objects.filter(approved=True).values_list('name', 'name')
        self.fields['tags'].widget.attrs['data-placeholder'] = 'Choose tags'

    class Meta:
        model = Snippet
        fields = ('title', 'body', 'tags')

    def get_submit_label(self):
        if not self.submit_label:
            return self.DEFAULT_SUBMIT_LABEL

        return self.submit_label

    def clean_tags(self):
        """
        Check if the tag/tags chosen by a user is available
        """
        available_tags = ApprovedTag.objects.all().values_list('name', flat=True)
        chosen_tags = self.cleaned_data['tags'] 

        for tag in chosen_tags:
            if tag not in available_tags:
                raise forms.ValidationError(_('The tag you chose is not avaiable.'))

        return chosen_tags


class UpdateSnippetForm(CreateSnippetForm):

    def __init__(self, *args, **kwargs):
        self.submit_label = 'Update'
        super(UpdateSnippetForm, self).__init__(*args, **kwargs)
        