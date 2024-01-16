""" report like pages for app models and data """

# from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.report import AnnualProgressView, AnnualStatView, AnnualTrendView

# from handyhelpers.views.report import get_colors

# import models
# from main_app.models import ()


class Main_AppDashboard(View):
    """main_app dashboard"""

    template_name = "main_app/custom/dashboard.html"

    def get(self, request):
        """render dashboard for main_app specific data"""
        context = {"title": "Main_App Dashboard"}
        return render(request, self.template_name, context=context)


class Main_AppAnnualProgressView(AnnualProgressView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]


class Main_AppAnnualStatView(AnnualStatView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]


class Main_AppAnnualTrendView(AnnualTrendView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]
