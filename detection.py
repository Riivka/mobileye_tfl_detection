import math


def crop_tlf(img, col, row, rang):
    '''

    :param img: img to crop
    :param col: the column to crop around
    :param row:
    :param rang:
    :return:
    '''
    start_range_col = col - math.floor(rang / 2) if col - math.floor(rang / 2) > 0 else 0
    end_range_col = start_range_col + rang if start_range_col + rang < img.shape[1] else img.shape[1]
    if end_range_col == img.shape[1]:
        start_range_col = end_range_col - rang

    start_range_row = row - math.floor(rang / 2) if row - math.floor(rang / 2) > 0 else 0
    end_range_row = start_range_row + rang if start_range_row + rang < img.shape[0] else img.shape[0]
    if end_range_row == img.shape[0]:
        start_range_row = end_range_row - rang

    return img[start_range_row:end_range_row, start_range_col: end_range_col]


def crop_img(img, pos, size):
    tlf_imgs = []
    for tlf in pos:
        #if tlf[1] >= 1012:
        #    print()
        cp = crop_tlf(img, tlf[0], tlf[1], size)
        tlf_imgs += list(crop_tlf(img, tlf[0], tlf[1], size))
    return tlf_imgs