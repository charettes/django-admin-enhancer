
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class RelatedFieldWidgetWrapper(RelatedFieldWidgetWrapper):
    
    class Media:
        css = {
            'screen': ('admin_enhancer/css/related-widget-wrapper.css',)
        }
        js = ('admin_enhancer/js/related-widget-wrapper.js',)
    
    def __init__(self, *args, **kwargs):
        self.can_change_related = kwargs.pop('can_change_related', None)
        self.can_delete_related = kwargs.pop('can_delete_related', None)
        super(RelatedFieldWidgetWrapper, self).__init__(*args, **kwargs)
    
    @classmethod
    def from_contrib_wrapper(cls, wrapper, can_change_related, can_delete_related):
        return cls(wrapper.widget, wrapper.rel, wrapper.admin_site,
                   can_add_related=wrapper.can_add_related,
                   can_change_related=can_change_related,
                   can_delete_related=can_delete_related)
    
    def get_related_url(self, rel_to, info, action, args=[]):
        return reverse("admin:%s_%s_%s" % (info + (action,)),
                       current_app=self.admin_site.name, args=args)
    
    def render(self, name, value, attrs={}, *args, **kwargs):
        rel_to = self.rel.to
        info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
        self.widget.choices = self.choices
        attrs['class'] = ' '.join((attrs.get('class', ''), 'related-widget-wrapper'))
        context = {'widget': self.widget.render(name, value, attrs, *args, **kwargs),
                   'name': name,
                   'can_change_related': self.can_change_related,
                   'can_add_related': self.can_add_related,
                   'can_delete_related': self.can_delete_related,}
        if self.can_change_related:
            if value:
                context['change_url'] = self.get_related_url(rel_to, info, 'change', [value])
            template = self.get_related_url(rel_to, info, 'change', ['%s'])
            context.update({'change_url_template': template,
                            'change_help_text': _(u'Change related model'),})
        if self.can_add_related:
            context.update({'add_url': self.get_related_url(rel_to, info, 'add'),
                            'add_help_text': _(u'Add another'),})
        if self.can_delete_related:
            if value:
                context['delete_url'] = self.get_related_url(rel_to, info, 'delete', [value])
            template = self.get_related_url(rel_to, info, 'delete', ['%s'])
            context.update({'delete_url_template': template,
                            'delete_help_text': _(u'Delete related model'),})
        
        return mark_safe(render_to_string('admin_enhancer/related-widget-wrapper.html', context))
