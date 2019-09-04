# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-09-03 21:57
# @Author  : lidong@immusician.com
# @Site    : 
# @File    : PDFParsing.py
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.converter import PDFPageAggregator, HTMLConverter


class Parser(object):
    def __init__(self, pdf_path, save_path, password=""):
        self._pdf_path = pdf_path
        self._fp = self.get_file_handles()
        self.save_path = save_path
        self.pdf_parser = PDFParser(self._fp)
        self.pdf_document = PDFDocument()

        self.pdf_parser.set_document(self.pdf_document)
        self.pdf_document.set_parser(self.pdf_parser)

        self.pdf_document.initialize(password=password)

        self.is_extractable()
        self.rsrc_manager = PDFResourceManager()
        self.la_params = LAParams()

        self.device = PDFPageAggregator(self.rsrc_manager, laparams=self.la_params)
        # 创建一个PDF解释器对象
        self.interpreter = PDFPageInterpreter(self.rsrc_manager, self.device)

        self.pages = self.pdf_document.get_pages()

    def get_file_handles(self):
        fp = open(self._pdf_path, "rb")
        return fp

    # @property
    def is_extractable(self):
        if self.pdf_document.is_extractable:
            return self.pdf_document.is_extractable
        raise PDFTextExtractionNotAllowed

    def parsing(self):
        for page in self.pages:
            self.interpreter.process_page(page)
            # 接收该页面的LTPage对象
            layout = self.device.get_result()
            # 这里的layout是一个LTPage对象 里面存放着page解析出来的各种对象
            # 一般包括LTTextBox，LTFigure，LTImage，LTTextBoxHorizontal等等一些对像
            # 想要获取文本就得获取对象的text属性
            for x in layout:
                try:
                    if isinstance(x, LTTextBoxHorizontal):
                        with open(self.save_path, 'a') as f:
                            result = x.get_text()
                            print(result)
                            f.write(result + "\n")
                except Exception as e:
                    print("Failed" + str(e))

    def close_fp(self):
        self._fp.close()


if __name__ == '__main__':
    parser = Parser("./PDFS/04747Java.pdf", "./demo1.txt")
    # print(list(parser.pages))
    print(parser.parsing())
    parser.close_fp()
