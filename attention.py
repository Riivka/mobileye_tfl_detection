import math

'''from PIL import Image
import matplotlib.pyplot as plt
import random
'''
import scipy
from scipy.signal import convolve
'''import os
import json
import glob
import argparse'''
import numpy as np
import scipy.ndimage as ndimager

def calc_find_tfl(c_image, kernal, min_threshold=0, max_threshold=math.inf):
    convoloved = convolve(c_image, kernal, 'same')
    # plt.imshow(convoloved)
    max_filtered_img = scipy.ndimage.maximum_filter(convoloved, size=100)
    # plt.imshow(max_filtered_img)
    max_filtered_copy = max_filtered_img.copy()
    mask = ((max_filtered_copy == convoloved) & (max_filtered_copy > min_threshold) & (max_filtered_copy < max_threshold))
    positions = np.where(mask == True)
    return positions[1], positions[0]

def find_tfl_lights(c_image: np.ndarray, **kwargs):
    """
    Detect candidates for TFL lights. Use c_image, kwargs and you imagination to implement
    :param c_image: The image itself as np.uint8, shape of (H, W, 3)
    :param kwargs: Whatever config you want to pass in here
    :return: 4-tuple of x_red, y_red, x_green, y_green
    """
    threshold = 652350
    kernal = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, -255, -255, -255, -255, 0, 0, 0, 0],
                       [0, 0, 0, -255, 255, 255, 255, 255, -255, 0, 0, 0],
                       [0, 0, -255, 255, 255, 255, 255, 255, 255, -255, 0, 0],
                       [0, -255, 255, 255, 255, -255, -255, 255, 255, 255, -255, 0],
                       [0, -255, 255, 255, 255, -255, -255, -255, 255, 255, -255, 0],
                       [0, -255, 255, 255, -255, -255, -255, 255, 255, 255, -255, 0],
                       [0, 0, -255, 255, 255, 255, 255, 255, 255, 255, -255, 0],
                       [0, 0, -255, 255, 255, 255, 255, 255, 255, -255, 0, 0],
                       [0, 0, 0, -255, -255, 255, 255, 255, -255, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, -255, -255, -255, 0, 0, 0]])  # 12x11
    red_img = c_image[:, :, 0]
    red_x, red_y = calc_find_tfl(red_img, kernal, threshold)
    green_img = c_image[:, :, 1]
    threshold = 842350
    #max_threshold = 942350
    green_x, green_y = calc_find_tfl(green_img, kernal, threshold)
    #blue_img = c_image[:, :, 2]
    #threshold = 0
    #kernal = np.array([[0, 63, 0],[64, -255, 64],[0, 64, 0],])
    #blue_x, blue_y = calc_find_tfl(blue_img, kernal, threshold)
    return red_x, red_y, green_x, green_y#, blue_x, blue_y

def decide_color():
    pass
'''
def show_image_and_gt(image, objs, fig_num=None):
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.imshow(image)
    ax2.imshow(image)
    labels = set()
    if objs is not None:
        for o in objs:
            poly = np.array(o['polygon'])[list(np.arange(len(o['polygon']))) + [0]]
            #plt.plot(poly[:, 0], poly[:, 1], 'white', label=o['label'])
            labels.add(o['label'])
        if len(labels) > 1:
            plt.legend()

def test_find_tfl_lights(image_path, json_path=None, fig_num=None):
    """
    Run the attention code
    """
    image = np.array(Image.open(image_path))
    if json_path is None:
        objects = None
    else:
        gt_data = json.load(open(json_path))
        what = ['traffic light']
        objects = [o for o in gt_data['objects'] if o['label'] in what]
        print(len(objects))
    show_image_and_gt(image, objects, fig_num)
    red_x, red_y, green_x, green_y = find_tfl_lights(image)#, blue_x, blue_y = find_tfl_lights(image)
    list_x = list(red_x)+list(green_x)
    list_y = list(red_y) + list(green_y)
    plt.plot(red_x, red_y, 'ro',marker='o', color='r', markersize=4)
    plt.plot(green_x, green_y, 'ro', marker= 'o', color='g', markersize=4)
   # plt.plot(blue_x, blue_y, 'ro', marker='o', color='b', markersize=4)


def main(argv=None):
    """It's nice to have a standalone tester for the algorithm.
    Consider looping over some images from here, so you can manually exmine the results
    Keep this functionality even after you have all system running, because you sometime want to debug/improve a module
    :param argv: In case you want to programmatically run this"""
    parser = argparse.ArgumentParser("Test TFL attention mechanism")
    parser.add_argument('-i', '--image', type=str, help='Path to an image')
    parser.add_argument("-j", "--json", type=str, help="Path to json GT for comparison")
    parser.add_argument('-d', '--dir', type=str, help='Directory to scan images in')
    args = parser.parse_args(argv)
    default_base = 'data/Images/leftImg8bit/train/aachen' #'../../data'
    if args.dir is None:
        args.dir = default_base
    flist = glob.glob(os.path.join(args.dir, '*_leftImg8bit.png'))
    #flist_rand = random.choices(flist, k=10)
    flist_get_5 = flist[5:10]
    for image in flist_get_5:
        print(image)
        json_fn = image.replace('_leftImg8bit.png', '_gtFine_polygons.json')
        if not os.path.exists(json_fn):
            json_fn = None
        test_find_tfl_lights(image, json_fn)
    if len(flist):
        print("You should now see some images, with the ground truth marked on them. Close all to quit.")
    else:
        print("Bad configuration?? Didn't find any picture to show")
    plt.show(block=True)


if __name__ == '__main__':
    main()'''