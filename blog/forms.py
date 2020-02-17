from django import forms

from .models import Article


class ArticleCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter Title Here..."}))
    passage = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Enter Passage Here..."}))
    publish_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'placeholder': "YYYY-MM-DD"}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Article
        fields = [
            'title',
            'passage',
            'publish_date',
            'image',
        ]


class ArticleEditForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Article
        fields = [
            'title',
            'passage',
            'image',
        ]
