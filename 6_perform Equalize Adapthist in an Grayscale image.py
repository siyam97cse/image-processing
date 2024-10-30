import cv2

# Load a grayscale image
image_path = input("Enter the path of the grayscale image: ")
grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if grayscale_image is None:
    print("Error loading image. Please check the path.")
else:
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized_image = clahe.apply(grayscale_image)

    # Display the original and equalized images
    cv2.imshow("Original Grayscale Image", grayscale_image)
    cv2.imshow("Equalized Image with CLAHE", equalized_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
