from django.contrib.admin import FieldListFilter


def get_custom_titled_list_filter(title: str) -> FieldListFilter:
    """
    Утилита которая позволяет установить свой заголовок в поисковом фильтре(list_filter).
    :param title: Заголовок
    :return:
    """
    class Wrapper(FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper
