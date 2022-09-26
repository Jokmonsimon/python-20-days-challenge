# Creating PDF Files with Python

# Why PDF?
# PDF file format is global. It is one of the most common file formats in use today and extensively used in all areas.
# It is portable. Yes! PDF stands for Portable Document Format. You can move your files around without having to worry about any restrictions.
# It is a platform-independent tool. It is independent of the hardware and the operating system. You can create your pdf files in Windows and view them in a Macintosh or Unix.
# It can be used offline. You don’t even need an internet connection.
# The ease of generation. There are many different ways to create a PDF file. Our purpose is to learn how to do it with Python.

# Import fpdf class
from fpdf import FPDF

class PDF(FPDF):
    pass # Nothing happens when it is executed

    # Create an object of the PDF class
pdf = PDF()
    # Set page orientation
    # Set unit measurement
    # Set page format
pdf = PDF(orientation='P', unit='mm', format='A4')

    # Add Page and save the output
pdf.add_page()
pdf.output('yearn_ai.pdf', 'F')



