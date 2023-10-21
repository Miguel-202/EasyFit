import re
from prompt_maker import get_outfit_recommendation, collect_user_profile, test_user_profile
from image_generator import generate_images, open_latest_images

try:
    prompt_line = ""
    explanation_line = ""
    suggestion_line = ""
    
    user_profile = test_user_profile()

    recommendation_text = get_outfit_recommendation(user_profile)
    print(recommendation_text)
    # Parse the recommendation_text to get the Prompt and Explanation
    try:
        pattern = re.compile(r'- Prompt: (.*?)(?:\n|$)', re.DOTALL)
        pattern_exp = re.compile(r'- Explanation: (.*?)(?:\n|$)', re.DOTALL)
        pattern_sug = re.compile(r'- Suggestions: (.*?)(?:\n|$)', re.DOTALL)
    
        match = pattern.search(recommendation_text)
        prompt_line = match.group(1).strip() if match else ""

        match = pattern_exp.search(recommendation_text)
        explanation_line = match.group(1).strip() if match else ""

        match = pattern_sug.search(recommendation_text)
        suggestion_line = match.group(1).strip() if match else ""
        
        
    except Exception as e:
        print(f"An error occurred while parsing: {e}")
        
    #print the prompt
    #print("\n\n\n\n-------------------PASSED Till 21-------\n\n\n")
    #print(f"Prompt: {prompt_line}")
    #print(f"Explanation: {explanation_line}")

    generate_images(prompt_line)
    open_latest_images()
except Exception as e:
    print(f"An error occurred: {e}")



