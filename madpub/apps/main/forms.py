# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from html5 import forms
from . import models


class HTML5FormMixin(object):
    def as_div(self):
        '''Returns this form rendered as HTML <div>s, optimized for jQuery
        Mobile.
        '''
        return self._html_output(normal_row=u'<div%(html_class_attr)s data-role="fieldcontain">%(label)s %(field)s%(help_text)s</div>',
                                 error_row=u'%s',
                                 row_ender='</div>',
                                 help_text_html=u' <span class="help-text">%s</span>',
                                 errors_on_separate_row=True)


class ResponderContactForm(ModelForm, HTML5FormMixin):

    class Meta:
        model = models.Residence
        fields = (
            'preferred',
            'first_name',
            'middle_name',  # not sure if that's still there
            'last_name',
            'street1',
            'street2',
            'city',
            'county',
            'postcode',
            'phone',
            'phone_extension',
            'cell',
            'provider',
            'contact_email',
            'contact_email2',
        )


class ResidenceOwnerForm(ModelForm, HTML5FormMixin):

    class Meta:
        model = models.Residence
        fields = (
            'owner',
        )


class DamagesDateLocationForm(ModelForm, HTML5FormMixin):

    damage_location = forms.ChoiceField(choices=(
        ('contact', _(u'At contact address')),
        ('geolocation', _(u'Use my current location (if supported by browser)')),
        ('new', _('Different address')),
    ))
    # TODO add address fields

    class Meta:
        model = models.Residence
        fields = (
            'date',
        )


class DamagesDetailsForm(ModelForm, HTML5FormMixin):

    # TODO pictures
    # TODO accessible buttons in template

    class Meta:
        model = models.Residence
        fields = (
            'damage',
            'cause',
            'description',
            'location',
        )


class ResidenceDamagesDetailsForm(ModelForm, HTML5FormMixin):

    class Meta:
        model = models.Residence
        fields = (
            'habitable',
            'estperproploss',
            'eststructloss',
        )


class FEMAForm(ModelForm, HTML5FormMixin):

    class Meta:
        model = models.Residence
        fields = (
            'fema',
            'reference',
        )


class InsuranceForm(ModelForm, HTML5FormMixin):

    class Meta:
        model = models.Residence
