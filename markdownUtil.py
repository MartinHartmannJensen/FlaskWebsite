from misaka import HtmlRenderer, HtmlTocRenderer
from flask_misaka import markdown
from flask import render_template

#class MarkdownGenerator:

#    def __init__(self, markdownDoc):
#        self.document = "markdown/" + markdownDoc
#        self.tocRen = Markdown(HtmlTocRenderer(3))
#        self.docRen = Markdown(HtmlRenderer(0, 3), ["EXT_FENCED_CODE", "EXT_QUOTE"])

#    def Toc(self):
#        return self.tocRen(render_template(self.document))

#    def Doc(self):
#        return self.docRen(render_template(self.documen


class MarkdownGenerator:

    def __init__(self, markdownDoc):
        self.document = "markdown/" + markdownDoc
        self.tocRen = HtmlTocRenderer(3)
        self.docRen = HtmlRenderer(0, 3)

    def Toc(self):
        return markdown(render_template(self.document), self.tocRen)

    def Doc(self):
        return markdown(render_template(self.document), self.docRen, fenced_code=True, qoute=True, tables=True)