import os
from PIL import Image

def make_gif(image_folder, output_path, duration=1000):
    images = []
    for file_name in sorted(os.listdir(image_folder)):
        if file_name.endswith('.png') or file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
            file_path = os.path.join(image_folder, file_name)
            images.append(Image.open(file_path))

    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:], duration=duration, loop=0)
    else:
        print("No images found in the folder.")

if __name__ == "__main__":
    root_folder = 'generate_images_v2'
    folders = os.listdir(root_folder)
    for folder in folders:
        image_folder = os.path.join(root_folder, folder, folder)
        if not os.path.exists(image_folder):
            continue
        if folder == 'teaser':
            output_path = os.path.join(root_folder, folder, 'output.gif')
            make_gif(image_folder, output_path)