from djangoaddicts.pygwalker.views import PygWalkerListView

# import forms
from main_app.forms.filter_forms import (
    EventFilterForm,
    EventPlatformFilterForm,
    MemberFilterForm,
    MemberInterestFilterForm,
    MemberLinkFilterForm,
    MemberSkillFilterForm,
    SkillLevelFilterForm,
    TechGroupFilterForm,
    TechGroupLinkFilterForm,
    TechnicalAreaFilterForm,
)

# import models
from main_app.models import (
    Event,
    EventPlatform,
    Member,
    MemberInterest,
    MemberLink,
    MemberSkill,
    SkillLevel,
    TechGroup,
    TechGroupLink,
    TechnicalArea,
)


class ListEvents(PygWalkerListView):
    """list available Event entries"""

    queryset = Event.objects.all()
    title = "Events"
    table = "main_app/table/events.htm"

    filter_form_obj = EventFilterForm
    filter_form_title = "<b>Filter Events: </b>"
    filter_form_modal = "filter_event"
    filter_form_tool_tip = "filter events"


class ListEventPlatforms(PygWalkerListView):
    """list available EventPlatform entries"""

    queryset = EventPlatform.objects.all()
    title = "EventPlatforms"
    table = "main_app/table/eventplatforms.htm"

    filter_form_obj = EventPlatformFilterForm
    filter_form_title = "<b>Filter EventPlatforms: </b>"
    filter_form_modal = "filter_eventplatform"
    filter_form_tool_tip = "filter eventplatforms"


class ListMembers(PygWalkerListView):
    """list available Member entries"""

    queryset = Member.objects.all()
    title = "Members"
    table = "main_app/table/members.htm"

    filter_form_obj = MemberFilterForm
    filter_form_title = "<b>Filter Members: </b>"
    filter_form_modal = "filter_member"
    filter_form_tool_tip = "filter members"


class ListMemberInterests(PygWalkerListView):
    """list available MemberInterest entries"""

    queryset = MemberInterest.objects.all()
    title = "MemberInterests"
    table = "main_app/table/memberinterests.htm"

    filter_form_obj = MemberInterestFilterForm
    filter_form_title = "<b>Filter MemberInterests: </b>"
    filter_form_modal = "filter_memberinterest"
    filter_form_tool_tip = "filter memberinterests"


class ListMemberLinks(PygWalkerListView):
    """list available MemberLink entries"""

    queryset = MemberLink.objects.all()
    title = "MemberLinks"
    table = "main_app/table/memberlinks.htm"

    filter_form_obj = MemberLinkFilterForm
    filter_form_title = "<b>Filter MemberLinks: </b>"
    filter_form_modal = "filter_memberlink"
    filter_form_tool_tip = "filter memberlinks"


class ListMemberSkills(PygWalkerListView):
    """list available MemberSkill entries"""

    queryset = MemberSkill.objects.all()
    title = "MemberSkills"
    table = "main_app/table/memberskills.htm"

    filter_form_obj = MemberSkillFilterForm
    filter_form_title = "<b>Filter MemberSkills: </b>"
    filter_form_modal = "filter_memberskill"
    filter_form_tool_tip = "filter memberskills"


class ListSkillLevels(PygWalkerListView):
    """list available SkillLevel entries"""

    queryset = SkillLevel.objects.all()
    title = "SkillLevels"
    table = "main_app/table/skilllevels.htm"

    filter_form_obj = SkillLevelFilterForm
    filter_form_title = "<b>Filter SkillLevels: </b>"
    filter_form_modal = "filter_skilllevel"
    filter_form_tool_tip = "filter skilllevels"


class ListTechGroups(PygWalkerListView):
    """list available TechGroup entries"""

    queryset = TechGroup.objects.all()
    title = "TechGroups"
    table = "main_app/table/techgroups.htm"

    filter_form_obj = TechGroupFilterForm
    filter_form_title = "<b>Filter TechGroups: </b>"
    filter_form_modal = "filter_techgroup"
    filter_form_tool_tip = "filter techgroups"


class ListTechGroupLinks(PygWalkerListView):
    """list available TechGroupLink entries"""

    queryset = TechGroupLink.objects.all()
    title = "TechGroupLinks"
    table = "main_app/table/techgrouplinks.htm"

    filter_form_obj = TechGroupLinkFilterForm
    filter_form_title = "<b>Filter TechGroupLinks: </b>"
    filter_form_modal = "filter_techgrouplink"
    filter_form_tool_tip = "filter techgrouplinks"


class ListTechnicalAreas(PygWalkerListView):
    """list available TechnicalArea entries"""

    queryset = TechnicalArea.objects.all()
    title = "TechnicalAreas"
    table = "main_app/table/technicalareas.htm"

    filter_form_obj = TechnicalAreaFilterForm
    filter_form_title = "<b>Filter TechnicalAreas: </b>"
    filter_form_modal = "filter_technicalarea"
    filter_form_tool_tip = "filter technicalareas"
