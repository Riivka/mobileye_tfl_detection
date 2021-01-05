from frame import Frame


class Container:
    def __init__(self,current_frame:Frame,prev_frame:Frame = None):
        self.current_frame = current_frame
        self.prev_frame = prev_frame
