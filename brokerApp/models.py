from django.db import models

# Create your models here.
class ServiceRecord(models.Model):
    """
    Service Model - defining the attributes
    """
    service_id = models.CharField(max_length=100)
    plan_id = models.CharField(max_length=100)
    organization_guid = models.CharField(max_length=100)
    space_guid = models.CharField(max_length=100)

    def __repr__(self):
        return self.service_instance_id + ' is added.'
