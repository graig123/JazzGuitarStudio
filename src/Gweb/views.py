from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class ChordsPage(generic.TemplateView):
    template_name = "chords.html"


class ScalesPage(generic.TemplateView):
    template_name = "scales.html"
