from django import forms

from study_buddy.classroom.models import Event, JoinedEvent, Location, Comment


class AddLocation(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'post_code': forms.TextInput(attrs={'class': 'form-control'}),
                   }


class AddEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'event_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'location': forms.Select(attrs={'class': 'form-control'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control'}),
                   'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
                   'photo': forms.FileInput(attrs={'class': 'form-control'}),
                   }


class EditEvent(AddEvent):
    pass


class DeleteEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class JoinEventForm(forms.ModelForm):
    class Meta:
        model = JoinedEvent
        fields = '__all__'
        widgets = {'event': forms.HiddenInput(attrs={'class': 'form-control'}),
                   'student': forms.HiddenInput}


class DeleteJoinedEvent(forms.ModelForm):
    class Meta:
        model = JoinedEvent
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class CommentsModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
        }


class DeleteCommentsForm(CommentsModelForm):
    class Meta:
        model = Comment
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
