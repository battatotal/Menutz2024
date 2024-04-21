from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.base import View


class MenuView(View):
    def get(self, request, item_slug=None):

        return render(request, 'mymenu/index.html',
                      {'cat_selected': item_slug})
