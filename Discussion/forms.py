from django.forms import ModelForm
from .models import*

class CreateInGroup(ModelForm):
    class Meta :
        model = Group
        fields = "__all__"

class CreateInMessage(ModelForm):
    class Meta :
        model = Message
        fields = "__all__"

class CreateInMember(ModelForm):
    class Meta :
        model = Member
        fields = "__all__"