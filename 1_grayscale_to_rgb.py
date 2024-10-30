import cv2

# Get the path of the grayscale image from user input
image_path = input("Enter the path of the grayscale image: ")

# Load the grayscale image
grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if grayscale_image is None:
    print("Error loading image. Please check the path.")
else:
    # Convert the grayscale image to RGB
    rgb_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2RGB)
    
    # Print out some information about the images
    print("Grayscale Image Shape:", grayscale_image.shape)
    print("RGB Image Shape:", rgb_image.shape)

    # Display the grayscale and RGB images
    cv2.imshow("Grayscale Image", grayscale_image)
    cv2.imshow("RGB Image", rgb_image)
    
    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
