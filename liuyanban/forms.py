from django import forms

class MessageForm(forms.Form):

	"""docstring for MessageForm"""

	name = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	homepage = forms.URLField(required = False)
	content = forms.CharField(required = True)
	publish_time = forms.DateTimeField(required = True)
