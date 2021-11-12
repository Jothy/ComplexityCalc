import streamlit as st
import numpy as np
import pydicom as dcm
from complexity.PyComplexityMetric import PyComplexityMetric
from complexity.dicomrt import RTPlan
from pathlib import Path

st.title('      VMAT Complexity Calculator')
st.sidebar.image("D:\Projects\ComplexityCalc\Plan.PNG", use_column_width=True)

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







