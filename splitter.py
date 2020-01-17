import textract
import csv
import smtplib
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

pdf = raw_input("Please, enter a pdf path: ")
csv_p = raw_input("Please, enter a csv path: ")
email_user = raw_input("Please, enter your email address: ")
email_password = raw_input("Please, enter your email password: ")
"""
Creating the output folder
"""
path = "./output"
try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)
pdf_file = open(pdf, 'rb')
pdf_reader = PdfFileReader(pdf_file)
subject = 'Recibo de Sueldo - Greencode'
"""
Email configuration
"""
msg = MIMEMultipart()
msg['From'] = email_user
msg['Subject'] = subject
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)
"""
Searching for matching 
"""
for x in range(pdf_reader.getNumPages()):
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(x))
    file_name = 'output/recibo_de_sueldo_n_{}.pdf'.format(x + 1)
    split_file = open(file_name, 'wb')
    pdf_writer.write(split_file)
    split_file.close()
    text = textract.process(file_name).decode('utf-8')
    with open(csv_p, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] in text:
                email_send = line[2]
                msg['To'] = email_send
                body = 'Hola! Aca te envio el recibo de sueldo {}, \nMuchas Gracias!! \nSaludos!'.format(line[1])
                msg.attach(MIMEText(body, 'plain'))
                attachment = open(file_name, 'rb')

                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= Recibo de sueldo {}".format(line[1]))

                msg.attach(part)
                text = msg.as_string()

                print("Sending email to %s" % line[2])
                server.sendmail(email_user, email_send, text)
                print("Email sent successfully")

server.quit()
pdf_file.close()
