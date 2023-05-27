'''
Renders all of the data in the folder_assets with eevee and cycles.
'''

import os
import argparse
import re
import gltf

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



# get all the file
import glob 

all_data = sorted(glob.glob(f"{opt.folder_assets}/*/"))

def get_materials_from_glb(file_path):
    glb = gltf.GLTF.load(file_path)
    materials = []
    
    for material in glb.materials:
        # Extract material properties
        # name = material.metallic
        # print(material.glossiness_factor) # dir(material)
        print(dir(material))
        # You can access other properties such as base color, metallic, roughness, etc.
        # using material.base_color, material.metallic, material.roughness, etc.
        
        # materials.append(name)  # Append the material name to the list
    
    return materials

my_set = set()
for obj in range(len(all_data)):
    data = all_data[obj]
    folder = sorted(glob.glob(data + "/*.glb"))
    for path in folder:
        
        for m in get_materials_from_glb(path):
            my_set.add(m)


        # os.makedirs(opt.save_folder + "_mug_" + str(pathName) + "_eevee",exist_ok=True)
        # render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 100 --resolution 400 --add_floor --engine BLENDER_EEVEE' % (
        #     opt.blender_root, path, opt.save_folder + "_mug_" + str(pathName) + "_eevee"
        # )
        # print(render_cmd)
        # os.system(render_cmd)
        # print("EEVEE DONE")

        # os.makedirs(opt.save_folder + "_mug_" + str(pathName) + "_cycles",exist_ok=True)
        # render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 100 --resolution 400 --add_floor --engine CYCLES' % (
        #     opt.blender_root, path, opt.save_folder + "_mug_" + str(pathName) + "_cycles"
        # )
        # print(render_cmd)
        # os.system(render_cmd)
        # print("CYCLES DONE")
        # render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 100 --depth --resolution 400 > tmp.out' % (
        #     opt.blender_root, path, opt.save_folder
        # )

print(my_set)
print(len(my_set))