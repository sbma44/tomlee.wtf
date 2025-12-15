jQuery(function(){
    alert('ok');
    jQuery('#createbkmklt').click(function(){
        var apikey=jQuery('#apikey').val();
        var bjs="javascript:f=function(){var w=window.open(\"\",\"wildebeast\",\"width=30,height=30,scrollbars=0,resizable=1\");var url=window.location.href;var html='<html><head></head><body><form action=\"https://prowl.weks.net/publicapi/add\" method=\"POST\"><input type=\"hidden\" name=\"apikey\" value=\"" + apikey + "\" /><input type=\"hidden\" name=\"priority\" value=\"0\" /><input type=\"hidden\" name=\"application\" value=\"CTU\" /><input type=\"hidden\" name=\"event\" value=\"Chloe says:\" /><input type=\"hidden\" name=\"description\" value=\"' + url + '\" /></form><script type=\"text/javascript\">document.forms[0].submit();</script></body></html>';w.document.open();w.document.write(html);w.document.close();window.setTimeout(function(){ w.close(); return false;}, 500);};f();";
        var button='<a href="' + bjs + '"><img title="sendittomyscreen" src="http://www.manifestdensity.net/wp-content/uploads/2009/07/sendittomyscreen.png" alt="sendittomyscreen" width="133" height="16" /></a>';
        var b=jQuery(button);
        jQuery('#bkmklt').empty().append(b);
    });
});