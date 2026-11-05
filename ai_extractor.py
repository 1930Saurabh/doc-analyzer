import os
from groq import Groq, APIError, APIConnectionError
from dotenv import load_dotenv
import json
from pydantic import ValidationError, Field
from models import Candidate 

def extract_candidate(resume_text):
    load_dotenv()
    my_api = os.getenv("GROQ_API_KEY")
    if not my_api:
        raise ValueError("GROQ_API_KEY not found")
    client = Groq(api_key=my_api)
    model = "openai/gpt-oss-120b"

    
    system_prompt = """
                You are an expert resume information extraction system.
                
                Your task is to extract structured candidate information from the
                provided resume.
                
                Extract the following fields:
                
                1. name
                2. email
                3. phone
                4. summary
                5. experience
                6. projects
                7. education
                8. skills
                9. certificates
                10. links
                
                OUTPUT STRUCTURE:
                
                Return a JSON object with exactly these top-level fields:
                
                {
                    "name": "string",
                    "email": null,
                    "phone": null,
                    "summary": null,
                    "experience": [
                        {
                            "company": "string",
                            "role": "string",
                            "start_date": "string",
                            "end_date": null,
                            "responsibilities": []
                        }
                    ],
                    "projects": [
                        {
                            "title": "string",
                            "year": null,
                            "description": "string",
                            "skills": [],
                            "outcome": null
                        }
                    ],
                    "education": [
                        {
                            "institution": "string",
                            "degree": null,
                            "level": null,
                            "period": null,
                            "year": null,
                            "percentage": null
                        }
                    ],
                    "skills": [],
                    "certificates": [],
                    "links": {}
                }
                
                EXTRACTION RULES:
                
                1. Return only valid JSON. Do not include Markdown or explanations.
                2. Do not invent or assume information that is not present in the resume.
                3. Use null for unavailable single values.
                4. Use empty arrays for unavailable list fields.
                5. Use an empty object {} for unavailable dictionary fields.
                6. Preserve the original information provided in the resume.
                7. Project objects must use "title", never "name".
                8. Education percentage must be a numeric value without the percentage symbol.
                   Example: 76.04, not "76.04%".
                9. Links must be a dictionary containing platform names as keys
                   and URLs as values.
                   Example: {"github": "https://github.com/example"}.
                10. Experience responsibilities and project skills must be arrays of strings.
                11. Dates and phone numbers must be returned as strings.
                12. Do not omit any top-level fields, even if their values are null,
                    empty arrays, or empty objects.
                
                Ensure that the JSON structure matches the specified output exactly.
                """


    messages  = [ 
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": resume_text
        }
    ]

    try:  
        response = client.chat.completions.create(messages= messages, model = model, temperature = 0)
        final_res = response.choices[0].message.content

    except APIError as e:
        print(f"Groq API error occurred: {e.status_code} - {e.message}")
        return None
    except APIConnectionError as e:
        print(f"Couldn't connect to the model: {e}")
        return None

    try:
        if final_res:
            extracted_data = json.loads(final_res)
            validated_candidate = Candidate.model_validate(extracted_data)
            return validated_candidate
        else: 
            print("Empty response from Groq")
            return None

    except json.JSONDecodeError:
        print("Invalid JSON response from AI")
        return None
    except ValidationError as e:
        print(e)
        return None