import logging
import os
from dotenv import load_dotenv
import requests
from datetime import datetime
import openai
load_dotenv()
def generate_images(_prompt):
    try:
        print("\n\n\nPrompt: ", _prompt, "\n\n\n")
        #model_engine = "image-davinci-002"  # replace this with the appropriate DALL-E engine ID
        response = openai.Image.create(
            prompt=_prompt,
            n=3,
            size="1024x1024",
        )
        
        image_urls = [data['url'] for data in response['data']]
        image_paths = []  # To store the paths of downloaded images

        # Generate a timestamp for folder naming
        timestamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        timestamped_folder = os.path.join("images", timestamp)

        # Create a folder with the current timestamp
        if not os.path.exists(timestamped_folder):
            os.makedirs(timestamped_folder)

        for i, image_url in enumerate(image_urls):
            image_path = download_image(image_url, timestamped_folder, i+1)  # Passing timestamped folder directly
            image_paths.append(image_path)

        return image_paths 

    except Exception as e:
        logging.error(f"----Error generating images: {e}")

def download_image(url, timestamped_folder, image_number):
    # Define the name of the image file
    image_name = f"image{image_number}.png"

    # Full path to save the image
    image_path = os.path.join(timestamped_folder, image_name)

    # Download and save the image
    response = requests.get(url)
    if response.status_code == 200:
        with open(image_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download image. HTTP Status Code: {response.status_code}")

    return image_path  # Return the path where the image is saved

def get_latest_directory(parent_directory):
    subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]
    subdirectories.sort(reverse=True)
    return os.path.join(parent_directory, subdirectories[0]) if subdirectories else None

def open_latest_images():
    latest_dir = get_latest_directory("images/")
    if latest_dir:
        for image in os.listdir(latest_dir):
            image_path = os.path.join(latest_dir, image)
            os.system(f'start "" "{image_path}"')
    else:
        print("No latest directory found.")
        