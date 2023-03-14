 // Used to add a spinner to submit buttons
var temp_button_text;
function CustomFormSubmitPost(e) {
    var el = $(e);
    temp_button_text = el.text()
    el.attr('disabled', 'disabled').text("").append('<class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Loading...');
};
function CustomFormSubmitResponse(e) {
    var el = $(e);
    el.removeAttr('disabled').text(temp_button_text);
};

function getSubmitButton(form){
    return form.find(":submit")
}


var DemoFunctions = function(){
	
	"use strict"
	
    var basicForm = function (){
        var form = $('#basicform')
        var submit_button = getSubmitButton(form)
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost(submit_button);
            var formdata = new FormData(form[0]); 
            var submit_button = getSubmitButton(form)
			$.ajax({
				url: form.attr("action"),
				method: form.attr("method"),
				data: data,
				success: function(json){
					CustomFormSubmitResponse(submit_button);
					var result = "Success"
					var message = json["message"]
					$('.modal').modal('hide');

					ShowAlert(result, json["message"], result.toLowerCase(), json["redirect"]);

				},
				error: function(json){
					CustomFormSubmitResponse(submit_button);
					var result = "Error"
					var message = json["message"]
					ShowAlert(result, json.responseJSON["message"], result.toLowerCase(), json.responseJSON["redirect"]);
					console.log(json.status + ": " + json.responseText);
				}
			})
        });
    };

	/* Function ============ */
	return {
		init:function(){
			basicForm();
		},
	}
	
}();

/* Document.ready Start */	
jQuery(document).ready(function() {
    'use strict';
	DemoFunctions.init();
	
});

$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    $.ajaxSetup({
        beforeSend: function(json, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                json.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
})
