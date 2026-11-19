
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load image
img = mpimg.imread('image.jpg')

# Convert RGB image into grayscale
gray = (
    0.299 * img[:, :, 0] +
    0.587 * img[:, :, 1] +
    0.114 * img[:, :, 2]
)

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

# Display grayscale image
plt.subplot(1, 3, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

# Display histogram
plt.subplot(1, 3, 3)
plt.hist(gray.ravel(), bins=256)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
