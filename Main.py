import streamlit as st
import numpy as np
import pydicom as dcm
from complexity.PyComplexityMetric import PyComplexityMetric
from complexity.dicomrt import RTPlan
from pathlib import Path

st.title('VMAT Complexity Calculator')
#st.button('Open plan file')

filebytes= st.file_uploader("D:\Projects\ComplexityCalc", type=("dcm"))


if filebytes==None:
    st.warning('No file selected.')
else:
    # ds = dcm.read_file(filebytes)
    # st.write('Patient ID: '+ds.PatientID)
    # st.write('Patient Name: ' + str(ds.PatientName))
    # st.write('Plan Name: ' + str(ds.RTPlanLabel))

    plan_info = RTPlan(filebytes)
    plan_dict = plan_info.get_plan()
    beams = [beam for k, beam in plan_dict["beams"].items()]
    complexity_obj = PyComplexityMetric()

    complexity_metric = complexity_obj.CalculateForPlan(None, plan_dict)
    # complexity_metric=complexity_obj.CalculateForPlanPerBeam(None,plan_dict)
    st.write('Plan complexity index: '+str(np.round(complexity_metric,4)))







