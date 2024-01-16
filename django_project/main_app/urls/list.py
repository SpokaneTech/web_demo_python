# urls for list views in main_app

from django.urls import path
from main_app.views import list

urlpatterns = [
    path("list_events/", list.ListEvents.as_view(), name="list_events"),
    path("list_eventplatforms/", list.ListEventPlatforms.as_view(), name="list_eventplatforms"),
    path("list_members/", list.ListMembers.as_view(), name="list_members"),
    path("list_skilllevels/", list.ListSkillLevels.as_view(), name="list_skilllevels"),
    path("list_techgroups/", list.ListTechGroups.as_view(), name="list_techgroups"),
    path("list_techgrouplinks/", list.ListTechGroupLinks.as_view(), name="list_techgrouplinks"),
    path("list_technicalareas/", list.ListTechnicalAreas.as_view(), name="list_technicalareas"),
]
