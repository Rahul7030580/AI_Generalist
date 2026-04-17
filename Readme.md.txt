# AI DDR Report Generator

## Overview

This project generates a Detailed Diagnostic Report (DDR) from inspection and thermal PDFs using AI.

## Features

* Extracts data from PDFs
* Identifies affected areas
* Generates root causes and recommendations
* Produces downloadable DDR report

## Tech Stack

* Python
* Streamlit
* PyMuPDF
* Groq API
* ReportLab

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Add API key:
   GROQ_API_KEY=your_key

3. Run:
   streamlit run app.py
