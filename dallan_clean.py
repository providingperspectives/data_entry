import pdfplumber

def clean_text(text):
    # Remove excessive newlines and spaces
    text = text.replace('\n', ' ')  # Replace line breaks with a space
    text = text.replace('  ', ' ')  # Replace double spaces with a single space
    return text

with pdfplumber.open("Everdell_Rulebook.pdf") as pdf:
    with open("Everdell.md", "w") as md_file:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                cleaned_text = clean_text(text)
                md_file.write(cleaned_text + "\n\n")
