from django.shortcuts import render
from app.forms import *
# Create your views here.
def hey(request):
    form = Hey(request.GET)
    if form.is_valid():
        name = form.cleaned_data['greeting']
        return render(request, "hey.html", {"form": form, "name":name})
    else:
        name = None
        return render(request, "hey.html", {"form": form})
    
def age(request):
    form = Age(request.GET)
    if form.is_valid():
        end = form.cleaned_data['end']
        birth = form.cleaned_data['birth']
        age = end - birth
        return render(request, "age.html", {"form": form, "end":end, "birth":birth, "age":age})
    else:
        end = None
        birth = None
        age = None
        return render(request, "age.html", {"form": form})

def order(request):
    form = Order(request.GET)
    if form.is_valid():
        burger= form.cleaned_data['burger']
        fries = form.cleaned_data['fries']
        drinks= form.cleaned_data['drinks']

        sub_total = round(float((burger * 4.50) + (fries * 1.50) + (drinks * 1)),2)
        taxes = round(float(sub_total * .07),2)
        total = round(float(sub_total + taxes),2)
        return render(request, "order.html", {"form": form, "burger":burger, "fries":fries, "drinks":drinks, "sub_total":sub_total, "taxes":taxes, "total":total})
    else:
        burger = None
        fries = None
        drinks = None
        sub_total = None
        taxes = None
        total = None
        return render(request, "order.html", {"form": form})
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def font(request):
    form = Font(request.GET)
    if form.is_valid():
        word = form.cleaned_data['word']
        repeat= form.cleaned_data['repeat']
        final = word[0:3] * repeat
        return render(request, 'font.html', {"word":word, "repeat":repeat, "final":final})
    else:
        word=None
        repeat=None
        final=None
        return render(request, "font.html", {"form":form})
def teen(request):
    form = Teen(request.GET)
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        D = 0
        if a in range(13, 20):
            a = 0
            
        if b in range(13, 20):
            b = 0
            
        if c in range(13, 20):
            c = 0
        
        D = a + b + c

        return render(request, "teen.html", {'form': form, 'D': D})
    else:
        return render(request, "teen.html", {'form': form})
def xyz(request):
    form = Xyz(request.GET)
    if form.is_valid():
        xyz = form.cleaned_data['xyz']
        if 'xyz' and '.xyz' not in xyz:
            boo = True
        else:
            boo = False
        

        return render(request, "xyz.html", {"form": form, "boo": boo})
    else:
        boo = None

        return render(request, "xyz.html", {"form": form})
def centered(request):
    form = Centered(request.GET)

    if form.is_valid():
        C_list = [
            form.cleaned_data["c"],
            form.cleaned_data["e"],
            form.cleaned_data["n"],
            form.cleaned_data["t"],
            form.cleaned_data["er"],
        ]

        # Append the 6th and 7th values only if they are not None or empty
        given_amount_6 = form.cleaned_data["r"]
        given_amount_7 = form.cleaned_data["ed"]

        if given_amount_6 is not None and given_amount_6 != '':
            C_list.append(given_amount_6)
        if given_amount_7 is not None and given_amount_7 != '':
            C_list.append(given_amount_7)

        if len(C_list) > 2:
            
            C_list.sort()
            C_list = C_list[1:-1]  
            centered_avg = sum(C_list) / len(C_list) 
            centered_avg = int(centered_avg)
        else:
            centered_avg = None

        return render(request, "centered.html", {"form": form,"centered_avg": centered_avg})

    else:
        return render(request, "centered.html", {"form": form})