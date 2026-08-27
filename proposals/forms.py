from django import forms

from .models import ProposalRequest


class ProposalRequestForm(forms.ModelForm):
    class Meta:
        model = ProposalRequest
        fields = ["full_name", "organization", "email", "phone", "sector", "message", "tor_document"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, lang="en", **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang
        if lang == "sw":
            self.fields["sector"].label_from_instance = lambda obj: obj.name_sw
        else:
            self.fields["sector"].label_from_instance = lambda obj: obj.name_en

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 20:
            if self.lang == "sw":
                raise forms.ValidationError("Tafadhali eleza ombi lako kwa undani zaidi (angalau maneno 20).")
            raise forms.ValidationError("Please describe your request in more detail (at least 20 words).")
        return message
