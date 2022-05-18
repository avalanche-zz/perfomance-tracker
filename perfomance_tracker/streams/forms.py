from django.forms import ModelForm
from .models import Stream

class AddStreamForm(ModelForm):

    class Meta:
        model = Stream
        fields = '__all__'
