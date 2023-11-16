from django import forms 
from datetime import date
from .models import Author




class Form_edit_author(forms.ModelForm):
    class Meta:
        model = Author 
        fields = '__all__'


class Add_authors(forms.Form):
    first_name = forms.CharField(label="First name author")
    last_name = forms.CharField(label="Last name author")
    date_of_birth = forms.DateField(label="Birth author", initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={"type" : date}))
    about = forms.CharField(label="About author", widget=forms.Textarea)
    photo = forms.ImageField(label="Photo author")
