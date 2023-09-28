# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code

st.session_state.hco1=st.text_input("Hydrocarbon 1 (grams)",value=5.326)
st.session_state.co2=st.text_input("CO2 output from 1 (grams)",value=7.552)
st.session_state.hco2=st.text_input("Hydrocarbon 2 (grams)",value=5.326)
st.session_state.h2o=st.text_input("H2O output from 2 (grams)",value=4.638)
if st.button("Compute"):
    st.write("Computing the heat of combustion")
    hco1=float(st.session_state.hco1)
    co2=float(st.session_state.co2)
    hco2=float(st.session_state.hco2)
    h2o=float(st.session_state.h2o)
    st.write(f"Inputs: HCO1 {hco1} CO2 {co2} HCO2 {hco2} H2O {h2o}")
    co2_moles=co2/44.01
    h2o_moles=h2o/18.02
    st.write(f"CO2 moles {co2_moles} H2O moles {h2o_moles}")
    c_moles=co2_moles
    h_moles=h2o_moles*2
    st.write(f"C moles {c_moles} H moles {h_moles}")
    c_grams=c_moles*12.01
    h_grams=h_moles*1.008
    st.write(f"C grams {c_grams} H grams {h_grams}")
    c_pct=100*c_grams/hco1
    h_pct=100*h_grams/hco2
    o_pct=100-(c_pct+h_pct)
    st.write(f"By weight C % {c_pct} H % {h_pct} O % {o_pct}")
    c_atoms=c_pct/12.01
    h_atoms=h_pct/1.008
    o_atoms=o_pct/16.00
    st.write(f"By atoms C {c_atoms} H {h_atoms} O {o_atoms}")
    #
    #
    #
    st.write("TO-DO: More to do....")