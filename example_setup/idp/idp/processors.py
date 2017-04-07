from django.contrib.auth.models import Group

from djangosaml2idp.processors import BaseProcessor


class GroupProcessor(BaseProcessor):
    """
        Example implementation of access control for users:
        - superusers are allowed
        - they have to belong to a certain group
    """
    group = "ExampleGroup"

    def has_access(self, user):
        return user.is_superuser or user.groups.filter(name=self.group).exists()