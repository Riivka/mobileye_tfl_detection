import matplotlib.pyplot as plt
import attention


class TflMan:

    def __init__(self, pp, focal):
        # self.EM =  # one EM? or list?
        self.pp = pp
        self.focal = focal

    def attention(self, frame):
        red_x, red_y, green_x, green_y = attention.find_tfl_lights(frame)
        #return candidates, auxiliary
        pass

    def detection(self, frame):
        pass

    def calc_distance(self, container):
        pass

    def run_frame(self, container, EM):
        # run attention on image- part 1
        # #container.current_frame.candidates, container.current_frame.auxiliary =
        self.attention(container.current_frame)
        # run detection tfl based on neural net- part 2
        # #container.current_frame.traffic_light, container.current_frame.auxiliary =
        self.detection(container.current_frame)
        # run distance - part 3
        self.calc_distance(container)
        self.visualize(container.current_frame)
        pass

    def visualize(self, frame):
        # fig, (curr_sec, prev_sec) = plt.subplots(1, 2, figsize=(12, 6))
        fig, (sec_part_1, sec_part_2, sec_part_3) = plt.subplots(3, sharex=True, sharey=True, figsize=(12, 6))
        fig.suptitle('Frame #: image name')
        sec_part_1.plot([1, 2, 3])
        sec_part_2.plot([1, 2, 3])
        sec_part_3.plot([1, 2, 3])
        # sec_part_1.imshow(img_part_1)
        # sec_part_2.imshow(img_part_2)
        # sec_part_3.imshow(img_part_3)
        plt.show()
