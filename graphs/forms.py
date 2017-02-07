

from django.forms import ModelForm

from graphs.models import book1,book2,book3,book4


class PostInputFormBook1(ModelForm):

    class Meta:
        model = book1
        fields = '__all__'



class PostInputFormBook2(ModelForm):

    class Meta:
        model = book2
        fields = '__all__'



class PostInputFormBook3(ModelForm):

    class Meta:
        model = book3
        fields = '__all__'



class PostInputFormBook4(ModelForm):

    class Meta:
        model = book4
        fields = '__all__'
