from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Books
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    things = Books.objects.all()
    return render(request, 'index.html', {
        'things': things,
        })

def thing_detail(request, slug):
    thing = Books.objects.get(slug=slug)
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
        })

@login_required
def edit_thing(request, slug):
    thing = Books.objects.get(slug=slug)
    if thing.user != request.user:
        raise Http404
    form_class = ThingForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        form = form_class(instance=thing)
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })

def create_thing(request):
    form_class = ThingForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.user = request.user
            thing.slug = slugify(thing.name)
            thing.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        form = form_class()
    
    return render(request, 'things/create_thing.html', {'form': form,
    })

def browse_by_name(request, initial=None):
    if initial:
        things = Books.objects.filter(title__istartswith=initial).order_by('title')
    else:
        things = Books.objects.all().order_by('title')
    
    return render(request, 'search/search.html', {
        'things': things,
        'initial': initial,
    })