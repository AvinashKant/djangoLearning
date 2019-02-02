from django import forms

class NameForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	c_myself = forms.BooleanField(required=False)