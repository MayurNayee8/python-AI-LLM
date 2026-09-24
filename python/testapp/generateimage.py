import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

prompt = 'A clever, minimalist logo for a company named "Nous8.ai". The logo icon is a stylized number 8. The top loop of the 8 subtly resembles a magnifying glass or a checkmark, while the bottom loop transitions into a digital data stream or microchip pattern. The color palette is a gradient from deep purple at the top to vibrant pink at the bottom. Clean white background, highly professional, software tech branding.'

print("Generating logo...")

# 1. Use generate_content instead of generate_images
# 2. Use the dedicated Gemini image model
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        # 3. Force the model to return an image instead of text
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio="1:1"
        )
    )
)

# 4. Extract the raw image bytes from the response and save it
for part in response.candidates[0].content.parts:
    if part.inline_data:
        with open("nous8_logo.jpg", "wb") as f:
            f.write(part.inline_data.data)
        print("Success! Logo saved as nous8_logo.jpg.")