from google.cloud import vision
import io

def detect_text(image_path):
    """Detects text in an image using Google Cloud Vision API."""
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        print("Detected Text:\n", texts[0].description)
    else:
        print("No text detected.")

    if response.error.message:
        raise Exception(f"Error in OCR: {response.error.message}")

# ✅ Use the correct image path with a raw string (r"") to avoid escape issues
image_path = r"C:\Users\Omar\Pictures\Screenshots\Screenshot 2024-10-20 134819.png"

# Run OCR
detect_text(image_path)
