# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.conf import settings

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.forms import InputForm

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import ajax_required
from utils.mixins import FormErrors

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
import openai

openai.api_key = settings.OPENAI_API_KEY

class GenerateLogoView(generic.FormView):
    """
    FormView used for our generate logo page.

    **Template:**

    :template:`generate_logo.html`
    """
    template_name = "generate_logo.html"
    form_class = InputForm
    success_url = "/"

    @method_decorator(ajax_required)
    def post(self, request,*args, **kwargs):
        data = {'result': 'Error', 'message': "Something went wrong, please try again", "redirect": False, "data":None}
        form = InputForm(request.POST)
        if form.is_valid():

            input = form.cleaned_data.get("input")

            response = openai.Image.create(
                prompt=input,
                n=1,
                size="1024x1024"
            )
            data.update({
                'result': "Success",
                'message': "ChatGPT has created this logo",
                'data': response['data'][0]['url']
            })
            return JsonResponse(data)

        else:
            data["message"] = FormErrors(form)
            return JsonResponse(data, status=400)
