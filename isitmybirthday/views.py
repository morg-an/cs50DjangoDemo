from django.shortcuts import render
from django import forms
import datetime

MONTHS = [(1, 'January'), (2,'February'), (3, 'March'), (4, 'April'),
(5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'),
(10, 'October'), (11, 'November'), (12, 'December')]

class BirthdayForm(forms.Form):
    month = forms.CharField(label = "Month", widget=forms.Select(choices=MONTHS))
    day = forms.IntegerField(label = "Day", min_value=1, max_value=31)

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            utc_dt = datetime.datetime.now()
            month = int(form.cleaned_data["month"])
            day = int(form.cleaned_data["day"])
            if utc_dt.month == month and utc_dt.day == day:
                return render(request, 'isitmybirthday/answer.html', {
                    "birthday": True,
                })
            else:
                return render(request, 'isitmybirthday/answer.html', {
                    "birthday": False,
                })
    return render(request, 'isitmybirthday/index.html', {
        "form": BirthdayForm
    })

def check(request, birthday):
    utc_dt = datetime.datetime.now()
    currentDay = utc_dt.day
    currentMonth = utc_dt.month
    if not len(birthday) == 4 or not birthday.isdigit():
        return render(request, 'isitmybirthday/index.html', {
            "form": BirthdayForm
        })
    month = int(birthday[0:2])
    day = int(birthday[2:4])
    if day == currentDay and month == currentMonth:
        return render(request, 'isitmybirthday/answer.html', {
            "birthday": True,
        })
    else:
        return render(request, 'isitmybirthday/answer.html', {
            "birthday": False,
        })

