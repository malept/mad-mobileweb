# -*- coding: utf-8 -*-

from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
from .forms import DamagesDateLocationForm, DamagesDetailsForm, FEMAForm, InsuranceForm, ResidenceDamagesDetailsForm, ResidenceOwnerForm, ResponderContactForm


def success(request):
    return TemplateResponse(request, 'main/success.html')


def wizard(request):
    return TemplateResponse(request, 'main/wizard.html', {
        'forms': [
            {
                'extra': u'''\
<fieldset id="responder-contact-next" class="button" data-role="fieldcontain">
    <button type="button" name="form_type" value="business">%s</button>
    <button type="button" name="form_type" value="residence">%s</button>
</fieldset>''' % (_(u'Business'), _('Residence')),
                'form': ResponderContactForm(),
                'id': 'responder-contact',
                'title': 'Responder Contact',
            },
            {
                'extra': u'''\
<fieldset class="button" data-role="fieldcontain">
    <button type="button">%s</button>
</fieldset>''' % u'Next',
                'form': ResidenceOwnerForm(),
                'id': 'residence-owner',
                'title': 'Residence Owner',
            },
            {
                'form': DamagesDateLocationForm(),
                'id': 'damages-date-location',
                'title': 'Damages: Date & Location',
            },
            {
                'form': DamagesDetailsForm(),
                'id': 'damages-details',
                'title': 'Damages: Details',
            },
            {
                'form': ResidenceDamagesDetailsForm(),
                'id': 'residence-damages-details',
                'title': 'Damages: Details (Residence)',
            },
            {
                'form': FEMAForm(),
                'id': 'fema',
                'title': 'FEMA',
            },
            {
                'form': InsuranceForm(),
                'id': 'insurance',
                'title': 'Insurance',
            },
        ]
    })
