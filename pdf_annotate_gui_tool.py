import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# import pandas as pd0
import PyPDF2
import os,sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
import io

root= tk.Tk()
root.geometry("300x500")
root.title("PDF Annotator V 1.0")
#canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
#canvas1.pack()


label1 = tk.Label(root, text='PDF Conversion Tool')
label1.config(font=('helvetica', 18))
#canvas1.create_window(150, 60, window=label1)
label1.grid(row=0)

label2 = tk.Label(root, text='----------------------')
label2.grid(row=1)


def getpdf ():
    global import_file_path, input_pdffile_reader
    
    import_file_path = filedialog.askopenfilename(title="Select Exome report PDF", initialdir = "/home/it/Desktop/",filetypes=(("pdf files","*.pdf"),("all files", "*.*")))
    input_pdffile_conn = open(import_file_path, 'rb')
    txtbox.insert(0.0, "PDF File name :" + import_file_path + " Selected\n\n")
    # open input pdf file pypdf reader connection
    input_pdffile_reader = PyPDF2.PdfFileReader(input_pdffile_conn)
    
browseButton_pdf = tk.Button(root ,text="      Import PDF File     ", command=getpdf, bg='green', fg='white', font=('helvetica', 12, 'bold'))
#canvas1.create_window(150, 130, window=browseButton_Excel)
browseButton_pdf.grid(row=2)

txtbox = tk.Text(root, width=41, height=35)
txtbox.grid(row=3)

txtbox.insert(0.0, "Welcome to PDF Annotator\n")
def annotpdf():
    
    txtbox.insert(0.0, "PDF File annotation started\n\n")
    print(input_pdffile_reader.getDocumentInfo())
    input_pdffile_total_page = input_pdffile_reader.getNumPages()
    print(input_pdffile_total_page)
    
    output_pdffile_name = os.path.basename(import_file_path)
    temp_name = output_pdffile_name.split(".")
    output_pdffile_name = temp_name[0] + "_With_page_no.pdf"
    print( "New file name : "+ output_pdffile_name)
    output_pdffile_conn = open( os.path.dirname(import_file_path)+ "/" + output_pdffile_name, 'wb')
    out_pdffile_writer = PyPDF2.PdfFileWriter()

    # intermidiate_pdffile = io.BytesIO()
    # intermidiate_pdffile_canvas = Canvas(intermidiate_pdffile, pagesize = A4)
    # intermidiate_pdffile_canvas.drawString(6.9 * inch, 0.5 * inch, "page number 1")
    # intermidiate_pdffile_canvas.save()
    # intermidiate_pdffile.seek(0)
    # intermidiate_pdffile_reader = PyPDF2.PdfFileReader(intermidiate_pdffile)

    # input_pdffile_reader_page = input_pdffile_reader.getPage(0)
    # input_pdffile_reader_page.mergePage(intermidiate_pdffile_reader.getPage(0))
    
    for i in range(input_pdffile_reader.getNumPages()):
        
        intermidiate_pdffile = io.BytesIO()
        intermidiate_pdffile_canvas = Canvas(intermidiate_pdffile, pagesize = A4)
        intermidiate_pdffile_canvas.drawString(6.9 * inch, 0.2 * inch, "Page " + str(i+1) + " of " + str(input_pdffile_total_page))
        intermidiate_pdffile_canvas.save()
        intermidiate_pdffile.seek(0)
        intermidiate_pdffile_reader = PyPDF2.PdfFileReader(intermidiate_pdffile)
        input_pdffile_reader_page = input_pdffile_reader.getPage(i)
        input_pdffile_reader_page.mergePage(intermidiate_pdffile_reader.getPage(0))
        out_pdffile_writer.addPage(input_pdffile_reader_page)
        
    # out_pdffile_writer.addPage(input_pdffile_reader_page)
    out_pdffile_writer.write(output_pdffile_conn)
    output_pdffile_conn.close()
    txtbox.insert(0.0, "PDF File annotation finished.\n\n")
    txtbox.insert(0.0, "Annotated PDF file created on above path ^\n\n")
    txtbox.insert(0.0, os.path.dirname(import_file_path)+ "/" + output_pdffile_name + "\n\n")

annobtn = tk.Button(root, text = "                    Annotate PDF ", command= annotpdf, bg = 'green', fg= 'white',font=('helvetica', 12, 'bold'))
annobtn.grid(row=4, sticky='n', column=0)

# def convertToCSV ():
#     global read_file
    
#     export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
#     read_file.to_csv (export_file_path, index = None, header=True)

# saveAsButton_CSV = tk.Button(text='Convert Excel to CSV', command=convertToCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 180, window=saveAsButton_CSV)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='Exit Application',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
exitButton.grid(row=4, sticky='w',  column=0)

root.mainloop()
