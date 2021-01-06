import matplotlib.pyplot as plt
import attention
import detection
import distance


class TflMan:

    def __init__(self, pp, focal, json_filename, h5_filename):
        # self.EM =  # one EM? or list?
        self.pp = pp
        self.focal = focal
        self.model = detection.open_model(json_filename, h5_filename)

    def attention(self, frame):
        red_x, red_y, green_x, green_y = attention.find_tfl_lights(frame.image)
        frame.candidates = list(zip(red_x, red_y))
        # frame.auxiliary = [red] * len(red_x)
        #return candidates, auxiliary

    def detection(self, frame):
        frame.traffic_lights = detection.crop_and_predict(frame.image, frame.candidates, self.model)
        pass

    def calc_distance(self, container, EM):
        if container.prev_frame is not None:
            container.current_frame.distances = distance.calc_tfl_distances(container.prev_frame, container.current_frame, self.focal, self.pp, EM)
            #container.current_frame.traffic_lights = container.current_frame.candidates
        else:
            container.current_frame.traffic_lights = container.current_frame.candidates
            container.current_frame.distances = [1 for i in range(len( container.current_frame.candidates))]
            container.current_frame.valid = [1 for i in range(len( container.current_frame.candidates))]


    def run_frame(self, container, EM):
        # run attention on image- part 1
        # #container.current_frame.candidates, container.current_frame.auxiliary =
        self.attention(container.current_frame)
        # run detection tfl based on neural net- part 2
        # container.current_frame.traffic_light, container.current_frame.auxiliary =
        self.detection(container.current_frame)
        # run distance - part 3
        self.calc_distance(container, EM)
        self.visualize(container.current_frame)

