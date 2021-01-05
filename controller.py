import pickle
from PIL import Image
import numpy as np
from frame import Frame
from tfl_man import TflMan
from container import Container

class Controller:
    def __init__(self,path):
        EM_list,img_paths,pp,focal = self.__load_frame_playlist(path)
        self.EM_list = EM_list
        self.frame_paths = img_paths
        self.tfl_manager = TflMan(pp, focal)

    # load frame list file
    def __load_frame_playlist(self, path):
        with open(path, "r") as pls_file:

            lines_path = pls_file.readlines()
            lines_path = [line.replace('\n', '') for line in lines_path]

            img_paths = []
            for line in lines_path:
                if line.endswith('.pkl'):
                    EM_list, pp, focal = self.load_pkl_file(line)
                elif line.endswith('.png'):
                    # img = np.array(Image.open(line))
                    img_paths.append(line)
        return EM_list,img_paths,pp,focal


    # open and load the pkl file
    def load_pkl_file(path):

        with open(path, 'rb') as pklfile:
            data = pickle.load(pklfile, encoding='latin1')

        first_frame_id = 24
        last_frame_id = 29
        EM_list = []

        for frame_id in range(first_frame_id, last_frame_id + 1):
            EM = np.eye(4)
            if frame_id != first_frame_id:
                EM = np.dot(data['egomotion_' + str(frame_id - 1) + '-' + str(frame_id)], EM)
                EM_list.append(EM)

        focal = data['flx']  # normalize by focal
        pp = data['principle_point']  # should be (0,0)
        return EM_list, pp, focal

    def run_all_frames(self):
        for index,path in enumerate(self.frame_paths):
            image = np.array(Image.open(path))
            frame = Frame(image)
            container = Container(frame)
            if index==0:
                self.tlf_manager.run_frame(container,None)
            else:
                self.tlf_manager.run_frame(container, self.EM_list[index - 1])

    # def get_EM_list(self, pkl_data):


if __name__ == '__main__':
    controller = Controller()
    # load the playlist file
    controller.load_frame_playlist('frames lists/listOfFrames_dusseldorf_000049.pls.txt')
    controller.run_all_frames()
    # t = TlfMan()
    # t.visualize(0,0,0)
