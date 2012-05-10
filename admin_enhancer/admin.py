
from django.contrib import admin
from django.forms.widgets import SelectMultiple
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from .widgets import RelatedFieldWidgetWrapper


class EnhancedAdminMixin(object):

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(EnhancedAdminMixin, self).formfield_for_dbfield(db_field, **kwargs)
        if (formfield and
            isinstance(formfield.widget, admin.widgets.RelatedFieldWidgetWrapper) and
            not isinstance(formfield.widget.widget, SelectMultiple)):
            request = kwargs.pop('request', None)
            related_modeladmin = self.admin_site._registry.get(db_field.rel.to)
            if related_modeladmin:
                can_change_related = related_modeladmin.has_change_permission(request)
                can_delete_related = related_modeladmin.has_delete_permission(request)
                widget = RelatedFieldWidgetWrapper.from_contrib_wrapper(formfield.widget,
                                                                        can_change_related,
                                                                        can_delete_related)
                formfield.widget = widget
        return formfield

class EnhancedModelAdminMixin(EnhancedAdminMixin):
    
    def response_change(self, request, obj):
        if '_popup' in request.REQUEST:
            return render_to_response('admin_enhancer/dismiss-change-related-popup.html',
                                     {'obj': obj})
        else:
            return super(EnhancedModelAdminMixin, self).response_change(request, obj)
        
    def delete_view(self, request, object_id, extra_context=None):
        delete_view_response = super(EnhancedModelAdminMixin, self).delete_view(request, object_id, extra_context)
        if (request.POST and '_popup' in request.REQUEST and
            isinstance(delete_view_response, HttpResponseRedirect)):
            return render_to_response('admin_enhancer/dismiss-delete-related-popup.html',
                                     {'object_id': object_id})
        else:
            return delete_view_response