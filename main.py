import streamlit as st
import os
import subprocess

genre = st.radio(
    "Select your tool - ",
    [":rainbow[nmap]", "***Steganography***", "Hashcat"],
    captions = ["Nmap your ass.", "Stegonograph you.", "Get your hash."])

if st.button("Submit"):
    if genre == ":rainbow[nmap]":
        options = ["-sS"]
        host = st.text_input('Host', '127.0.0.1')
        command = ['nmap'] + options + [host]
        result = subprocess.run(command, capture_output=True, text=True)