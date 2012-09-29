from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from .widgets import FilteredSelectMultipleWrapper, RelatedFieldWidgetWrapper


class EnhancedAdminMixin(object):
    enhance_exclude = ()
    filtered_multiple_wrapper = FilteredSelectMultipleWrapper
    related_widget_wrapper = RelatedFieldWidgetWrapper

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(EnhancedAdminMixin, self).formfield_for_dbfield(db_field, **kwargs)
        if (formfield and db_field.name not in self.enhance_exclude and
            isinstance(formfield.widget, admin.widgets.RelatedFieldWidgetWrapper)):
            request = kwargs.pop('request', None)
            related_modeladmin = self.admin_site._registry.get(db_field.rel.to)
            if related_modeladmin:
                can_change_related = related_modeladmin.has_change_permission(request)
                can_delete_related = related_modeladmin.has_delete_permission(request)
                if isinstance(formfield.widget.widget, admin.widgets.FilteredSelectMultiple):
                    formfield.widget.widget = self.filtered_multiple_wrapper.wrap(formfield.widget.widget)
                widget = self.related_widget_wrapper.wrap(formfield.widget,
                                                          can_change_related,
                                                          can_delete_related)
                formfield.widget = widget
        return formfield

    def delete_view(self, request, object_id, extra_context=None):
        """ Sets is_popup context variable to hide admin header
        """
        if not extra_context:
            extra_context = {}
        extra_context['is_popup'] = request.REQUEST.get('_popup', 0)
        return super(EnhancedAdminMixin, self).delete_view(request, object_id, extra_context)

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
