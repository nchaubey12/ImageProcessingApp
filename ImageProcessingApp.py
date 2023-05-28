import cv2

# Function to apply a grayscale filter to an image
def apply_grayscale(image):

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow(&#39;Grayscale&#39;, gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Function to resize an image
def resize_image(image, width, height):
resized_image = cv2.resize(image, (width, height))
cv2.imshow(&#39;Resized Image&#39;, resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Function to convert image format
def convert_image_format(image, format):
converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imwrite(&#39;converted_image.&#39; + format, converted_image)
print(&#39;Image converted to&#39;, format)

# Function for basic image recognition
def image_recognition(image, template):
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(gray_image, gray_template,
cv2.TM_CCOEFF_NORMED)
_, max_val, _, max_loc = cv2.minMaxLoc(result)

threshold = 0.8 # Adjust this value for desired accuracy

if max_val &gt;= threshold:
print(&#39;Image recognized at position:&#39;, max_loc)
else:
print(&#39;Image not found&#39;)

# Load an image
image_path = &#39;image.jpg&#39;
image = cv2.imread(image_path)

# Apply grayscale filter
apply_grayscale(image)

# Resize the image
new_width = 400
new_height = 300
resize_image(image, new_width, new_height)

# Convert image format
output_format = &#39;png&#39;
convert_image_format(image, output_format)

# Perform image recognition
template_path = &#39;template.jpg&#39;
template = cv2.imread(template_path)
image_recognition(image, template)