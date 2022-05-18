from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import Stream
from .forms import AddStreamForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'streams/index.html'
    context_object_name = 'streams'
    
    def get_queryset(self):
        return Stream.objects.order_by('-stream')


class DetailView(generic.DetailView):
    model = Stream
    template_name = 'streams/detail.html'


def add(request):
    if request.method == 'POST':
        form = AddStreamForm(request.POST)
        if form.is_valid():
            Stream.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('streams:index'))
    else:
        form = AddStreamForm()
    context = {
        'form': form
    }
    return render(request, 'streams/add.html', context)


def edit(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)
    context = {
        'stream': stream.id,
        'year': stream,
        'required': stream.required,
        'autopass': stream.autopass
    }
    return render(request, 'streams/edit.html', context)


def delete(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)
    context = {
        'stream': stream.id,
        'year': stream
    }
    return render(request, 'streams/delete.html', context)
