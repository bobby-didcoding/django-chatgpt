# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic


class HomeView(generic.TemplateView):
    """
    TemplateView used for our home page.

    **Template:**

    :template:`index.html`
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f'Home'
        return context
    

# import os

# import openai
# from flask import Flask, redirect, render_template, request, url_for

# app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")


# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))

#     result = request.args.get("result")
#     return render_template("index.html", result=result)