import base64

import cv2
import numpy as np
import zmq


def sub_video():
    context = zmq.Context()
    footage_socket = context.socket(zmq.SUB)
    port = 5555
    bind_address = "tcp://*:{}".format(port)  # 'tcp://*:5555'
    print("Subscribe Video at ", bind_address)
    footage_socket.bind(bind_address)
    footage_socket.setsockopt_string(zmq.SUBSCRIBE, str(''))
    while True:
        try:
            frame = footage_socket.recv()
            img = base64.b64decode(frame)
            npimg = np.frombuffer(img, dtype=np.uint8)
            npimg = npimg.reshape([720, 1280, 3])
            cv2.imshow("image", npimg)
            cv2.waitKey(113)
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            print("\n\nBye bye\n")
            break


if __name__ == '__main__':
    sub_video()
