import os
import json
from google import genai
from pypdf import PdfReader

# 1. SETUP
client = genai.Client()
PDF_PATH = "data/2025_Wimbledon_Compendium.pdf"

def debug_generation():
    print("--- DEBUG MODE START ---")
    reader = PdfReader(PDF_PATH)
    
    # Let's just try ONE page (Page 25) to see what's happening
    test_page_index = 25 
    page = reader.pages[test_page_index]
    text = page.extract_text()

    if not text.strip():
        print(f"FAILED: Page {test_page_index} is empty! pypdf cannot read this PDF. Is it a scan?")
        return

    print(f"SUCCESS: Read {len(text)} characters from page {test_page_index}.")
    print("--- Sending to Gemini ---")

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Extract 1 QA pair from this text as JSON: {text}"
        )
        print("GEMINI RESPONSE:", response.text)
    except Exception as e:
        print(f"API ERROR: {e}")

if __name__ == "__main__":
    debug_generation()