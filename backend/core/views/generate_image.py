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
from core.forms import AnimalForm

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

class GenerateImageView(generic.FormView):
    """
    FormView used for our generate image page.

    **Template:**

    :template:`generate_image.html`
    """
    template_name = "generate_image.html"
    form_class = AnimalForm
    success_url = "/"

    def generate_prompt(self, breed):
        return 'Suggest three names for an animal that is a superhero.'

    @method_decorator(ajax_required)
    def post(self, request,*args, **kwargs):
        data = {'result': 'Error', 'message': "Something went wrong, please try again", "redirect": False, "data":None}
        form = AnimalForm(request.POST)
        if form.is_valid():

            breed = form.cleaned_data.get("breed")

            response = openai.Image.create(
                prompt=breed,
                n=1,
                size="1024x1024"
            )
            print(response)
            print(response['data'][0]['url'])
            data.update({
                'result': "Success",
                'message': "ChatGPT has created this image",
                'data': response['data'][0]['url']
            })
            return JsonResponse(data)

        else:
            data["message"] = FormErrors(form)
            return JsonResponse(data, status=400)
