# WebSociety

## Introduction
This tool is a simple Steganography application built using Streamlit. It allows users to perform basic steganographic operations on images, hiding and revealing text within them.

## Tools Supported
- :rainbow: [Nmap](#nmap)
- :lock: **Steganography**
- :key: [Hashcat](#hashcat)

## Usage
1. Select the desired tool using the radio button.
2. Click the "Let's Go!" button to initiate the selected tool.
3. Follow the instructions for each tool.

## Tools Details

### Nmap
- Scans a host using Nmap with options like `-sS`.
- Enter the host IP and click "Run Nmap!".

### Steganography
- Upload an image (supports jpg, png, bmp).
- Enter text to hide.
- Click "Hide Text!" to hide the text within the image.

### Hashcat
- Enter the hash to crack and the wordlist path.
- Click "Run Hashcat!" to initiate the hash cracking process.

## How to Run
1. Install the required packages:
   ```bash
   pip install streamlit Pillow stegano

   ### Run the Streamlit app:
```bash
streamlit run your_app.py
