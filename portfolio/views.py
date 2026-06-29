from django.shortcuts import render
from .data import (
    PROFILE,
    TECH_STACK,
    FOCUS_AREAS,
    PROJECTS,
    LEARNING_NOW,
    EDUCATION,
    LANGUAGES,
    CERTIFICATIONS,
)


def home(request):
    context = {
        "profile": PROFILE,
        "tech_stack": TECH_STACK,
        "focus_areas": FOCUS_AREAS,
        "projects": PROJECTS,
        "learning_now": LEARNING_NOW,
        "education": EDUCATION,
        "languages": LANGUAGES,
        "certifications": CERTIFICATIONS,
    }
    return render(request, "portfolio/home.html", context)