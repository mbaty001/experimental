from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import EntryForm, TopicForm

def check_topic_owner(request, owner):
    ''' Verify that owner matches currently logged in user '''
    if owner != request.user:
        raise Http404

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """ Show all topics """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Show a single topic and all its entries """
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(request, topic.owner)
    entries = topic.entry_set.order_by('-date_added')
    
    context = {'topic': topic, 'entries': entries}
    
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """ Add new topic """
    if request.method != "POST":
        # No data submitted, create a blank form
        form = TopicForm()
    else:
        # POST data submitted, process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form
    context = {"form": form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Add new entry for a particular topic """

    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(request, topic.owner)

    print(f'Topic: {topic}')
    if request.method != "POST":
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # Display a blank or invalid form
    context = {"form": form, "topic": topic}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(request, topic.owner)

    if request.method != 'POST':
        # Initial request: pre-fill form with the current entry:
        form = EntryForm(instance=entry)
    else:
        # POST submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)