import streamlit as st
import os
import subprocess

genre = st.radio(
    "Select your tool - ",
    [":rainbow[nmap]", "***Steganography***", "Hashcat"],
    captions = ["Nmap your ass.", "Stegonograph you.", "Get your hash."])

button1 = st.button('Lets Go!')
if st.session_state.get('button') != True:

    st.session_state['button'] = button1

if (st.session_state['button'] == True):
    if genre==":rainbow[nmap]":
        options = ["-sS"]
        host = st.text_input('Host', '127.0.0.1')
        command = ['nmap'] + options + [host]
        if st.button('Run!'):
            result = subprocess.run(command, capture_output=True, text=True)
