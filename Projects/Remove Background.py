from rembg import remove
from PIL import Image
input_path='C:\Users\HP\Desktop\DSC02973.JPG'
image_input= Image.open(input_path)
output=remove(image_input)
output_path='output.png'
output.save(output_path)