from django import forms
# import models
from main_app.models import (Event, EventPlatform, Member, MemberInterest,
                             MemberSkill, SkillLevel, TechGroup, TechGroupLink,
                             TechnicalArea)

base_choices = [(None, "--------")]


class EventFilterForm(forms.Form):
    """form class used to filter Event list view"""

    def __init__(self, *args, **kwargs):
        super(EventFilterForm, self).__init__(*args, **kwargs)

    group = forms.ModelChoiceField(
        queryset=TechGroup.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Group",
    )

    location__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Location"
    )

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )


class EventPlatformFilterForm(forms.Form):
    """form class used to filter EventPlatform list view"""

    def __init__(self, *args, **kwargs):
        super(EventPlatformFilterForm, self).__init__(*args, **kwargs)

    base_url__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Base Url"
    )

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )

    techgroup = forms.ModelChoiceField(
        queryset=TechGroup.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Techgroup",
    )


class MemberFilterForm(forms.Form):
    """form class used to filter Member list view"""

    def __init__(self, *args, **kwargs):
        super(MemberFilterForm, self).__init__(*args, **kwargs)

    email__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Email"
    )

    first_name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="First Name"
    )

    last_name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Last Name"
    )

    zip_code__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Zip Code"
    )

    memberinterest__interest__name = forms.ChoiceField(
        choices=base_choices + [(i.name, i.name) for i in TechnicalArea.objects.all()],
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Interest",
    )

    memberskill__skill__name = forms.ChoiceField(
        choices=base_choices + [(i.name, i.name) for i in TechnicalArea.objects.all()],
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Skill",
    )


class MemberInterestFilterForm(forms.Form):
    """form class used to filter MemberInterest list view"""

    def __init__(self, *args, **kwargs):
        super(MemberInterestFilterForm, self).__init__(*args, **kwargs)

    interest = forms.ModelChoiceField(
        queryset=TechnicalArea.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Interest",
    )

    member = forms.ModelChoiceField(
        queryset=Member.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Member",
    )


class MemberLinkFilterForm(forms.Form):
    """form class used to filter MemberLink list view"""

    def __init__(self, *args, **kwargs):
        super(MemberLinkFilterForm, self).__init__(*args, **kwargs)

    member = forms.ModelChoiceField(
        queryset=Member.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Member",
    )

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )

    url__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Url"
    )


class MemberSkillFilterForm(forms.Form):
    """form class used to filter MemberSkill list view"""

    def __init__(self, *args, **kwargs):
        super(MemberSkillFilterForm, self).__init__(*args, **kwargs)

    level = forms.ModelChoiceField(
        queryset=SkillLevel.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Level",
    )

    member = forms.ModelChoiceField(
        queryset=Member.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Member",
    )

    skill = forms.ModelChoiceField(
        queryset=TechnicalArea.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Skill",
    )


class SkillLevelFilterForm(forms.Form):
    """form class used to filter SkillLevel list view"""

    def __init__(self, *args, **kwargs):
        super(SkillLevelFilterForm, self).__init__(*args, **kwargs)

    description__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Description"
    )

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )

    memberskill = forms.ModelChoiceField(
        queryset=MemberSkill.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Memberskill",
    )


class TechGroupFilterForm(forms.Form):
    """form class used to filter TechGroup list view"""

    def __init__(self, *args, **kwargs):
        super(TechGroupFilterForm, self).__init__(*args, **kwargs)

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )

    platform = forms.ModelChoiceField(
        queryset=EventPlatform.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Platform",
    )

    url__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Url"
    )

    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Event",
    )

    techgrouplink = forms.ModelChoiceField(
        queryset=TechGroupLink.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Techgrouplink",
    )


class TechGroupLinkFilterForm(forms.Form):
    """form class used to filter TechGroupLink list view"""

    def __init__(self, *args, **kwargs):
        super(TechGroupLinkFilterForm, self).__init__(*args, **kwargs)

    group = forms.ModelChoiceField(
        queryset=TechGroup.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Group",
    )

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )

    url__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Url"
    )


class TechnicalAreaFilterForm(forms.Form):
    """form class used to filter TechnicalArea list view"""

    def __init__(self, *args, **kwargs):
        super(TechnicalAreaFilterForm, self).__init__(*args, **kwargs)

    description__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Description"
    )

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )

    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Event",
    )

    memberinterest = forms.ModelChoiceField(
        queryset=MemberInterest.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Memberinterest",
    )

    memberskill = forms.ModelChoiceField(
        queryset=MemberSkill.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Memberskill",
    )
