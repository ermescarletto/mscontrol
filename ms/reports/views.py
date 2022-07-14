import functools
import entidades.models as emd
from django.conf import settings
from django.views.generic import DetailView

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import WeasyTemplateResponse, WeasyTemplateView


class MyDetailView(DetailView):
    # vanilla Django DetailView
    template_name = 'relatorio_ambiente.html'

class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    # customized response class to change the default URL fetcher
    def get_url_fetcher(self):
        # disable host and certificate check
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)

class PrintView(WeasyTemplateResponseMixin, MyDetailView):
    # output of MyDetailView rendered as PDF with hardcoded CSS

    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # custom response class to configure url-fetcher
    response_class = CustomWeasyTemplateResponse

class DownloadView(WeasyTemplateResponseMixin, MyDetailView):
    # suggested filename (is required for attachment/download!)
    pdf_filename = 'foo.pdf'

class DynamicNameView(WeasyTemplateResponseMixin, MyDetailView):
    # dynamically generate filename
    def get_pdf_filename(self):
        return 'foo-{at}.pdf'.format(
            at=timezone.now().strftime('%Y%m%d-%H%M'),
        )



class ChecklistsAmbientes(WeasyTemplateView):
    template_name='relatorio_ambiente.html'

    def get(self, request, ambiente_id, *args, **kwargs):
        ambiente = emd.Ambiente.objects.filter(pk=ambiente_id)
        context = self.get_context_data(**kwargs)
        context['ambiente'] = ambiente
        return self.render_to_response(context)
