# 0213.py
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Video:
    def __init__(self, device=0):   # device = 0 #인식되는 기본 웹캠
        self.cap = cv2.VideoCapture(device)  # cv2로 영상캡쳐할 객체 생성
        self.retval, self.frame = self.cap.read() # 객체의 기본 retval 값 frame 값 저장
        self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)) #cv2 형변화하여 영상보게하는 객체 생성
        print('start capture ...')

    def updateFrame(self, k):
        self.retval, self.frame = self.cap.read()
        self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))
        # 이전 버전과 호환성을 위해 set_array함???
        return self.im,

    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture.')

# 프로그램 시작
fig = plt.figure()
fig.canvas.set_window_title('Video Capture')
plt.axis("off")

camera = Video()
##camera = Video('./data/vtest.avi')
ani = animation.FuncAnimation(fig, camera.updateFrame, interval=50)
# fig : Figure = 그리기, 크기 조정 및 기타 필요한 이벤트를 가져오는 데 사용되는 그림 개체.
# func : 소집할 수 있는# 각 프레임에서 호출하는 기능. 첫 번째 인수는 프레임의 다음 값이 될 것이다. 추가 위치 인수는 fargs 매개 변수를 통해 제공될 수 있다.
# frames : 허용 가능, int, 제너레이터 기능 또는 없음, 선택 사항, func 및 애니메이션의 각 프레임에 전달되는 데이터 소스
# init_funch : 호출 가능, 선택 사항
# fargs : tuple or none, 선택사항 각 통화에 func로 전달하기 위한 추가 인수.
# save_count : int, 선택사항, 프레임에서 캐시까지의 값 수입니다.
# interval : : 숫자, 선택 사항, 프레임 간 지연 시간(밀리초) 기본값은 200이다.
# repeat_delay : 숫자, 선택사항, 애니메이션이 반복되는 경우, 애니메이션을 반복하기 전에 밀리초 단위로 지연 시간을 추가하십시오. 기본적으로 없음으로 설정됨.
# reqeat : : bool, 선택 사항, 프레임 시퀀스가 완료될 때 애니메이션이 반복되어야 하는지 여부를 제어한다. 기본값은 True.
# blit : bool, optional, 도면을 최적화하기 위해 블리팅을 사용하는지 여부를 제어한다. 참고: 블리팅을 사용할 때 애니메이션 아티스트는 해당 지역의 순서에 따라 그려진다. 하지만, 그들은 그들의 지리에 상관없이 이전의 모든 예술가들 위에 그려질 것이다. 기본값은 False.
# cache_frame_data : bool, optional, 프레임 데이터가 캐시되는지 여부를 제어한다. 기본값은 True. 프레임에 큰 객체가 포함되어 있는 경우 캐시를 사용하지 않도록 설정하는 것이 도움이 될 수 있다.

plt.show()  # 그래프 보여줄게
# show 많다... https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html
camera.close()
