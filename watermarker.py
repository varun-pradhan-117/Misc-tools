import PyPDF2
import sys

inputs=sys.argv[1:]
try:
    original=PyPDF2.PdfFileReader(open(inputs[0],'rb'))
    watermark=PyPDF2.PdfFileReader(open(inputs[1],'rb'))
    output=PyPDF2.PdfFileWriter()
    for i in range(original.getNumPages()):
        page=original.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)        
        with open('watermarked_output.pdf','wb') as file:
            output.write(file)
except IndexError:
    print("Enter Path of two pdf files(Source and Watermark).")
except FileNotFoundError:
    print("Invalid file path.")