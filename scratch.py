import os, glob
import pydicom as dcm

# os.chdir("\\\\N12000\\ArcCheck\\Import\\19354436")
# for file in glob.glob(("*.dcm")):
#     ds=dcm.dcmread(file)
#     if(ds.Modality=='RTPLAN'):
#         print(file)

ds=dcm.dcmread('Plans\\RP.ZZA140TRAIN_rapidarc1.dcm')
print(ds.DoseReferenceSequence[0].TargetPrescriptionDose)

