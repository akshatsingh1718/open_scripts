import requests
from django.shortcuts import render
from .forms import URLForm, ContributionForm
from .utils.contribuiton import contrib_response

APP = "linkedin"


def index(request):
    return render(
        request,
        f"{APP}/index.html",
    )


def contribution_from_text(request):
    submitted_data = None
    if request.method == "POST":
        form = ContributionForm(request.POST)
        if form.is_valid():
            # Capture the cleaned data
            submitted_data = {
                "heading": form.cleaned_data["heading"],
                "subheading": form.cleaned_data.get("subheading"),
                "reference_text": form.cleaned_data["reference_text"],
            }
            contrib_resp = contrib_response(**submitted_data)
            response = contrib_resp["response"]
            llm_input = contrib_resp["llm_input"]

            print("=" * 40)
            print(response)
            submitted_data["response"] = response.content
            submitted_data["llm_input"] = llm_input

    else:
        form = ContributionForm()

    return render(
        request,
        f"{APP}/contribution_from_text.html",
        {"form": form, "submitted_data": submitted_data},
    )


def contribution_from_link(request):
    data = None
    error = None
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            try:
                response = requests.get(url)
                print(response)
                response.raise_for_status()
                data = response.text  # Fetch the content of the page
            except requests.RequestException as e:
                error = f"Failed to fetch data: {e}"
    else:
        form = URLForm()

    return render(
        request,
        f"{APP}/contribution_from_link.html",
        {"form": form, "data": data, "error": error},
    )
