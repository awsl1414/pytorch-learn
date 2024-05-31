from torch.utils.tensorboard.writer import SummaryWriter
from PIL import Image
import numpy as np

writer = SummaryWriter("logs")
image_path = "hymenoptera_data/train/bees/39672681_1302d204d1.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)

# print(img_array.shape)

writer.add_image("bee", img_array, 2, dataformats="HWC")
for i in range(100):
    writer.add_scalar("y=2x", 2 * i, i)

writer.close()
