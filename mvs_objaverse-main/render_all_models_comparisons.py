import os
import argparse

parser = argparse.ArgumentParser(description='Renders glbs')
parser.add_argument(
    '--save_folder', type=str, default='/Users/jaeyounglee/Desktop/CS231N_Final_Project',
    help='path for saving rendered image')
parser.add_argument(
    '--folder_assets', type=str, default='/Users/jaeyounglee/.objaverse/hf-objaverse-v1/glbs',
    help='path to downloaded 3d assets')
parser.add_argument(
    '--blender_root', type=str, default='/Applications/Blender.app/Contents/MacOS/Blender',
    help='path to blender executable')
opt = parser.parse_args()



# get all the file
import glob 
data = sorted(glob.glob(f"{opt.folder_assets}/*/"))[10:]

for path in data:
    # path = data[-5]
    path = sorted(glob.glob(path + "/*.glb"))[0]

    # render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 100 --resolution 400' % (
    #     opt.blender_root, path, opt.save_folder
    # )

    # print(render_cmd)
    # os.system(render_cmd)


    os.makedirs(opt.save_folder + "eevee",exist_ok=True)
    render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 10 --resolution 400 --add_floor --engine BLENDER_EEVEE' % (
        opt.blender_root, path, opt.save_folder + "eevee"
    )
    print(render_cmd)
    os.system(render_cmd)
    print("EEVEE DONE")

    os.makedirs(opt.save_folder + "cycles",exist_ok=True)
    render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 10 --resolution 400 --add_floor --engine CYCLES' % (
        opt.blender_root, path, opt.save_folder + "cycles"
    )
    print(render_cmd)
    os.system(render_cmd)
    print("CYCLES DONE")
    # render_cmd = '%s -b -P rendering/render_blender.py -- --obj %s --output %s --views 100 --depth --resolution 400 > tmp.out' % (
    #     opt.blender_root, path, opt.save_folder
    # )
    break