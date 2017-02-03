

from django.forms import ModelForm

from graphs.models import book1


class PostInputForm(ModelForm):

    class Meta:
        model = book1
        fields = '__all__'