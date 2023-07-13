from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name="core"
urlpatterns = [
    path("",views.index,name="home"),
    path("data/",views.data_json),
    path("user/join",views.register_user,name="signup"),
    path("user/login",views.login_user,name="login"),
    path("user/logout",views.logout_user,name="logout"),
    path("category/<slug:val>",views.category,name="category")
]
