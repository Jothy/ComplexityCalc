'''Takes SNCPatient ArcCheck pdf per arc as PDF ifle and extract gamma pass rates adn other related information using
regular expression'''

import PyPDF2
import re

class PDF2Txt():
    def __init__(self):
        self.Info={}

    def ParsePDF(self,filename):
        reader=PyPDF2.PdfFileReader(filename)
        txt=reader.getPage(0).extractText()
        #print(txt)
        self.Info['PatientName']=re.search(r'Patient Name : (.*?)Patient ID',txt).group(1)
        self.Info['PatientID']=re.search(r'Patient ID : (.*?)Plan Date',txt).group(1)
        self.Info['PlanDate']=re.search(r'Plan Date : (.*?)SSD',txt).group(1)
        Thresholds=re.search(r' Mode : (.*?)Dose Values',txt).group(1)
        self.Info['DD']=float(Thresholds.split(':')[0])
        self.Info['DTA'] = float(Thresholds.split(':')[1])
        self.Info['DT'] = float(Thresholds.split(':')[2])
        self.Info['GammaPass'] = float(Thresholds.split(':')[6])
        return self.Info

# filename="Docs\\ArcCheck_PDFs\\5.pdf"
# parser=PDF2Txt()
# info=parser.ParsePDF(filename)
# print(info)


