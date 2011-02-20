$(function () { // vim: set ts=2 sts=2 sw=2 :
  $.support.formPlaceholder = ('placeholder' in document.createElement('input'));
  $('form div.ui-field-contain[class!="image-upload"][class!="button"]').each(function () {
    var helptext, input, label, div, text;
    div = jQuery(this);
    helptext = div.children('span.help-text');
    label = div.children('label');
    if (helptext.length != 0) {
      label.text(helptext.text() + ":");
    }
    helptext.remove();
    // TODO use some jQuery placeholder plugin (probably self-written)
    if ($.support.formPlaceholder) {
      text = label.text();
      text = text.substr(0, text.length - 1);
      input = div.children('input');
      if (input.length > 0) {
        input.attr('placeholder', text);
        label.remove();
      } else {
        var select = div.find('select');
        if (select.length > 0) {
          text = '---- ' + text + ' ----';
          var fix_jqm = function () {
            var that = $(this);
            if (that.text() == '---------') {
              that.text(text);
            }
          };
          select.children('option[value=""]').text(text);
          $('#' + label.attr('for') + '-menu a[role="option"]:first').each(fix_jqm);
          $('#' + label.attr('for') + '-button .ui-btn-text:first').each(fix_jqm);
          label.remove();
        }
      }
    }
  });
  $('form').validator();
  $('#responder-contact-next button').click(function (evt) {
    if (this.form.checkValidity()) {
      evt.preventDefault();
      // TODO save to evercookie?
      if ($(this).val() == 'business') {
        alert('business is not done yet');
      } else {
        window.location.hash = '#residence-owner';
      }
    }
    return false;
  });/*
  // responder contact form specific
  function hide_all() {
    $('#responder-contact-form input:not(type="submit"):not(#id_first_name):not(#id_middle_name):not(#id_last_name):not(#id_county)').hide();
  }
  function update_fields(dropdown) {
    var field_map;
    if (!dropdown || !dropdown.val) {
      dropdown = $(this);
    }
    field_map = {
      '': [],
      'cell': ['cell', 'provider'],
      'email': ['contact_email', 'contact_email2'], 
      'phone': ['phone', 'phone_extension'],
      'snail': ['street1', 'street2', 'city', 'state', 'postcode']
    };
    hide_all();
    $.each(field_map[dropdown.val()], function () {
      $('#id_' + this).show();
    });
  }
  var preferred = $('#responder-contact-form #id_preferred');
  preferred.change(update_fields);
  update_fields(preferred);*/
});
