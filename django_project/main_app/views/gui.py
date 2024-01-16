from handyhelpers.views import (HandyHelperIndexView)

# import models
# from main_app.models import ()

# import forms
# from main_app.forms import ()


class Index(HandyHelperIndexView):
    """render the main_app index page"""

    title = """Main_App"""
    subtitle = "Select an option below"
    item_list = [
        {
            "url": "/main_app/dashboard",
            "icon": "fas fa-tachometer-alt",
            "title": "Dashboard",
            "description": "Dashboard for Main_App ",
        },
        {
            "url": "/main_app/rest",
            "icon": "fas fa-download",
            "title": "APIs",
            "description": "List RESTful APIs for Main_App",
        },
    ]
    protected_item_list = []
    protected_group_name = "admin"


# class ListMyModels(HandyHelperListPlusCreateAndFilterView):
#     """list available MyModel entries"""
#     queryset = MyModel.objects.all()
#     title = "MyModel"
#     table = "myapp/table/mymodels.htm"


# class DetailMyModel(DetailView):
#     model = MyModel
#     template_name = 'myapp/detail/mymodel.html'
