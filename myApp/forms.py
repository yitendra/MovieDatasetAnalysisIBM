from django import forms

class form(forms.Form):
    Review=forms.CharField(max_length=800,widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Your Feedback","id":"input_form","type":"text"}))