# Image-Handling-and-Pixel-Transformations-Using-OpenCV 

## AIM:
Write a Python program using OpenCV that performs the following tasks:

1) Read and Display an Image.  
2) Adjust the brightness of an image.  
3) Modify the image contrast.  
4) Generate a third image using bitwise operations.

## Software Required:
- Anaconda - Python 3.7
- Jupyter Notebook (for interactive development and execution)

## Algorithm:
### Step 1:
Load an image from your local directory and display it.

### Step 2:
Create a matrix of ones (with data type float64) to adjust brightness.

### Step 3:
Create brighter and darker images by adding and subtracting the matrix from the original image.  
Display the original, brighter, and darker images.

### Step 4:
Modify the image contrast by creating two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix).  
Display the original, lower contrast, and higher contrast images.

### Step 5:
Split the image (boy.jpg) into B, G, R components and display the channels

## Program Developed By:
- **Name:** SUPRIYA PRABHU  
- **Register Number:** 212224240165

  ### Ex. No. 01



# **Step 1: Load and Display the Image**

## Import the required libraries

```PYTHON
import cv2
import matplotlib.pyplot as plt
```

## Read the image using OpenCV

```PYTHON
img = cv2.imread('Qno. 1.jpg.jpeg', cv2.IMREAD_COLOR)
```

## Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)

```PYTHON
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

## Display the image using Matplotlib

```PYTHON
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()
```
## Output:
<img width="612" height="502" alt="image" src="https://github.com/user-attachments/assets/d998c3ea-7fc9-48d8-ba11-9d4c7c67815e" />

---

# **Step 2: Drawing Operations**

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Convert BGR to RGB

```PYTHON
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

## Display the image size

```PYTHON
img_rgb.shape
```

---

## Draw a line from the top-left to the bottom-right

```PYTHON
height, width = img_rgb.shape[:2]

line_img = cv2.line(img_rgb.copy(),
                    (0,0),
                    (width-1,height-1),
                    (255,0,0),
                    2)

plt.imshow(line_img)
plt.title("Image with Line")
plt.axis('off')
plt.show()
```
## Output:
<img width="608" height="502" alt="image" src="https://github.com/user-attachments/assets/167344d1-b1ee-4486-bb87-fd686a966d42" />

---

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Convert BGR to RGB

```PYTHON
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

## Draw a circle at the center of the image

```PYTHON
height, width = img_rgb.shape[:2]

circle_img = cv2.circle(img_rgb.copy(),
                        (width//2,height//2),
                        150,
                        (255,0,0),
                        5)

plt.imshow(circle_img)
plt.title("Image with Circle")
plt.axis('off')
plt.show()
```
## Output:
<img width="606" height="502" alt="image" src="https://github.com/user-attachments/assets/f3c4cf46-9e49-46a5-8a4d-580a5f9f378e" />

---

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Convert BGR to RGB

```PYTHON
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

## Draw a rectangle around the image

```PYTHON
height, width = img_rgb.shape[:2]

rectangle_img = cv2.rectangle(img_rgb.copy(),
                              (0,0),
                              (width-1,height-1),
                              (0,255,0),
                              5)

plt.imshow(rectangle_img)
plt.title("Image with Rectangle")
plt.axis('off')
plt.show()
```
## Output:
<img width="602" height="501" alt="Screenshot 2026-07-24 111457" src="https://github.com/user-attachments/assets/ebc66b06-2fc2-496e-a3b1-57d28f7b40a6" />


---

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Convert BGR to RGB

```PYTHON
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

## Add the text "OpenCV Drawing"

```PYTHON
text_img = cv2.putText(img_rgb.copy(),
                       "OpenCV Drawing",
                       (20,40),
                       cv2.FONT_HERSHEY_SIMPLEX,
                       1,
                       (255,255,255),
                       2)

plt.imshow(text_img)
plt.title("Image with Text")
plt.axis('off')
plt.show()
```

---

# **Step 3: Color Space Conversion**

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Convert BGR to RGB

```PYTHON
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

## Display the Original RGB Image

```PYTHON
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")
plt.show()
```
## Output:
<img width="610" height="501" alt="image" src="https://github.com/user-attachments/assets/b3e3e6a3-dede-41a4-9653-d3a42d077858" />

---

## Convert RGB to HSV

```PYTHON
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")
plt.show()
```
## Output:
<img width="603" height="497" alt="image" src="https://github.com/user-attachments/assets/d51b5324-2c89-4f91-b9a2-947c70c9e70f" />

---

## Convert RGB to Grayscale

```PYTHON
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

plt.imshow(image_gray,cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()
```
## Output:
<img width="1086" height="331" alt="Screenshot 2026-07-24 110342" src="https://github.com/user-attachments/assets/f5bbc0d6-ba8e-4aac-b99b-72cc52e97409" />

---

## Convert RGB to YCrCb

```PYTHON
image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")
plt.show()
```

---

## Convert HSV back to RGB

```PYTHON
image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)

plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB")
plt.axis("off")
plt.show()
```
## Output:
<img width="605" height="497" alt="image" src="https://github.com/user-attachments/assets/422ec725-10d6-410c-9b58-1a8228165c61" />

---

# **Step 4: Pixel Access and Modification**

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Access the pixel value at (100,100)

```PYTHON
print(image[100,100])
```

---

## Modify the pixel at (200,200) to white

```PYTHON
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()
```
## Output:
<img width="610" height="503" alt="image" src="https://github.com/user-attachments/assets/98a1f695-44a7-4f1f-a4a3-99640616a964" />

## Convert BGR to RGB

```PYTHON
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
```

## Display the modified image

```PYTHON
plt.imshow(image_rgb)
plt.title("Modified Pixel")
plt.axis("off")
plt.show()
```

---

# **Step 5: Resize the Image**

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Display image size

```PYTHON
image.shape
```

---

## Resize the image to half its size

```PYTHON
height,width = image.shape[:2]

resized_image = cv2.resize(image,(width//2,height//2))
```


## Convert BGR to RGB

```PYTHON
resized_image_rgb = cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB)
```

## Display the resized image

```PYTHON
plt.imshow(resized_image_rgb)
plt.title("Half Size Image")
plt.axis("off")
plt.show()
```
## Output:
<img width="607" height="502" alt="image" src="https://github.com/user-attachments/assets/82436cf2-58e3-45c5-912f-f5ad3e8201a1" />

---

# **Step 6: Crop the Region of Interest (ROI)**

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Crop a 100×100 Region starting at (50,50)

```PYTHON
roi = image[50:150,50:150]
```

## Convert BGR to RGB

```PYTHON
roi_rgb = cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
```

## Display the ROI

```PYTHON
plt.imshow(roi_rgb)
plt.title("Region of Interest")
plt.axis("off")
plt.show()
```
## Output:
<img width="481" height="502" alt="image" src="https://github.com/user-attachments/assets/4f316b74-f369-4aa7-b953-b9df52b2b3a6" />

---

# **Step 7: Flip the Image**

## Load the image

```PYTHON
image = cv2.imread('Qno. 1.jpg.jpeg')
```

## Flip the image horizontally

```PYTHON
flip_horizontal = cv2.flip(image,1)

flip_horizontal_rgb = cv2.cvtColor(flip_horizontal,cv2.COLOR_BGR2RGB)

plt.imshow(flip_horizontal_rgb)
plt.title("Horizontal Flip")
plt.axis("off")
plt.show()
```
## Output:
<img width="605" height="510" alt="image" src="https://github.com/user-attachments/assets/08f8ed10-ff58-4e8e-86e7-79dcd7126522" />

---

## Flip the image vertically

```PYTHON
flip_vertical = cv2.flip(image,0)

flip_vertical_rgb = cv2.cvtColor(flip_vertical,cv2.COLOR_BGR2RGB)

plt.imshow(flip_vertical_rgb)
plt.title("Vertical Flip")
plt.axis("off")
plt.show()
```
## Output:
<img width="606" height="503" alt="image" src="https://github.com/user-attachments/assets/053d820a-c824-4980-8bc7-eaa075cb0472" />

---






## Result:
Thus, the images were read, displayed, brightness and contrast adjustments were made, and bitwise operations were performed successfully using the Python program.
