import os, glob
import numpy as np
import pydicom as dcm
import PDF2Txt

# os.chdir("\\\\N12000\\ArcCheck\\Import\\19354436")
# for file in glob.glob(("*.dcm")):
#     ds=dcm.dcmread(file)
#     if(ds.Modality=='RTPLAN'):
#         print(file)

# ds=dcm.dcmread('Plans\\RP.ZZA140TRAIN_rapidarc1.dcm')
# print(ds.DoseReferenceSequence[0].TargetPrescriptionDose)

# PDFReports=[]
#
# for root, dirs, files in os.walk("\\\\N12000\ArcCheck\\Archive"):
#     for file in files:
#         if file.endswith(".pdf"):
#             try:
#                 int(root.split('\\')[5])
#                 PDFReports.append(os.path.join(root, file))
#             except:
#                 print('Non clincial ID',os.path.join(root, file))
#
#
# print('No. of PDFs found: ',np.size(PDFReports))
# parser=PDF2Txt.PDF2Txt()
# for x in range(0,np.size(PDFReports),1):
#     try:
#         info=parser.ParsePDF(PDFReports[x])
#         print(x,'/',np.size(PDFReports),info['GammaPass'])
#     except:
#         print('Error')





