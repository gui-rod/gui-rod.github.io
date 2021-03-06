import xml.etree.ElementTree as ET
import json
my_data = []
mycont = 0
def extract_skeleton(path):
    global mycont
    tree = ET.parse(path)
    my_skeleton = []
    root = tree.getroot()

    for i,child in enumerate(root):
        # there are many skeletons tracked, each folder has only one skeleton Tracked
        if (i == 0) or True:
            #print(child)
            for option in child:
                if option.tag == "Joints":
                    for joint in option:
                        position = joint[0]
                        #print(f'x={position[0].text}; y={position[1].text}; z={position[2].text}')
                        x=position[0].text
                        y=position[1].text
                        z=position[2].text
                        my_skeleton.append({"x": x, "y": y, "z":z})
                        if ((mycont % 20 == 0) and (mycont<200)) or x=='0':
                            pass
                            #print(f'{path[-10:]} {x},{y},{z}')
                        mycont = mycont + 1
    #print(len(my_skeleton))
    return my_skeleton

def run_sample():
    folder = 'dataset/Misc/KinectOutput40/Skeleton'
    folder = 'dataset/Fighting/KinectOutput106/Skeleton'

    from os import walk
    for (dirpath, dirnames, filenames) in walk(folder):
        for filename in filenames:
            my_data.append(extract_skeleton(f'{folder}/{filename}'))

    with open("skeletons.json", "w") as write_file:
        json.dump(my_data, write_file)
        #print(f'{len(my_data)} frames saved')


run_sample()