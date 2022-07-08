import PyPDF2
fhandle = open('campsites.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(fhandle)
pagehandle = pdfReader.getPage(0)
print(pagehandle.extractText())