from .models.apartments import Apartment
from .models.predictions import Predictions
from django import forms
from django.core.exceptions import ValidationError


class ApartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApartmentForm, self).__init__(*args, **kwargs)

    def clean_interior_area(self):
        interior_area = self.cleaned_data['interior_area']
        if (int(interior_area) < 65) | (int(interior_area) > 140):
            raise ValidationError(
                "Interior Area should be between 65 and 140"
            )
        return interior_area

    def clean_rooms(self):
        rooms = self.cleaned_data['rooms']
        if (int(rooms) < 1) | (int(rooms) > 2):
            raise ValidationError(
                "Rooms should be between 1 and 2"
            )
        return rooms

    def clean_bathrooms(self):
        bathrooms = self.cleaned_data['bathrooms']
        if (int(bathrooms) < 1) | (int(bathrooms) > 2):
            raise ValidationError(
                "Bathrooms should be between 1 and 2"
            )
        return bathrooms

    class Meta:
        model = Apartment
        fields = ("__all__")


class ApartmentFormReadOnly(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApartmentFormReadOnly, self).__init__(*args, **kwargs)
        self.fields['interior_area'].widget.attrs['readonly'] = True
        self.fields['zone'].widget.attrs['readonly'] = True
        self.fields['rooms'].widget.attrs['readonly'] = True
        self.fields['bathrooms'].widget.attrs['readonly'] = True

    class Meta:
        model = Apartment
        fields = ("__all__")


class PredictitonsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PredictitonsForm, self).__init__(*args, **kwargs)
        # self.fields['id'].widget = forms.HiddenInput()
        self.fields['predicted_price'].widget.attrs['readonly'] = True

    class Meta:
        model = Predictions
        fields = ["id", "predicted_price", "accurate_price"]
