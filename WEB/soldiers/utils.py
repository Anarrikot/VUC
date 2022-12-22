from rest_framework.pagination import PageNumberPagination

class SolderAPIPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


menu = [{'title': "Главная страница", 'url_name': 'home'},
 {'title': "О сайте", 'url_name': 'about'},
 {'title': "Преподаватели", 'url_name': 'home'},
 {'title': "Добавить преподователя", 'url_name': 'addsolder'}]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context