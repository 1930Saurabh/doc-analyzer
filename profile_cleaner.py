import json

candidate = {
    "name": "   Alex           ",
    "skills": [
        " Python ",
        "RAG",
        "Python",
        " LangChain ",
        "",
        "LLMs"
    ]
}

def clean_skills(candidate):
    
    try: 
        cleaned_skills = {
        skill.strip()
        for skill in candidate["skills"]
        if skill.strip()
    }
        return list(cleaned_skills)
   
    except KeyError: empty_set = set()
    return empty_set

def clean_profile(candidate):
    candidate_name = candidate["name"].strip()
    candidate_skills = clean_skills(candidate)

    return {
        "name": candidate_name,
        "skills": candidate_skills
    }


def save_profile(profile, filename):
    try:
        with open(filename, "w") as file:
            return json.dump(profile, file, indent=4)

    except OSError as e:
        return (f"File operation failed: {e}")

def load_profile(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print ("File source not found")
        return {}


    
# clean_skills(candidate)
# clean_profile_func = clean_profile(candidate) 
# save_profile(clean_profile_func, r"C:\Users\1930s\OneDrive\Desktop\aiprojects\doc_analyzer\data\candidate.json" )
# print(clean_profile_func)

# profile = load_profile(r"C:\Users\1930s\OneDrive\Desktop\aiprojects\doc_analyzer\data\candidate.json")
# print(profile)
# print(type(profile))



