from io import BytesIO
from reportlab.pdfgen import canvas



class PdfGen:
    def create_pdf(self, project):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        height = 700
        p.drawString(200, 800, "Project total report bill")

        p.drawString(150, height, "%s:  %s" % ("User", project.user))
        height -= 25
        p.drawString(150, height, "%s:  %s" % ("Title", project.title))
        height -= 25
        p.drawString(150, height, "%s:  %s" % ("Description", project.description))
        height -= 25
        p.drawString(150, height, "%s:  %s" % ("Type of payment", project.type_of_payment_pdf))
        height -= 25
        p.drawString(150, height, "%s:  %s" % ("Start date project", project.start_date))
        height -= 25
        p.drawString(150, height, "%s:  %s" % ("End date project", project.end_date))
        height -= 25
        p.drawString(150, height, "%s:  %s" % ("End date project", project.end_date))
        height -= 25
        p.drawString(150, height, "%s:  %s" % ("Total", project.total))
        height -= 25
        p.showPage()
        p.save()
        pdf = buffer.getvalue()
        buffer.close()
        return pdf