import cv2
import numpy as np

def cumulative_addition(image, constant=5):
    """Perform cumulative addition on an image with a specified constant."""
    # Make a copy of the image to modify
    cumulative_image = np.copy(image)

    # Iterate over each row of the image
    for i in range(cumulative_image.shape[0]):
        # Add the cumulative value to each row progressively
        cumulative_image[i, :] = np.clip(cumulative_image[i, :] + (i * constant), 0, 255)
    
    return cumulative_image

# Load a grayscale image
image_path = input("Enter the path of the grayscale image: ")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print("Error loading image. Please check the path.")
else:
    # Constant value to add cumulatively
    constant_value = 5  # Adjust the constant as needed

    # Apply cumulative addition
    cumulative_image = cumulative_addition(image, constant=constant_value)

    # Display the original and cumulative images
    cv2.imshow("Original Image", image)
    cv2.imshow("Cumulative Image with Constant", cumulative_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
