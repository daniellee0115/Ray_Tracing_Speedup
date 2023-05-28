'''
Renders all of the data in the folder_assets with eevee and cycles.
'''

import os
import argparse
import re
import gltf
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image as PLImage, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import glob 

user = "Caroline"

if user == "Daniel":
    out_path = '/Users/jaeyounglee/Desktop/CS231N_Final_Project/output'
    in_path = '/Users/jaeyounglee/.objaverse/hf-objaverse-v1/glbs'
    blender_path = '/Applications/Blender.app/Contents/MacOS/Blender'

elif user == "Caroline":
    out_path = '/Users/carolinecahilly/Documents/cs231n_final_project/mvs_objaverse-main/output/'
    in_path = '/Users/carolinecahilly/.objaverse/hf-objaverse-v1/glbs/'
    blender_path = '/Applications/Blender.app/Contents/MacOS/Blender'

elif user == "stanforduser":
    out_path = '/Users/stanforduser/Desktop/cs231n_final_project-main/mvs_objaverse-main/output/'
    in_path = '/Users/stanforduser/.objaverse/hf-objaverse-v1/glbs/'
    blender_path = '/Users/stanforduser/Desktop/Blender.app/Contents/MacOS/Blender'

parser = argparse.ArgumentParser(description='Renders glbs')
parser.add_argument(
    '--save_folder', type=str, default=out_path,
    help='path for saving rendered image')
parser.add_argument(
    '--folder_assets', type=str, default=in_path,
    help='path to downloaded 3d assets')
parser.add_argument(
    '--blender_root', type=str, default=blender_path,
    help='path to blender executable')
opt = parser.parse_args()

def is_glossy(file_path):
    glb = gltf.GLTF.load(file_path)
    glossy = False
    
    for material in glb.materials:
        if material.glossiness_factor != None and material.glossiness_factor > 0:
            glossy = True
    
    return glossy

def is_metallic(file_path):
    glb = gltf.GLTF.load(file_path)
    metallic = False
    
    for material in glb.materials:
        if material.metallic_factor != None and material.metallic_factor > 0:
            metallic = True
    
    return metallic

def create_pdf_with_paths(image_paths, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []

    # Define the styles for the paths
    styles = getSampleStyleSheet()
    path_style = styles["Normal"]

    # Add each image and its path to the PDF
    for path in image_paths:
        # Open the image and get its dimensions
        image = Image.open(path)
        width, height = image.size

        # Add the image to the elements list
        elements.append(PLImage(path, width=width, height=height))

        # Add the path as a paragraph
        path_paragraph = Paragraph(path, path_style)
        elements.append(path_paragraph)

    doc.build(elements)
    print(f"Final PDF saved to '{output_path}'.")

def get_paths(feature, p):
    all_data = sorted(glob.glob(f"{opt.folder_assets}/*/*"))
    print(len(all_data))

    indices = []
    for idx in range(len(all_data)):
        path = all_data[idx]

        if feature=="metallic":
            b = is_metallic(path)
        else:
            b = is_glossy(path)

        if b:
            indices.append(idx)

    paths = []
    for i in indices:
        paths.append(p + "mug_" + str(i) + "_cycles/" + "080.png")

    return paths

# Example usage

path_to_images_folder = "/Users/carolinecahilly//Desktop/231n/mvs_objaverse-main/images/"

paths_g = get_paths("glossy", path_to_images_folder)
paths_m = get_paths("metallic", path_to_images_folder)
output_path_m = "metallic_examples.pdf"
output_path_g = "glossy_examples.pdf"

create_pdf_with_paths(paths_m, output_path_m)
create_pdf_with_paths(paths_g, output_path_g)



        