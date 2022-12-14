from django import forms

from ff_tickets.news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'is_private', 'news_photos')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter title',
                       }),
            'content': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter description'}),
            'is_private': forms.NullBooleanSelect(),
        }
