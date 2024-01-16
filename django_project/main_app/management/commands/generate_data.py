import logging
import random

from django.core.management.base import BaseCommand, CommandParser
from faker import Faker
# import models
from main_app.models import (Event, EventPlatform, Member, MemberInterest,
                             MemberLink, MemberSkill, SkillLevel, TechGroup,
                             TechGroupLink, TechnicalArea)

__version__ = "0.0.1"


class Command(BaseCommand):
    """ """

    help = "Create some test data for the SpokaneTech main app"

    def __init__(self):
        self.opts = None
        self.fake = Faker()
        super(Command, self).__init__()

    def add_arguments(self, parser: CommandParser) -> None:
        """define command arguments"""
        parser.add_argument(
            "--clean",
            action="store_true",
            required=False,
            help="delete existing entries if present before creating new entries",
        )

    def handle(self, *args, **kwargs):
        """command entry point"""
        self.opts = kwargs
        logging.info("Generating test data for the SpokaneTech main app")
        self.generate_technical_areas()
        self.generate_skill_levels()
        self.generate_event_platforms()
        self.generate_tech_groups()
        self.generate_members(15)
        self.generate_events(5)

    def generate_technical_areas(self):
        """ """
        if self.opts.get("clean"):
            logging.info("removing existing TechnicalArea entries")
            TechnicalArea.objects.all().delete()
        logging.info("Generating TechnicalArea entries")
        data_list = [
            {"name": "python", "description": ""},
            {"name": "golang", "description": ""},
            {"name": ".net", "description": ""},
            {"name": "devops", "description": ""},
            {"name": "web development", "description": ""},
            {"name": "cloud", "description": ""},
            {"name": "automation", "description": ""},
            {"name": "networking", "description": ""},
        ]
        for data in data_list:
            TechnicalArea.objects.get_or_create(**data)

    def generate_skill_levels(self):
        """ """
        if self.opts.get("clean"):
            logging.info("removing existing SkillLevel entries")
            SkillLevel.objects.all().delete()
        logging.info("Generating SkillLevel entries")
        data_list = [
            {"name": "beginner", "description": ""},
            {"name": "intermediate", "description": ""},
            {"name": "advanced", "description": ""},
            {"name": "expert", "description": ""},
        ]
        for data in data_list:
            SkillLevel.objects.get_or_create(**data)

    def generate_event_platforms(self):
        """ """
        if self.opts.get("clean"):
            logging.info("removing existing EventPlatform entries")
            EventPlatform.objects.all().delete()
        logging.info("Generating EventPlatform entries")
        data_list = [
            {"name": "meetup"},
            {"name": "eventbright"},
            {"name": "facebook"},
        ]
        for data in data_list:
            EventPlatform.objects.get_or_create(**data)

    def generate_tech_groups(self):
        """ """
        if self.opts.get("clean"):
            logging.info("removing existing TechGroup entries")
            TechGroup.objects.all().delete()
        logging.info("Generating TechGroup entries")
        data_list = [
            {"name": "Spokane Python User Group"},
            {"name": "Spokane Devops"},
            {"name": "LaunchPad INW"},
            {"name": "Spokane Gophers"},
        ]
        for data in data_list:
            group, is_new = TechGroup.objects.get_or_create(
                **data,
                defaults={
                    "description": self.fake.paragraph(),
                    "url": self.fake.url(),
                    "platform": EventPlatform.objects.get_random_row(),
                },
            )
            if is_new:
                for _ in range(random.randint(1, 5)):
                    TechGroupLink.objects.create(
                        group=group, name=self.fake.company(), description=self.fake.paragraph(), url=self.fake.url()
                    )

    def generate_members(self, qty=1):
        """ """
        if self.opts.get("clean"):
            logging.info("removing existing Member entries")
            Member.objects.all().delete()
        logging.info("Generating Member entries")
        for i in range(qty):
            member, is_new = Member.objects.get_or_create(
                first_name=self.fake.first_name(),
                last_name=self.fake.last_name(),
                email=self.fake.email(),
                zip_code=self.fake.zipcode(),
            )
            if is_new:
                for _ in range(random.randint(0, TechnicalArea.objects.count())):
                    skill = {"member": member, "skill": TechnicalArea.objects.get_random_row()}
                    MemberSkill.objects.get_or_create(
                        **skill, defaults={"level": SkillLevel.objects.get_random_row(), "yoe": random.randint(1, 10)}
                    )
                for _ in range(random.randint(0, TechnicalArea.objects.count())):
                    interest = {"member": member, "interest": TechnicalArea.objects.get_random_row()}
                    MemberInterest.objects.get_or_create(**interest, defaults={"interest_level": random.randint(1, 10)})
                for _ in range(random.randint(0, 4)):
                    link = {"member": member, "name": self.fake.company()}
                    MemberLink.objects.get_or_create(
                        **link,
                        defaults={
                            "description": self.fake.paragraph(),
                            "url": self.fake.url(),
                            "is_public": self.fake.boolean(),
                        },
                    )

    def generate_events(self, qty=1):
        """ """
        if self.opts.get("clean"):
            logging.info("removing existing Event entries")
            Event.objects.all().delete()
        logging.info("Generating Event entries")
        for i in range(qty):
            data = dict(
                name=self.fake.catch_phrase(),
                description=self.fake.paragraph(),
                duration=random.randint(1, 5),
                location=self.fake.address(),
                group=TechGroup.objects.get_random_row(),
                date_time=self.fake.future_datetime(),
            )
            event = Event.objects.get_or_create(**data, defaults=data)[0]
            for _ in range(random.randint(1, 5)):
                event.labels.add(TechnicalArea.objects.get_random_row())
