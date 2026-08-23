from django import forms

from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["full_name", "email", "phone", "cover_message", "resume"]
        widgets = {
            "cover_message": forms.Textarea(attrs={"rows": 5}),
        }

    def clean_cover_message(self):
        message = self.cleaned_data["cover_message"].strip()
        if len(message) < 20:
            raise forms.ValidationError("Tafadhali eleza kwa undani zaidi kwa nini unafaa nafasi hii.")
        return message
