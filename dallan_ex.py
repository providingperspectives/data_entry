import pdfplumber

with pdfplumber.open("Everdell_Rulebook.pdf") as pdf:
    with open("output_file.md", "w") as md_file:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                md_file.write(text + "\n\n")