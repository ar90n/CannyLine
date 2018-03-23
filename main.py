
import cv2
import numpy as np

from cannypf import CannyPF, comp_edge_chain
from cannyline import MetaLine

def main():
    img_path = r"./img/lena30.jpg"
    img = cv2.imread(img_path, 0)
    # print('image shape', img.shape)
    # # compute edge map
    # cannypf = CannyPF(3, 70, img)
    # edgemap = cannypf.comp_edge_map()
    # # cv2.imwrite("C:\\Users\\Administrator\\Downloads\\lena30py.jpg", edgemap)
    # # line chainner , remove noise line
    # edge_chain = comp_edge_chain(img, edgemap)
    # print("computed edge chain")
    # # print(edge_chain)
    # # show image
    # result_img = np.zeros((img.shape),dtype=np.uint8)
    # for chain in edge_chain:
    #     for col,row in chain:
    #         result_img[row, col] = 255
    # cv2.imwrite("C:\\Users\\Administrator\\Downloads\\CannyPFpy.jpg", result_img)
    mtline = MetaLine()
    mtline.getInfo(img,1,1,0.125)
    cv2.imwrite(r"./img/cannypf.jpg", mtline.canny_edge)

if __name__  == "__main__":
    main()