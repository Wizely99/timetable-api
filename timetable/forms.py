from django import forms
from timetable.models import EnrolledCourse


class EnrolledCourseForm(forms.ModelForm):
    class Meta:
        model = EnrolledCourse
        fields = "__all__"
        widgets = {
            "color": forms.TextInput(attrs={"type": "color"}),
        }
