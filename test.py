import cv2

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Perform morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    return opening

def segment_characters(image):
    # Find contours
    contours, _ = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours from left to right
    contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])

    characters = []

    # Iterate over contours
    for contour in contours:
        # Get bounding box
        (x, y, w, h) = cv2.boundingRect(contour)
        
        # Filter out small contours (noise)
        if cv2.contourArea(contour) > 50:
            # Extract character
            character = image[y:y+h, x:x+w]
            characters.append(character)

    return characters

def recognize_characters(characters):
    # Implement character recognition (e.g., using machine learning models)

    # Example: print each character image
    for i, char in enumerate(characters):
        print(i)
        print(char)
        cv2.imwrite(f"char_{i}.png", char)
        print(f"Saved character {i}")

if __name__ == "__main__":
    print("Starting CAPTCHA solving...")
    image_path = "captcha_td_screenshot.png"
    
    # Preprocess image
    preprocessed_image = preprocess_image(image_path)
    print("Image preprocessed.")

    # Segment characters
    segmented_characters = segment_characters(preprocessed_image)
    print('segmented_characters>>',segmented_characters)
    print("Characters segmented.")

    # Recognize characters
    recognize_characters(segmented_characters)
    print("Character recognition completed.")
