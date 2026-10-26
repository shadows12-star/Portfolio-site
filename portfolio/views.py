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
        "project_sections": [
            {
                "id": "frontend-projects",
                "title": "Frontend Projects",
                "description": "Responsive interfaces and frontend experiences.",
                "projects": [p for p in PROJECTS if p.get("category") == "Frontend"],
            },
            {
                "id": "backend-projects",
                "title": "Backend Projects",
                "description": "Server-side applications, APIs, and data-driven web systems.",
                "projects": [p for p in PROJECTS if p.get("category") == "Backend"],
            },
            {
                "id": "ai-ml-projects",
                "title": "AI/ML Projects",
                "description": "Machine learning, deep learning, and intelligent applications.",
                "projects": [p for p in PROJECTS if p.get("category") == "AI/ML"],
            },
        ],
        "learning_now": LEARNING_NOW,
        "education": EDUCATION,
        "languages": LANGUAGES,
        "certifications": CERTIFICATIONS,
    }
    return render(request, "portfolio/home.html", context)