import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image


resize = transforms.Resize((512, 512))


def do(p):
    img = Image.open(p)
    img = resize(img)
    img.save(p)


for i in range(7):
    p = f"./style/{i}.jpg"
    do(p)