django.jQuery(document).ready(function($){
    
    window.dismissChangeRelatedPopup = function(win, objId, newRepr) {
        objId = html_unescape(objId);
        newRepr = html_unescape(newRepr);
        var id = windowname_to_id(win.name).replace(/^edit_/, ''),
            selects = $(interpolate('#%s, #%s_from, #%s_to', [id, id, id]));
        selects.find('option').each(function(){
            if (this.value == objId) this.innerHTML = newRepr;
        });
        win.close();
    };
    
    if (!dismissAddAnotherPopup.original) {
        var originalDismissAddAnotherPopup = dismissAddAnotherPopup;
        dismissAddAnotherPopup = function(win, newId, newRepr) {
            originalDismissAddAnotherPopup(win, newId, newRepr);
            newId = html_unescape(newId);
            newRepr = html_unescape(newRepr);
            $('#' + windowname_to_id(win.name)).trigger('change');
        };
        dismissAddAnotherPopup.original = originalDismissAddAnotherPopup;
    }
    
    window.dismissDeleteRelatedPopup = function(win, objId) {
        objId = html_unescape(objId);
        var id = windowname_to_id(win.name).replace(/^delete_/, ''),
            selects = $(interpolate('#%s, #%s_from, #%s_to', [id, id, id]));
        selects.find('option').each(function(){
            if (this.value == objId) $(this).remove();
        }).trigger('change');
        win.close();
    };
    
	var relatedWidgetCSSSelector = '.related-widget-wrapper-change-link, .related-widget-wrapper-delete-link',
  		hrefTemplateAttr = 'data-href-template';
  
    $('#container').delegate('.related-widget-wrapper', 'change', function(event){
        var siblings = $(this).nextAll(relatedWidgetCSSSelector),
            value = event.target.value;
        if (!siblings.length) return;
        if (value) {
	       siblings.each(function(){
		      var elm = $(this);
		      elm.attr('href', elm.attr(hrefTemplateAttr).replace('__pk__', value));
	       });
        } else siblings.removeAttr('href');
    });

	$('#container').delegate('.related-widget-wrapper-link', 'click', function(event){
    	if (this.href) {
    		return showAddAnotherPopup(this);
    	} else return false;
    });
});
