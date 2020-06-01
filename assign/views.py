from django.views.generic import FormView, TemplateView
from django.http import (HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404, FileResponse)
from assign.models import QuestionM, AnswerM
from reportlab.pdfgen import canvas
import io


class Question(TemplateView): 
    template_name = 'question.html'
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login/")
        return super(Question, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Question, self).get_context_data(**kwargs)
        context['question'] 
        return context




class Download(TemplateView):

    def post(self, request):
        """
         to download pdf
        """
        if  not request.user.is_authenticated:
            return HttpResponseRedirect('/login/')
        Qs = QuestionM.objects.filter(user=request.user)
        buffer = io.BytesIO()

        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer)

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        buffer.seek(0)
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(100, 100, Qs)

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return FileResponse(buffer, as_attachment=True, filename='question.pdf')
            
        

        

