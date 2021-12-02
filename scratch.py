import os, glob
import pydicom as dcm

# os.chdir("\\\\N12000\\ArcCheck\\Import\\19354436")
# for file in glob.glob(("*.dcm")):
#     ds=dcm.dcmread(file)
#     if(ds.Modality=='RTPLAN'):
#         print(file)

# ds=dcm.dcmread('Plans\\RP.ZZA140TRAIN_rapidarc1.dcm')
# print(ds.DoseReferenceSequence[0].TargetPrescriptionDose)

xx={'Manufacturer': 'Varian Medical Systems', 'InstitutionName': 'CCO', 'TreatmentMachineName': 'V106', 'BeamName': 'Field 1', 'SourcetoSurfaceDistance': '', 'BeamDescription ': '', 'BeamType': 'DYNAMIC', 'RadiationType': 'PHOTON', 'ManufacturerModelName': '2100C/D', 'PrimaryDosimeterUnit': 'MU', 'NumberofWedges': '', 'NumberofCompensators': '', 'NumberofBoli': '', 'NumberofBlocks': '', 'FinalCumulativeMetersetWeight': '1.0', 'NumberofControlPoints': '', 'TreatmentDeliveryType': 'TREATMENT'}

print(xx['BeamName'])
