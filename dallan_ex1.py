import pdfplumber

# Define relevant keywords related to game setup, play, and scoring
relevant_keywords = ['setup', 'rules', 'scoring', 'how to play', 'instructions', 'gameplay']

def clean_text(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Filter out lines that don't contain relevant keywords
    cleaned_lines = [line for line in lines if any(keyword in line.lower() for keyword in relevant_keywords)]
    
    # Join the filtered lines back together
    return ' '.join(cleaned_lines)

# Extract and clean the PDF content
with pdfplumber.open("Everdell_Rulebook.pdf") as pdf:
    with open("manual.md", "w") as md_file:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                cleaned_text = clean_text(text)
                if cleaned_text:  # Only write non-empty content
                    md_file.write(cleaned_text + "\n\n")
