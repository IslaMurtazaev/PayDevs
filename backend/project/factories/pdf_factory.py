from project.gen_pdf import PdfGen


class GeneratePdfFactory:
    @staticmethod
    def create():
        return PdfGen()