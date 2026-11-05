from file_handler import (extract_document )
from profile_cleaner import ( clean_profile, clean_skills, save_profile, load_profile )
from ai_extractor import extract_candidate
from pathlib import Path


def main():
    print("Starting Document Analyzer...")

    resume_path = Path(input("Enter resume file path: "))
    if resume_path.suffix.lower() in [".pdf", ".docx", ".txt"]:
        # Extract text from the document
        resume_text = extract_document(resume_path)
        if not resume_text:
            print("Could not extract resume text.")
            return
        # Send extracted text to Groq
        result = extract_candidate(resume_text)
        if result is not None:
            print(result.name)
            output_dir = Path("output")
            output_dir.mkdir(parents=True, exist_ok=True)
            file_path = r"C:\Users\1930s\OneDrive\Desktop\aiprojects\output\cleaned_profile.json"
            save_profile(result.model_dump(), file_path)

    else: 
        print("Unsupported file format. \n Supported formats: PDF, DOCX, TXT")
        return None


if __name__ == "__main__":
    main()



    



