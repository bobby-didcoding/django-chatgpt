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

class HomeView(generic.FormView):
    """
    FormView used for our home page.

    **Template:**

    :template:`index.html`
    """
    template_name = "index.html"
    form_class = AnimalForm
    success_url = "/"

    def generate_prompt(self, breed):
        return f'Suggest three {breed} animal names'

    @method_decorator(ajax_required)
    def post(self, request,*args, **kwargs):
        data = {'result': 'Error', 'message': "Something went wrong, please try again", "redirect": False, "data":None}
        form = AnimalForm(request.POST)
        if form.is_valid():

            breed = form.cleaned_data.get("breed")

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=breed,
                temperature=0.6,
            )
            data.update({
                'result': "Success",
                'message': "ChatGPT has suggested some names",
                'data': list(filter(None,response.choices[0].text.splitlines( )))
            })
            return JsonResponse(data)

        else:
            data["message"] = FormErrors(form)
            return JsonResponse(data, status=400)
