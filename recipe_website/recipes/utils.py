menu = [{'title': 'Add Page', 'url_name': 'add-page'},
]


class DataMixin:
    paginate_by = 9

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

