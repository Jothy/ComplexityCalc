import PyPDF2
import numpy as np
import re

reader=PyPDF2.PdfFileReader("D:\\Projects\\ComplexityCalc\\Docs\\ArcCheck_PDFs\\5.pdf")
txt=reader.getPage(0).extractText()
#print(txt)

PatientName=re.search(r'Patient Name : (.*?)Patient ID',txt).group(1)
PatientID=re.search(r'Patient ID : (.*?)Plan Date',txt).group(1)
PlanDate=re.search(r'Plan Date : (.*?)SSD',txt).group(1)
Thresholds=re.search(r' Mode : (.*?)Dose Values',txt).group(1)
DD=float(Thresholds.split(':')[0])
DTA=float(Thresholds.split(':')[1])
DT=float(Thresholds.split(':')[2])
GammaPass=float(Thresholds.split(':')[6])



print('Patient Name: ',PatientName)
print('Patient ID: ',PatientID)
print('Plan Date: ',PlanDate)
print({'Dose Diff':DD,'DTA':DTA,'Threshold':DT,'Gamma': GammaPass})
