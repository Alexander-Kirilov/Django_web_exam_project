from django import forms

from ff_tickets.news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'is_private', 'news_photos')
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
        #     }
        # }

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'}),
        #     'created_at': forms.TextInput(attrs={'class': 'form-control'}),
        #     'created_by': forms.TextInput(attrs={'class': 'form-control'}),
        # }
