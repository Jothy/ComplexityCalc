import os

import streamlit as st
import webbrowser
import base64
import numpy as np
import pydicom as dcm
from complexity.PyComplexityMetric import PyComplexityMetric
from complexity.dicomrt import RTPlan
from pathlib import Path
import os
import AutoCalc

PlanInfo={}


cwd=os.getcwd()

st.title('      VMAT Complexity Index Calculator')
#st.sidebar.image("D://Projects//ComplexityCalc//Plan.PNG", use_column_width=True)

OrganizationImg=open(os.path.join(cwd,'Images\The Canberra Hospital.jpg'), 'rb').read()
st.sidebar.image(OrganizationImg,use_column_width=True, clamp = True)

st.sidebar.title("Welcome to ComplexityCalc!")
st.sidebar.subheader('')

link = '[This is based on the publication by Younge et al, JOURNAL OF APPLIED CLINICAL MEDICAL PHYSICS, VOLUME 17, NUMBER 4, 2016.](https://aapm.onlinelibrary.wiley.com/doi/full/10.1120/jacmp.v17i4.6241)'
st.sidebar.markdown(link, unsafe_allow_html=True)

openBtn,closeBtn=st.sidebar.columns(2)

if openBtn.button('Open PDF'):
    with open(os.path.join(cwd,'Docs\JACMP_Ref.pdf'), "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # Embedding PDF in HTML
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="300" height="400" type="application/pdf">'
        # Displaying File
        st.sidebar.markdown(pdf_display, unsafe_allow_html=True)
if closeBtn.button('Close PDF'):
    st.sidebar.empty()


st.sidebar.write('Broken?')

mailLink,mailAddress=st.sidebar.columns([0.5,1])
mailLink.markdown('<a href="mailto:Jothy.Selvaraj@act.gov.au?Subject=''ComplexityCalc issue">Contact</a>', unsafe_allow_html=True)
mailAddress.write('Jothy.Selvaraj@act.gov.au')


licenseLink = '[This program is distributed under GNU General Public License v3.0](https://github.com/Jothy/ComplexityCalc/blob/master/LICENSE)'
st.sidebar.markdown(licenseLink, unsafe_allow_html=True)

LicenseImg=open(os.path.join(cwd,'Images\LicenseConditions.PNG'), 'rb').read()
st.sidebar.image(LicenseImg,use_column_width=True, clamp = False)




gitHublink = '[Find me on GitHub](https://github.com/Jothy/ComplexityCalc)'
st.sidebar.markdown(gitHublink, unsafe_allow_html=True)


#Calculate complexity indices
filebytes= st.file_uploader('',type=("dcm"),accept_multiple_files=False)

if filebytes==None:
    st.warning('No file selected.')
else:
    plan_info = RTPlan(filebytes)
    PlanInfo['Fractions']=plan_info.ds.FractionGroupSequence[0].NumberOfFractionsPlanned

    st.write('----------------------------------------')
    st.write('Patient Name: ',plan_info.ds.PatientName)
    st.write('Patient ID: ',plan_info.ds.PatientID)
    st.write('Plan Label: ',plan_info.ds.RTPlanLabel)
    st.write('Fractions: ',str(PlanInfo['Fractions']))
    st.write('----------------------------------------')

    plan_dict = plan_info.get_plan()
    beams = [beam for k, beam in plan_dict["beams"].items()]
    complexity_obj = PyComplexityMetric()

    #complexity_metric = complexity_obj.CalculateForPlan(None, plan_dict)
    complexity_metric=complexity_obj.CalculateForPlanPerBeam(None,plan_dict)
    for metric in complexity_metric:
        st.write('Arc Complexity Index: '+str(np.round([metric],4)))









