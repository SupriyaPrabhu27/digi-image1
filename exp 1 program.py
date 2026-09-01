import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Qno. 1.jpg.jpeg', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(img_rgb.shape)

height, width = img_rgb.shape[:2]

line_img = cv2.line(img_rgb.copy(), (0, 0), (width-1, height-1), (255, 0, 0), 2)

plt.imshow(line_img)
plt.title("Image with Line")
plt.axis('off')
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = img_rgb.shape[:2]

circle_img = cv2.circle(img_rgb.copy(), (width//2, height//2), 150, (255, 0, 0), 5)

plt.imshow(circle_img)
plt.title("Image with Circle")
plt.axis('off')
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = img_rgb.shape[:2]

rectangle_img = cv2.rectangle(img_rgb.copy(), (0, 0), (width-1, height-1), (0, 255, 0), 5)

plt.imshow(rectangle_img)
plt.title("Image with Rectangle")
plt.axis('off')
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text_img = cv2.putText(img_rgb.copy(), "OpenCV Drawing", (20, 40),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

plt.imshow(text_img)
plt.title("Image with Text")
plt.axis('off')
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")
plt.show()

image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")
plt.show()

image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

plt.imshow(image_gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")
plt.show()

image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)

plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB")
plt.axis("off")
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')

print(image[100, 100])

image[200, 200] = [255, 255, 255]

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Modified Pixel")
plt.axis("off")
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')

print(image.shape)

height, width = image.shape[:2]

resized_image = cv2.resize(image, (width//2, height//2))

resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

plt.imshow(resized_image_rgb)
plt.title("Half Size Image")
plt.axis("off")
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')

roi = image[50:150, 50:150]

roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

plt.imshow(roi_rgb)
plt.title("Region of Interest")
plt.axis("off")
plt.show()

image = cv2.imread('Qno. 1.jpg.jpeg')

flip_horizontal = cv2.flip(image, 1)

flip_horizontal_rgb = cv2.cvtColor(flip_horizontal, cv2.COLOR_BGR2RGB)

plt.imshow(flip_horizontal_rgb)
plt.title("Horizontal Flip")
plt.axis("off")
plt.show()

flip_vertical = cv2.flip(image, 0)

flip_vertical_rgb = cv2.cvtColor(flip_vertical, cv2.COLOR_BGR2RGB)

plt.imshow(flip_vertical_rgb)
plt.title("Vertical Flip")
plt.axis("off")
plt.show()
