from django import forms

from .models import BuyerRegistration, EventRegistration, ProjectApplication


class BuyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = BuyerRegistration
        fields = ["buyer_type", "name", "contact", "company"]

    def clean(self):
        cleaned_data = super().clean()
        if (
            cleaned_data.get("buyer_type") == BuyerRegistration.WHOLESALE
            and not cleaned_data.get("company")
        ):
            self.add_error("company", "Укажите название компании.")
        return cleaned_data


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ["event_title", "name", "contact", "guests"]


class ProjectApplicationForm(forms.ModelForm):
    class Meta:
        model = ProjectApplication
        fields = ["name", "contact", "idea"]
