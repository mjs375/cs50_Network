from .models import User, Post
from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post # configure the model to work from
        #
        fields = '__all__' # pull all model fields to use
        #
        labels = []
        #
        widgets = {
            'user': forms.HiddenInput(), # auto-done
            'timestamp': forms.HiddenInput(),
            'message': forms.Textarea(),
            'likers': forms.HiddenInput(),
        }
