from .models import User, Post
from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post # configure the model to work from
        #
        fields = '__all__' # pull all model fields to use
        #
        labels = {
            'message': "",
        }
        #
        widgets = {
            'user': forms.HiddenInput(), # auto-done
            'timestamp': forms.HiddenInput(),
            'message': forms.Textarea(attrs={'cols':80, 'rows':2, 'class':'squeak_entry', 'id':'counter', 'onkeyup':'myCounter(this);'}),
            'likers': forms.HiddenInput(),
        }


# https://www.codexworld.com/live-character-counter-javascript/