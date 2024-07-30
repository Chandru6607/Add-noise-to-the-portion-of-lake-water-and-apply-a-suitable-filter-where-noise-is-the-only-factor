import cv2
import numpy as np


image = cv2.imread('Image358.jpg')


noise = np.random.normal(0, 1, (15, 15, 3)) * 50
noise = noise.astype(np.uint8)


image_with_noise = np.copy(image)
image_with_noise[100:115, 100:115, :] += noise


image_with_noise = np.clip(image_with_noise, 0, 255).astype(np.uint8)


kernel = np.ones((3, 3), np.float32) / 9
filtered_image = cv2.filter2D(image_with_noise, -1, kernel)


subset_image = filtered_image[100:115, 100:115, :]


print("DN values for subset image:")
for channel in range(3):
    print(f"Channel {channel + 1}:")
    for row in range(15):
        for col in range(15):
            print(subset_image[row, col, channel], end=" ")
        print()
    print()
cv2.imwrite('output.jpg', subset_image)
