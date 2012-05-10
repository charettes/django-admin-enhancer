django.jQuery(document).ready(function($){
    
    window.dismissChangeRelatedPopup = function(win, objId, newRepr) {
        objId = html_unescape(objId);
        newRepr = html_unescape(newRepr);
        var id = windowname_to_id(win.name).replace(/^edit_/, ''),
            $elem = $('#' + id);
        $elem.find('option').each(function(){
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
            $elem = $('#' + id);
        $elem.find('option').each(function(){
            if (this.value == objId) $(this).remove();
        }).trigger('change');
        win.close();
    };
    
	var relatedWidgetCSSSelector = '.related-widget-wrapper-change-link, .related-widget-wrapper-delete-link',
  		hrefTemplateAttr = 'data-href-template';
  
    $('.related-widget-wrapper').live('change', function(){
        var siblings = $(this).nextAll(relatedWidgetCSSSelector);
        if (!siblings.length) return;
        if (this.value) {
	       var val = this.value;
	       siblings.each(function(){
		      var elm = $(this);
		      elm.attr('href', interpolate(elm.attr(hrefTemplateAttr), [val]));
	       });
        } else siblings.removeAttr('href');
    });
	
	$('.related-widget-wrapper-link').live('click', function(){
    	if (this.href) {
    		return showAddAnotherPopup(this);
    	} else return false;
    });
});
