from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import arabic_reshaper
from bidi.algorithm import get_display


def get_filename(filename):
    return filename.upper()


def render_to_pdf(template_src, context_dict=None):
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result, encoding="utf-8")
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
