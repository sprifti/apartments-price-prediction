from unicodedata import decimal

from utils import MODEL, SCALER
import pickle
import pandas as pd
from apartments.models.apartments import Apartment
from apartments.models.predictions import Predictions


def predict_price(data):
    record = {'interior_area': int(data["interior_area"]),
              "bathrooms": int(data["bathrooms"]), "rooms": int(data["rooms"])}
    apartment = Apartment.objects.create(zone=int(data["zone"]), interior_area=int(data["interior_area"]),
                                         bathrooms=int(
                                             data["bathrooms"]), rooms=int(data["rooms"]))
    record = pd.DataFrame(data=record, index=[0])
    # Getting model files for respective zone
    scaler_file = SCALER[int(data["zone"])]
    model_file = MODEL[int(data["zone"])]

    # scaling record based on scaler file
    scaled_record = scale_data(record, scaler_file)
    predicted = predict(scaled_record, model_file)

    predictions = Predictions.objects.create(apartment=Apartment.objects.get(id=apartment.id),
                                             predicted_price=round(predicted, 2))
    return predictions.id, apartment.id


def scale_data(record, scaler):
    scaler = pickle.load(open('trained_models/' + scaler, 'rb'))
    dataframe = scaler.transform(record)
    scaled_record = pd.DataFrame(data=dataframe, columns=record.columns)
    return scaled_record


def predict(record, model):
    model = pickle.load(open('trained_models/' + model, 'rb'))
    predicted = model.predict(record)
    return predicted[0]
