from django.contrib import admin
from django.urls import path, include

from mymenu.views import MenuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('mymenu.urls', namespace="mymenu")),
    # path('', MenuView.as_view(), name="main"),
    # path('<slug:item_slug>/', MenuView.as_view(), name="menu"),
    path("__debug__/", include("debug_toolbar.urls")),

]