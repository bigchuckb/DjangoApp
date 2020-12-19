from django.shortcuts import render, redirect
from collection.forms import ThingForm, RatingForm, ShtetlForm
from collection.models import Books, Rating, Shtetl
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
    if thing.owner != request.user:
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

def add_rating(request, slug=None):
    form_class = RatingForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.save()
            return redirect('home')
    else:
        form = form_class()

    return render(request, 'log_rating.html', {'form': form,})

def add_shtetl(request):
    form_class = ShtetlForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            shtetl = form.save(commit=False)
            shtetl.user = request.user
            shtetl.save()
            return redirect('home')
    else:
        form = form_class()

    return render(request, 'log_shtetl.html', {'form':form,})

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


def pie_chart(request):
    labels = []
    data = []

    queryset = Books.objects.all()
    for book in queryset:
        if str(book.title) in labels:
            pass
        else:
            labels.append(str(book.title))
            avg_rating = book.average_rating
            data.append(str(avg_rating))

    context = {'title':'Book Ratings',
                'labels': labels,
                'data': data}
    print(context)

    return render(request, 'chart.html', context)

def shtetl_record(request):
    labels =[]
    data = []

    queryset = Shtetl.objects.all()
    for shtetl in queryset:
        if str(shtetl.winner) in labels:
            pass
        else:
            labels.append(str(shtetl.winner))
            wincount = Shtetl.objects.filter(winner=shtetl.winner).count()
            data.append(str(wincount))

    context = {'title':"Settler's Victories",
                'labels': labels,
                'data': data}
    print(context)

    return render(request, 'chart_2.html',context)