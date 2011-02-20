# -*- coding: utf-8 -*-

from datetime import date
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Residence(models.Model):
    '''Model for the primary residence form.'''

    # responder contact
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(blank=True, max_length=256)
    last_name = models.CharField(max_length=256)
    street1 = models.CharField(help_text=_('Street address 1'), max_length=256)
    street2 = models.CharField(blank=True, help_text=_('Street address 2'), max_length=256)
    city = models.CharField(max_length=256)
    county = models.CharField(max_length=5)  # FIPS code
    state = USStateField()
    postcode = models.CharField(help_text=_('ZIP'), max_length=10)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    # residence info
    owner = models.BooleanField(help_text=_('Are you an owner?'), default=True)
    estpredistfmv = models.PositiveIntegerField(help_text=_('Estimated Pre-Disaster FMV of STRUCTURE'))
    date = models.DateField(help_text=_('Date of Damage'), default=date.today)

    # damages
    eststructloss = models.PositiveIntegerField(help_text=_('Estimated STRUCTURE Loss in $$'))
    estperproploss = models.PositiveIntegerField(help_text=_('Estimated PERSONAL PROPERTY Loss in $$'))
    cause = models.CharField(choices=(
        ('flood', _('Flood')),
        ('fire', _('Fire')),
        ('wind', _('Wind')),
        ('earthquake', _('Earthquake')),
        ('volcano', _('Volcano')),
        ('snow_ice', _('Snow/Ice')),
        ('vandalism', _('Vandalism')),
        ('other', _('Other')),
    ), help_text=_('Primary Cause of Damage'), max_length=256)
    habitable = models.BooleanField(default=True)
    accessible = models.BooleanField(default=True)
    damage = models.CharField(choices=(
        ('structural', _('Structural')),
        ('roadway', _('Roadway')),
        ('land', _('Land')),
    ), help_text=_('Category of Damage'), max_length=256)
    description = models.TextField(help_text=_('Description of Damages'))
    location = models.TextField(help_text=_('Damage Location Description'))
    uninsured_loss = models.IntegerField(help_text=_('Total Uninsured Loss'))

    # insurance
    insurance = models.BooleanField(default=True, help_text=_('Do you have insurance?'))
    insurance_type = models.CharField(blank=True, help_text=_('Type of Insurance'), max_length=256)
    insurance_provider = models.CharField(max_length=256)
    deductible = models.IntegerField()

    # response
    fema = models.BooleanField(help_text=_('Have you started a FEMA application?'))
    reference = models.PositiveIntegerField(blank=True, help_text=_('What is your FEMA reference number?'))
    contact = models.CharField(blank=True, help_text=_('Contact Name'), max_length=256)
    preferred = models.CharField(choices=(
        ('phone', _('Landline phone')),
        ('cell', _('Cell phone')),
        ('email', _('E-mail')),
        ('snail', _('Postal mail')),
    ), help_text=_('Preferred method of contact'), max_length=10)
    phone = PhoneNumberField(blank=True, help_text=_('Contact phone'))
    phone_extension = models.CharField(blank=True, max_length=20)
    cell = PhoneNumberField(blank=True, help_text=_('Contact cell'))
    provider = models.CharField(blank=True, help_text=_('Cell provider'), max_length=256)
    contact_email = models.EmailField(blank=True)
    contact_email2 = models.EmailField(blank=True, help_text=_('Second contact email'))


class ResidenceImage(models.Model):
    residence = models.ForeignKey(Residence)
    image = models.ImageField(upload_to='residences')
