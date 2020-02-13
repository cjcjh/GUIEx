# 0214.py
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Video(animation.FuncAnimation):
    def __init__(self, device=0, fig=None, frames=None,
                 interval=50, repeat_delay=5, blit=False, **kwargs):
# matplotlib.animation.FuncAnimation (옵션들)
# fig : Figure
# func : callable
# frames : iterable, int, generator function, or None, optional
# init_func : callable, optional
# fargs : tuple or None, optional
# save_count : int, optional
# interval : number, optional
# repeat_delay : number, optional
# repeat : bool, optional
# blit : bool, optional : 실시간 성능을 극적으로 개선하기 위해
# cache_frame_data : bool, optional
# **kwargs : 가변인자
        if fig is None:
            self.fig = plt.figure()
            self.fig.canvas.set_window_title('Video Capture')
            plt.axis("off")

        super(Video, self).__init__(self.fig, self.updateFrame, init_func=self.init,
                                    frames=frames, interval=interval, blit=blit,
                                    repeat_delay=repeat_delay, **kwargs)

        self.cap = cv2.VideoCapture(device)
        print("start capture ...")

    def init(self):
        retval, self.frame = self.cap.read()
        if retval:
            self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

    def updateFrame(self, k):
        retval, self.frame = self.cap.read()
        if retval:
            self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))
        return self.im
        # set_array : Set the image array from numpy array A

    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print("finish capture.")

# 프로그램 시작
camera = Video()
##camera = Video('./data/vtest.avi')
plt.show()   # 그래프 보여줘
camera.close()
