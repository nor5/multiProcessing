import concurrent.futures
import pathlib
import time as t

from PIL import Image, ImageFilter

# get the images names that are in this same directory
images_names = [
    f.name for f in pathlib.Path().iterdir() if f.is_file() and ".py" not in f.name
]
size = (1200, 1200)


def process_image(image_name):
    img = Image.open(image_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f"processed/processed-{image_name}")
    return f"{image_name} was processed successfuly"


# comparing time Using multiProcessing
t_start = t.time()
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(process_image, images_names)
    for result in results:
        print(result)


t_end = t.time()

print(f"finish processing in {t_end - t_start} seconds")
 
#without Using Parallel Programming
t_start = t.time()

results = map(process_image, images_names)
for result in results:
        print(result)


t_end = t.time()
print(f"finish processing in {t_end - t_start} seconds ")
