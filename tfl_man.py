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
        sec_part_1.imshow(frame.image)
        sec_part_2.imshow(frame.image)
        sec_part_3.imshow(frame.image)
        plt.show()
        fig, (sec_part_1, sec_part_2, sec_part_3) = plt.subplots(3, sharex=True, sharey=True, figsize=(12, 6))
        fig.suptitle(f'Frame #{frame.frame_id}: image name')
        sec_part_1.imshow(frame.image)
        x = [pt[0] for pt in frame.candidates]
        y = [pt[1] for pt in frame.candidates]
        sec_part_1.plot(x, y, 'ro', marker='o', color='r', markersize=2)
        sec_part_2.imshow(frame.image)
        sec_part_3.imshow(frame.image)
        # curr_sec.plot(curr_p[:, 0], curr_p[:, 1], 'b+')
        for i in range(len(frame.traffic_lights)):
            # curr_sec.plot([curr_p[i, 0], foe[0]], [curr_p[i, 1], foe[1]], 'b')
            if frame.valid[i]:
                sec_part_3.text(frame.traffic_lights[i][0], frame.traffic_lights[i][1],
                                r'{0:.1f}'.format(frame.distances[i]), color='r')
        # curr_sec.plot(foe[0], foe[1], 'r+')
        # curr_sec.plot(rot_pts[:, 0], rot_pts[:, 1], 'g+')
        plt.show()
