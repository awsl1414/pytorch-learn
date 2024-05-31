from torchvision import transforms
from PIL import Image

# tensor 使用
image_path = "hymenoptera_data/train/bees/39672681_1302d204d1.jpg"
img = Image.open(image_path)
# print(img)

tensor_trans = transforms.ToTensor()

tensor_img = tensor_trans(img)

print(tensor_img)
