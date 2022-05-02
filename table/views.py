from django.shortcuts import render
from .models import Athletes
from .filters import AthleteFilter
from django.contrib.auth.decorators import login_required


def listify(csv):
    with open(csv, 'r') as f:
        listt = []
        for line in f:
            line2 = line.split(',')
            line2[5] = line2[5].replace('\n', '')
            listt.append(line2)

    return listt


master_list = listify("I:\\Programmer's pack\\Files and Docs\\CSV files\\snip csv.txt")

atl = Athletes.objects.all()
atl.delete()
for line in master_list:
    atl = Athletes(name=line[0], sport=line[1], nationality=line[2], age=line[3] ,weight=line[4], height=line[5])
    atl.save()
    # for sub in line:


# Create your views here.
@login_required
def home(request):
    all_athletes = Athletes.objects.all()
    myFilter = AthleteFilter(request.GET, queryset=all_athletes)
    all_athletes = myFilter.qs

    context = {
        'athletes': all_athletes,
        'myFilter': myFilter,
        'all_athletes': all_athletes,

    }
    return render(request, 'table/home.html', context)
