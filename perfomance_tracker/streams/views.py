from django.db.models import Count
from django.urls import reverse_lazy
from django.views import generic

from .models import Stream

# Create your views here.


class StreamsList(generic.ListView):
    model = Stream
    queryset = Stream.objects.annotate(groups_num=Count('group'))
    context_object_name = 'streams'
    ordering = [
        '-stream'
    ]
    template_name = 'streams/streams.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        search = self.request.GET.get('search') or ''
        if search:
            context_data['streams'] = context_data['streams'].filter(
                stream__icontains=search
            )
        context_data['search'] = search
        return context_data


class StreamDetail(generic.DetailView):
    model = Stream
    context_object_name = 'stream'
    template_name = 'streams/stream.html'


class AddStream(generic.CreateView):
    model = Stream
    fields = '__all__'
    success_url = reverse_lazy('streams:streams')


class EditStream(generic.UpdateView):
    model = Stream
    fields = '__all__'
    success_url = reverse_lazy('streams:streams')


class DeleteStream(generic.DeleteView):
    model = Stream
    context_object_name = 'stream'
    success_url = reverse_lazy('streams:streams')
