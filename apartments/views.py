from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from apartments.actions.predict import predict_price
from .models.apartments import Apartment
from django.shortcuts import render
from .form import ApartmentForm, PredictitonsForm, ApartmentFormReadOnly
from .models.predictions import Predictions


def save_predicted_price(request):
    print(request.POST)
    form = PredictitonsForm(request.POST)
    predicted = form.save()
    if request.POST["accurate_price"] == "false":
        accurate_price = False
    else:
        accurate_price = True
    Predictions.objects.filter(id=predicted.id).update(accurate_price=accurate_price)
    form = ApartmentForm()
    return render(request, "apartments/home.html",
                  {"form": form})


def make_predictions(request):
    form = ApartmentForm()
    return render(request, "apartments/home.html",
                  {"form": form})


def predict(request):
    form = ApartmentForm(request.POST)
    if form.is_valid():
        predictid, apartmentid = predict_price(request.POST)
        prediction = Predictions.objects.filter(id=predictid).first()
        apartment = Apartment.objects.filter(id=apartmentid).first()
        f = ApartmentFormReadOnly(instance=apartment)
        form = PredictitonsForm(instance=prediction)
        return render(request, "apartments/result.html",
                      {"f": f, "form": form})
    else:
        return render(request, "apartments/home.html",
                      {"form": form})
