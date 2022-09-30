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
    # Create a line method to draw a line in the middle of the page
    def line(self):
        # Set line width to 0.0 mm
        self.set_line_width(0.0) 

        # Draw a simple line with four arguments: line(x1, y1, x2, y2)
        self.line(0, pdf_height/2, 210, pdf_height/2)

# Create an object of the PDF class with Defualt A4 Format
pdf = PDF() 

# Set page orientation
# Set unit measurement
# Set page format
pdf = PDF(orientation='P', unit='mm', format='A4')

    # Add Page and save the output
pdf.add_page() # add.page function adds a new page to the document.
pdf.output('python-notes.pdf', 'F')

# PyFPDF is built on the coordinate space (x,y)
# The default value of orientation is ‘A4’
# The size of A4 is: w:210 mm and h:297 mm

# Assign size of A4 dimensions to variables for later use
pdf_width = 210
pdf_height = 297


