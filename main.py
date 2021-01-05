from controller import Controller

if __name__ == '__main__':
    controller = Controller('frames lists/listOfFrames_dusseldorf_000049.pls.txt')
    # load the playlist file
    # controller.load_frame_playlist('frames lists/listOfFrames_dusseldorf_000049.pls.txt')
    controller.run_all_frames()
    # t = TlfMan()
    # t.visualize(0,0,0)

