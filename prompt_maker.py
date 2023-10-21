from datetime import datetime
import openai
import logging
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # Read from environment variable

def get_outfit_recommendation(user_profile):
    prompt_maker = f""" 
    You are an expert fashion consultant database generator.
    Based on the user profile with attributes such as:
        Gender: {user_profile.get('User_Gender')},
        Age: {user_profile.get('User_Age')},
        Location: {user_profile.get('Location')},
        Date: {datetime.today().strftime('%Y-%m-%d')},
        Wardrobe_Content: {user_profile.get('Wardrobe_Content')},
    please create one single entry for the database of outfit recommendations in the following format:

    - Prompt: [Your image prompt here MUST BE MANNEQUIN, e.g., a mannequin shown front, side and back, wearing a specific outfit based on the user gender and age, and weather at the current time in the location]
    - Explanation: [Your explanation here on why this outfit is appropriate based on weather, location, and user profile]
    - Suggestions: [Consider the user current wardrobe, suggest items to consider buying in a responsible manner, and avoiding duplicates]

    Thank you.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_maker,
        max_tokens=2000
    )
    return response.choices[0].text.strip()

def collect_user_profile():
    profile = {}
    profile['name'] = input("Type in your name you wish to be called: ")
    profile['skills'] = input("List your skills separated by commas (Example: C++, C#, Leadership, Unreal Engine,...): ").split(',')
    profile['years_experience_commercial'] = input("Years of commercial experience: ")
    profile['years_experience_personal'] = input("Years of personal experience: ")
    profile['target_country'] = input("Target country for job: ")
    profile['target_jobs'] = input("Target jobs separated by commas (Example: Front End, Game Developer, Lead Programmer, Full Stack Developer,...): ").split(',')
    profile['current_status'] = input("Current status (job, student, unemployed): ")
    profile['current_country'] = input("Current country: ")
    profile['current_legal_status'] = input("Current legal status (F-1, resident, other visa): ")
    
    clear_console()
    print("LOADING...")
    return profile

def test_user_profile():
    profile = {}
    profile['User_Name'] = "Jennifer"
    profile['User_Gender'] = "Female"
    profile['User_Age'] = "21"  # Add the appropriate age
    profile['Location'] = "Orlando, Florida"  # Add the appropriate location to recommend buying clothes for the weather
    profile['Wardrobe_Content'] = [
        "Green T-shirt",
        "White shirt",
        "Dark blue coat",
        "Black jeans",
        "Grey hoodie",
        "Brown leather jacket",
        "Beige chinos",
        "Black dress shoes",
        "White sneakers"
    ]
    return profile



def clear_console():
    print("\033c")