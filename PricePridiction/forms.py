from django import forms
from .models import HousePricePredictionModel
import pandas as pd
import os

# Assuming that the CSV file is directly in the '/app' directory of the ml-model-data volume
csv_file_path = os.path.join('/app', 'processed_data.csv')

df = pd.read_csv(csv_file_path)
location_list, size_list, sqft_list, bath_list = (
    list(df['location'].unique()),
    list(df['size'].unique()),
    list(df['total_sqft'].unique()),
    list(df['bath'].unique())
)

BLANK_CHOICE = [('', '')]
LOCATION_CHOICES = BLANK_CHOICE + [(location_list[i], data) for i, data in enumerate(location_list)]
SIZE_CHOICES = BLANK_CHOICE + [(size_list[i], data) for i, data in enumerate(size_list)]
SQFT_CHOICES = BLANK_CHOICE + [(sqft_list[i], data) for i, data in enumerate(sqft_list)]
BATH_CHOICES = BLANK_CHOICE + [(bath_list[i], data) for i, data in enumerate(bath_list)]

class HousePricePredictionForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION_CHOICES)
    size = forms.ChoiceField(choices=SIZE_CHOICES)
    total_sqft = forms.ChoiceField(choices=SQFT_CHOICES)  # Fix typo here
    bath = forms.ChoiceField(choices=BATH_CHOICES)

    class Meta:
        model = HousePricePredictionModel
        exclude = ('price',)
