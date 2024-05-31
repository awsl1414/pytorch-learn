from torch.utils.tensorboard.writer import SummaryWriter
from PIL import Image

writer = SummaryWriter("logs")
image_path = "./hymenoptera_data/train/ants/1030023514_aad5c608f9.jpg"
img_PIL = Image.open(image_path)
for i in range(100):
    writer.add_scalar("y=2x", 2 * i, i)

writer.close()
