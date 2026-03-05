from django.shortcuts import render


def index(request):
    """Render a simple landing page for the blog app."""
    return render(request, "blog/index.html", {"title": "FinTech Blog"})
