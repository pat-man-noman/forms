from django import forms

class Hey(forms.Form):
    greeting = forms.CharField()

class Age(forms.Form):
    end = forms.IntegerField()
    birth = forms.IntegerField()

class Order(forms.Form):
    burger = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Font(forms.Form):
    word = forms.CharField()
    repeat = forms.IntegerField()

class Teen(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()

class Xyz(forms.Form):
    xyz = forms.CharField()

class Centered(forms.Form):
    c = forms.IntegerField()
    e = forms.IntegerField() 
    n = forms.IntegerField()
    t = forms.IntegerField()
    er = forms.IntegerField()
    r = forms.IntegerField()
    ed = forms.IntegerField()