from auditlog.registry import auditlog
from django.db import models
from django.urls import reverse
from handyhelpers.models import HandyHelperBaseModel


class Event(HandyHelperBaseModel):
    """ """

    name = models.CharField(max_length=64, help_text="name of this event")
    description = models.TextField(blank=True, null=True, help_text="name of this event")
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, help_text="")
    duration = models.IntegerField(blank=True, null=True, help_text="planned duration of this event")
    location = models.CharField(
        max_length=128, blank=True, null=True, help_text="location where this event is being hosted"
    )
    group = models.ForeignKey("TechGroup", blank=True, null=True, on_delete=models.SET_NULL)
    labels = models.ManyToManyField("TechnicalArea")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("main_app:detail_event", kwargs={"pk": self.pk})


class EventPlatform(HandyHelperBaseModel):
    """ """

    name = models.CharField(max_length=32, unique=True, help_text="service where this tech group is hosted")
    enabled = models.BooleanField(default=True)
    base_url = models.URLField(blank=True, null=True, help_text="base url of provider")

    def __str__(self) -> str:
        return self.name


class Member(HandyHelperBaseModel):
    """ """

    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.EmailField(blank=True, null=True)
    zip_code = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self) -> str:
        return reverse("main_app:detail_member", kwargs={"pk": self.pk})


class MemberInterest(models.Model):
    """ """

    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    interest = models.ForeignKey("TechnicalArea", on_delete=models.CASCADE)
    interest_level = models.IntegerField(default=1, help_text="level of interest (from 1 to 5) in this technical area")

    def __str__(self) -> str:
        return self.interest.name


class MemberLink(models.Model):
    """ """

    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True, help_text="description of this link")
    url = models.URLField(help_text="")
    is_public = models.BooleanField(default=False, help_text="make this contact link publically visible")

    def __str__(self) -> str:
        return self.name


class MemberSkill(models.Model):
    """ """

    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    skill = models.ForeignKey("TechnicalArea", on_delete=models.CASCADE)
    level = models.ForeignKey("SkillLevel", blank=True, null=True, on_delete=models.CASCADE)
    yoe = models.IntegerField(blank=True, null=True, help_text="years of experience with this skill")

    def __str__(self) -> str:
        return self.skill.name


class SkillLevel(HandyHelperBaseModel):
    """ """

    name = models.CharField(max_length=16, unique=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class TechnicalArea(HandyHelperBaseModel):
    """ """

    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class TechGroup(HandyHelperBaseModel):
    """ """

    name = models.CharField(max_length=32, unique=True, help_text="organization hosting this event")
    description = models.TextField(blank=True, null=True, help_text="description of this group")
    enabled = models.BooleanField(default=True)
    platform = models.ForeignKey("EventPlatform", blank=True, null=True, on_delete=models.SET_NULL)
    url = models.URLField(blank=True, null=True, help_text="url of tech group")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("main_app:detail_tech_group", kwargs={"pk": self.pk})


class TechGroupLink(models.Model):
    """ """

    group = models.ForeignKey("TechGroup", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True, help_text="description of this link")
    url = models.URLField(help_text="")

    def __str__(self) -> str:
        return self.name


# register models with auditlog
auditlog.register(Event)
auditlog.register(TechGroup)
auditlog.register(TechnicalArea)
auditlog.register(Member)
