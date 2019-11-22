from django.db import models

# Create your models here.

class Agent(models.Model):
    agent_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    cash_inflow = models.BigIntegerField()
    cash_outflow = models.BigIntegerField()
    daily_transaction = models.BigIntegerField()
    internal_branding_photo = models.ImageField(upload_to='internal_branding', blank=True)
    external_branding_photo = models.ImageField(upload_to='external_branding', blank=True)
    tariffs_display_photo = models.ImageField(upload_to='tarrifs_photo', blank=True)

    def __str__(self):
            return self.agent_name