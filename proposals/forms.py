from django import forms

from .models import ProposalRequest


class ProposalRequestForm(forms.ModelForm):
    class Meta:
        model = ProposalRequest
        fields = ["full_name", "organization", "email", "phone", "sector", "message", "tor_document"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 20:
            raise forms.ValidationError("Tafadhali eleza ombi lako kwa undani zaidi (angalau maneno 20).")
        return message
