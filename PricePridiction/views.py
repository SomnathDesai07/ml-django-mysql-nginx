from django.shortcuts import render
from django.http import HttpResponse
import pickle
from .forms import HousePricePredictionForm
import os
import pandas as pd
def home(r):
    form = HousePricePredictionForm()
    return render(r, 'index.html', {'form': form})



def result(r):
    if r.method == 'POST':
        form = HousePricePredictionForm(r.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            size = form.cleaned_data['size']
            total_sqft = form.cleaned_data['total_sqf']
            bath = form.cleaned_data['bath']

            pickle_file_path = os.path.join('/app', 'RidgeModel.pkl')
            with open(pickle_file_path, 'rb') as model_file:
                model = pickle.load(model_file)


            input_data = pd.DataFrame([[location,size, total_sqft, bath]], columns=['location','size', 'total_sqft', 'bath'])
            predicted_price = round(model.predict(input_data)[0])


            house = form.save(commit=False)
            house.price = predicted_price
            house.save()

            return render(r, 'result.html', {'predicted_price': predicted_price})

    return HttpResponse('Invalid form submission')

