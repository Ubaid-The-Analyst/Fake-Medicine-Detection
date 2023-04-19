import requests
import pytesseract
from PIL import Image

# Load the image and extract the text using pytesseract
image = Image.open("medicine_image.jpg")
text = pytesseract.image_to_string(image)

# Split the text into separate lines and extract the medicine name and code
lines = text.split("\n")
medicine_name = lines[0]
medicine_code = lines[1]

# Call the API to check the authenticity of the medicine
api_url = "https://api.medicinesverify.com/check"
payload = {
    "medicine_name": medicine_name,
    "medicine_code": medicine_code
}
response = requests.post(api_url, json=payload)

# Check the response from the API and print the result
if response.status_code == 200:
    result = response.json()["result"]
    if result == "authentic":
        print("The medicine is authentic.")
    else:
        print("The medicine is not authentic.")
else:
    print("Error: Failed to check medicine authenticity.")
