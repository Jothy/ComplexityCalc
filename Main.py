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

cwd=os.getcwd()


st.title('      VMAT Complexity Index Calculator')
#st.sidebar.image("D://Projects//ComplexityCalc//Plan.PNG", use_column_width=True)

Img1=open(os.path.join(cwd,'Images\The Canberra Hospital.jpg'), 'rb').read()
st.sidebar.image(Img1,use_column_width=True, clamp = True)

st.sidebar.title("Welcome to ComplexityCalc!")
st.sidebar.subheader('')

link = '[This is based on the publication by Younge et al, JOURNAL OF APPLIED CLINICAL MEDICAL PHYSICS, VOLUME 17, NUMBER 4, 2016.](https://aapm.onlinelibrary.wiley.com/doi/full/10.1120/jacmp.v17i4.6241)'
st.sidebar.markdown(link, unsafe_allow_html=True)

if st.sidebar.button('Open PDF'):
    with open(os.path.join(cwd,'Docs\JACMP_Ref.pdf'), "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # Embedding PDF in HTML
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="300" height="400" type="application/pdf">'
        # Displaying File
        st.sidebar.markdown(pdf_display, unsafe_allow_html=True)
if st.sidebar.button('Close PDF'):
    st.sidebar.empty()

st.sidebar.write('Broken?')
st.sidebar.markdown('<a href="mailto:Jothy.Selvaraj@act.gov.au?Subject=''ComplexityCalc issue">Contact</a>', unsafe_allow_html=True)
st.sidebar.write('Jothy.Selvaraj@act.gov.au')


filebytes= st.file_uploader('',type=("dcm"),accept_multiple_files=False)


if filebytes==None:
    st.warning('No file selected.')
else:
    # ds = dcm.read_file(filebytes)
    # st.write('Patient ID: '+ds.PatientID)
    # st.write('Patient Name: ' + str(ds.PatientName))
    # st.write('Plan Name: ' + str(ds.RTPlanLabel))

    plan_info = RTPlan(filebytes)

    st.write('----------------------------------------')
    st.write('Patient Name: ',plan_info.ds.PatientName)
    st.write('Patient ID: ',plan_info.ds.PatientID)
    st.write('Plan Label: ',plan_info.ds.RTPlanLabel)
    st.write('----------------------------------------')

    plan_dict = plan_info.get_plan()
    beams = [beam for k, beam in plan_dict["beams"].items()]
    complexity_obj = PyComplexityMetric()

    #complexity_metric = complexity_obj.CalculateForPlan(None, plan_dict)
    complexity_metric=complexity_obj.CalculateForPlanPerBeam(None,plan_dict)
    for metric in complexity_metric:
        st.write('Arc Complexity Index: '+str(np.round([metric],4)))







