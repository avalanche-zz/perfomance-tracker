from django.db.models import Count
from django.urls import reverse_lazy
from django.views import generic

from .models import Group
from streams.models import Stream

# Create your views here.


class GroupsList(generic.ListView):
    model = Group
    queryset = Group.objects.annotate(students_number=Count('student'))
    context_object_name = 'groups'
    ordering = [
        '-group_number'
    ]
    template_name = 'groups/groups.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['streams'] = Stream.objects.all().order_by('stream')

        search = self.request.GET.get('search') or ''
        if search:
            groups = [group for group in context_data['groups']
                      if search.lower().strip() in str(group).lower()]
            context_data['groups'] = groups
        context_data['search'] = search

        stream = self.request.GET.get('stream') or ''
        if stream:
            context_data['groups'] = context_data['groups'].filter(
                stream_id=stream
            )
        context_data['stream_selected'] = stream

        sort = self.request.GET.get('sort') or ''
        order = self.request.GET.get('order') or ''
        if not sort or sort == 'group':
            if not order or order == 'up':
                context_data['groups'] = context_data['groups'].order_by(
                    'education_type', 'stream', 'group_number', 'subgroup'
                )
            else:
                context_data['groups'] = context_data['groups'].order_by(
                    '-education_type', '-stream', '-group_number', '-subgroup'
                )
        elif sort == 'students_number':
            if not order or order == 'up':
                context_data['groups'] = context_data['groups'].order_by(
                    'students_number'
                )
            else:
                context_data['groups'] = context_data['groups'].order_by(
                    '-students_number'
                )
        context_data['sort'] = sort
        context_data['order'] = order
        return context_data


class GroupDetail(generic.DetailView):
    model = Group
    context_object_name = 'group'
    template_name = 'groups/group.html'


class AddGroup(generic.CreateView):
    model = Group
    fields = '__all__'
    success_url = reverse_lazy('groups:groups')


class EditGroup(generic.UpdateView):
    model = Group
    fields = '__all__'
    success_url = reverse_lazy('groups:groups')


class DeleteGroup(generic.DeleteView):
    model = Group
    context_object_name = 'group'
    success_url = reverse_lazy('groups:groups')
