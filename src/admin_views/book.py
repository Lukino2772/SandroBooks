from flask_admin.contrib.sqla import ModelView
from markupsafe import Markup

class BookView(ModelView):
    column_list = (
        'title',
        'description',
        'page_count',
        'online_link',
        'audio_link',
        'android_link',
        'ios_link',
    )

    def _description_formatter(view, context, model, name):
        desc = getattr(model, name) or ""
        return desc[:100] + ('...' if len(desc) > 100 else '')

    def _link_formatter(view, context, model, name):
        url = getattr(model, name)
        if url:
            return Markup(f'<a href="{url}" target="_blank">View</a>')
        return ""

    column_formatters = {
        'description': _description_formatter,
        'online_link': _link_formatter,
        'audio_link': _link_formatter,
        'android_link': _link_formatter,
        'ios_link': _link_formatter,
    }

    form_columns = (
        'title',
        'price',
        'image',
        'description',
        'publication_year',
        'page_count',
        'format',
        'ISBN',
        'cover_type',
        'book_type',
        'audience',
        'online_link',
        'audio_link',
        'android_link',
        'ios_link',
        'about_series'
    )

    can_create = True
    can_edit = True
    can_delete = True