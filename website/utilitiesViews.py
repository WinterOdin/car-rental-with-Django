from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from xhtml2pdf import pisa
from io import BytesIO
from .models import *
from itertools import chain

def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None



#Opens up page as PDF
class ViewPDF(View):
	def get(self,  request,pk, *args, **kwargs):
		rawData=Order.objects.get(id=pk)
		cleanData = to_dict(rawData)
		context={
			'cleanData':cleanData
		}
		pdf = render_to_pdf('pdfInvoice.html', context)
		
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request,pk, *args, **kwargs):
		rawData=Order.objects.get(id=pk)
		cleanData = to_dict(rawData)

		pdf = render_to_pdf('pdfInvoice.html', cleanData)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

