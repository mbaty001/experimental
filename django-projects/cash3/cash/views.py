from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import Entry, Person
from .forms import EntryForm
from django.contrib.auth.decorators import login_required

import datetime, time
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import *

@login_required
def index(request):
    """Entry page"""
    entries = Entry.objects.all()
    context = {"entries": entries}

    return render(request, "cash/index.html", context)

@login_required
def stats(request, precision=30):
    precision=30
    """Statistics page"""

    entries = Entry.objects.all()
    persons = Person.objects.all()
    day_stats = dict()
    time_stats = dict()
    delta_stats = dict()
    cash = dict()

    """ Prepare headers for charts' lists """
    """ time data """
    time_header = ["hour"]
    for person in persons:
        time_header.append(person.name)
    time_data = [time_header]

    """ day data """
    day_data = [["day", "number of cash transfers"]]

    """ delta data """
    delta_data = [["year-month", "time delta"]]

    ''' delta sum data '''
    delta_sum_data = [['year-month', 'time delta sum']]

    #
    # Prepare helper data
    #
    for entry in entries:
        try:
            day_stats[entry.entry_date.day] += 1
        except KeyError:
            day_stats[entry.entry_date.day] = 1
        try:
            """time stats are for each persons"""
            hour = str(entry.entry_date.hour)
            if len(hour) == 1:
                hour = "0" + str(hour)
                """ trim minutes according to precission e.g. to 30 or 00"""
            minute = str(int(entry.entry_date.minute / int(precision)) * int(precision))
            if len(minute) == 1:
                minute += "0"

            if f'{hour}:{minute}' not in time_stats:
                time_stats[f'{hour}:{minute}'] = dict()
            try:
                time_stats[f'{hour}:{minute}'][entry.person.id] += 1
            except KeyError:                    
                time_stats[f'{hour}:{minute}'][entry.person.id] = 1
        except Exception as err:
            time_stats[hour + ":" + minute][entry.person.id] = 1

        """ delta stats """
        month = str(entry.month)
        year = str(entry.year)
        if len(month) == 1:
            month = "0" + str(month)

        if f'{year}-{month}' not in delta_stats:
            delta_stats[f'{year}-{month}'] = dict()
        
        delta_stats[f'{year}-{month}'][entry.person.id] = entry.entry_date

    """ Rewrite helper structures for charts needs """
    """ day data """
    for k, v in day_stats.items():
        day_data.append([k, v])

    """ time data """
    for hour in sorted(time_stats.keys()):
        row = [hour]
        for person in persons:
            try:
                row.append(time_stats[hour][person.id])
            except:
                row.append(0)
        time_data.append(row)

    """ delta data and total difference"""
    total_difference = 0
    for year_month, persons_data in sorted(delta_stats.items()):
        try:
            delta = int(
                (
                    time.mktime(persons_data[2].timetuple())
                    - time.mktime(persons_data[1].timetuple())
                )
                / 3600
            )
            delta_data.append([year_month, delta])
            total_difference += delta
            delta_sum_data.append([year_month, total_difference])
        except KeyError:
            print("%s skipped" % year_month)

    if total_difference > 0:
        person = "Przemyslaw"
    else:
        person = "Michal"

    """ 11400k salary, 2% banks's interest, 20% belka, 365 days, 24 hours """
    salary = 11400
    bank = 2
    belka = 20
    cash_difference = (
        (((salary * (bank / float(100)) * (100 - belka) / 100) / 365))
        * abs(total_difference)
        / 24
    )
    cash = {
        "person": person,
        "cash": "{0:.2f}".format(abs(cash_difference)),
        "total_difference": abs(total_difference),
        "bank": bank,
        "belka": belka,
        "salary": salary,
    }

    """ prepare charts """
    day_chart = ColumnChart(SimpleDataSource(data=day_data))
    time_chart = LineChart(SimpleDataSource(data=time_data))
    delta_chart = ColumnChart(SimpleDataSource(data=delta_data))
    delta_sum_chart = LineChart(SimpleDataSource(data=delta_sum_data))

    context = {
        "day_chart": day_chart,
        "time_chart": time_chart,
        "delta_chart": delta_chart,
        'delta_sum_chart': delta_sum_chart,
        "cash": cash,
    }

    return render(request, "cash/stats.html", context)


@login_required
def new_entry(request):
    ''' Add new entry '''
    if request.method != 'POST':
        form = EntryForm()
    else:
        # Post data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cash:index')
    
    # Display a blank or invalid form
    context = {"form": form}
    return render(request, 'cash/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    ''' Edit entry '''
    entry = Entry.objects.get(id=entry_id)
    if request.method != 'POST':
        # Initial request: pre-fill with the current entry
        form = EntryForm(instance=entry)
    else:
        # Post submitted: process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cash:index')
    # Display a form
    context = {'form': form, 'entry':entry}
    return render(request, 'cash/edit_entry.html', context)