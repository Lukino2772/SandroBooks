from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class SecureIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated