class Frame:
    def __init__(self, image ,frame_id = None, candidates = None, auxiliary=None,traffic_lights = None,distance = None):
        self.frame_id = 0
        self.image = image
        self.candidates = candidates
        self.auxiliary = auxiliary
        self.traffic_lights = traffic_lights
        self.distances = distance