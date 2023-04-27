'''
Renders all of the data in the folder_assets with eevee and cycles.
'''

import os
import argparse

user = "Caroline"

if user == "Daniel":
    out_path = '/Users/jaeyounglee/Desktop/CS231N_Final_Project'
    in_path = '/Users/jaeyounglee/.objaverse/hf-objaverse-v1/glbs'
    blender_path = '/Applications/Blender.app/Contents/MacOS/Blender'

elif user == "Caroline":
    out_path = '/Users/carolinecahilly/Documents/cs231n_final_project/mvs_objaverse-main/output/'
    in_path = '/Users/carolinecahilly/.objaverse/hf-objaverse-v1/glbs/'
    blender_path = '/Applications/Blender.app/Contents/MacOS/Blender'

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
count = []
iterator = 0
for obj in range(len(all_data)):
    data = all_data[obj]
    folder = sorted(glob.glob(data + "/*.glb"))
    for path in folder:
        os.makedirs(opt.save_folder + "mug_" + str(obj) + "_eevee",exist_ok=True)
        render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 100 --resolution 400 --add_floor --engine BLENDER_EEVEE' % (
            opt.blender_root, path, opt.save_folder + "mug_" + str(obj) + "_eevee"
        )
        print(render_cmd)
        os.system(render_cmd)
        print("EEVEE DONE")

        os.makedirs(opt.save_folder + "mug_" + str(obj) + "_cycles",exist_ok=True)
        render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 100 --resolution 400 --add_floor --engine CYCLES' % (
            opt.blender_root, path, opt.save_folder + "mug_" + str(obj) + "_cycles"
        )
        print(render_cmd)
        os.system(render_cmd)
        print("CYCLES DONE")
        # render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 100 --depth --resolution 400 > tmp.out' % (
        #     opt.blender_root, path, opt.save_folder
        # )
        break