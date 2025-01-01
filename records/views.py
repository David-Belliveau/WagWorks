from django.shortcuts import render, redirect
from .forms import PetDetailsForm
from django.http import HttpResponseRedirect



# Create your views here.
def index(request):
    return render(request, "records/index.html")




def register(request):
    if request.method == "POST":
        print("POST request received")  # Debugging log
        form = PetDetailsForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging log
            form.save() # Save data to the database
            return redirect('success')
        else:
            print("Form is invalid")  # Debugging log
            print(form.errors)
            return render(request, "records/register.html", {'form': form})


    else:
        form = PetDetailsForm()
    
    return render(request, "records/register.html", {'form': form})



def register2(request):
    if request.method == "POST":
        print("POST request received")  # Debugging log
        form = PetDetailsForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging log
            form.save() # Save data to the database
            return redirect('success')
        else:
            print("Form is invalid")  # Debugging log
            print(form.errors)
            return render(request, "records/register2.html", {'form': form})


    else:
        form = PetDetailsForm()
    
    return render(request, "records/register2.html", {'form': form})


def about(request):
    return render(request, "records/about.html")


def success(request):
    return render(request, "records/success.html")


def mission(request):
    return render(request, "records/mission.html")