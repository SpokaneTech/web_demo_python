from django.contrib import admin

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


class EventAdmin(admin.ModelAdmin):
    list_display: list = [
        "id",
        "created_at",
        "updated_at",
        "name",
        "description",
        "date_time",
        "duration",
        "location",
        "group",
    ]
    search_fields: list = ["id", "name", "description", "duration", "location"]
    list_filter: list = ["group"]


class EventPlatformAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "name", "enabled", "base_url"]
    search_fields = ["id", "name", "base_url"]
    list_filter = ["enabled"]


class MemberAdmin(admin.ModelAdmin):
    list_display: list = ["id", "created_at", "updated_at", "first_name", "last_name", "email", "zip_code"]
    search_fields: list = ["id", "first_name", "last_name", "email", "zip_code"]
    list_filter: list = []


class MemberInterestAdmin(admin.ModelAdmin):
    list_display: list = ["id", "member", "interest", "interest_level"]
    search_fields: list = ["id", "interest_level"]
    list_filter: list = ["member", "interest"]


class MemberLinkAdmin(admin.ModelAdmin):
    list_display: list = ["id", "member", "name", "description", "url", "is_public"]
    search_fields: list = ["id", "name", "description", "url"]
    list_filter: list = ["member", "is_public"]


class MemberSkillAdmin(admin.ModelAdmin):
    list_display: list = ["id", "member", "skill", "level", "yoe"]
    search_fields: list = ["id", "yoe"]
    list_filter: list = ["member", "skill", "level"]


class SkillLevelAdmin(admin.ModelAdmin):
    list_display: list = ["id", "created_at", "updated_at", "name", "description", "enabled"]
    search_fields: list = ["id", "name", "description"]
    list_filter: list = ["enabled"]


class TechnicalAreaAdmin(admin.ModelAdmin):
    list_display: list = ["id", "created_at", "updated_at", "name", "description"]
    search_fields: list = ["id", "name", "description"]
    list_filter: list = []


class TechGroupAdmin(admin.ModelAdmin):
    list_display: list = ["id", "created_at", "updated_at", "name", "description", "enabled", "platform", "url"]
    search_fields: list = ["id", "name", "description", "url"]
    list_filter: list = ["enabled", "platform"]


class TechGroupLinkAdmin(admin.ModelAdmin):
    list_display: list = ["id", "group", "name", "description", "url"]
    search_fields: list = ["id", "name", "description", "url"]
    list_filter: list = ["group"]


# register models
admin.site.register(Event, EventAdmin)
admin.site.register(EventPlatform, EventPlatformAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(MemberInterest, MemberInterestAdmin)
admin.site.register(MemberLink, MemberLinkAdmin)
admin.site.register(MemberSkill, MemberSkillAdmin)
admin.site.register(SkillLevel, SkillLevelAdmin)
admin.site.register(TechnicalArea, TechnicalAreaAdmin)
admin.site.register(TechGroup, TechGroupAdmin)
admin.site.register(TechGroupLink, TechGroupLinkAdmin)
