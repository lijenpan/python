from django.utils import timezone
from django.db import models

class User(models.Model):
  internal_id = models.CharField(max_length=25, blank=True, null=True)
  verified = models.BooleanField(blank=False, null=False, default=False)
  approval_date = models.DateTimeField('date approved')

class Link(models.Model):
  name = models.CharField(max_length=50, null=False, blank=False)
  link = models.URLField(null=False, blank=False)
  date_created = models.DateTimeField('date created')
  date_modified = models.DateTimeField('date modified')
  tags = models.TextField(null=True, blank=True)

  def __unicode__(self):
    return self.name

  def update_modified_date(self):
    self.date_modified = timezone.now()

class List(models.Model):
  name = models.CharField(max_length=50, null=False, blank=False)
  date_created = models.DateTimeField('date created')
  date_modified = models.DateTimeField('date modified')
  links = models.ManyToManyField(Link)

  def __unicode__(self):
    return self.name

  def update_modified_date(self):
    self.date_modified = timezone.now()
