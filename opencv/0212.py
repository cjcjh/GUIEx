# 0212.py
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 프로그램 시작
#cap = cv2.VideoCapture('./data/vtest.avi')
cap = cv2.VideoCapture(0) # 집 노트북으로하니 바로 노트북 캠이 사용됨
fig = plt.figure(figsize=(10, 6)) # fig.set_size_inches(10, 6)
# plt.figure( 속성들 )
# num num : integer or string, optional, default: None
# 제공되지 않으면 새로운 그림이 생성되고, 숫자 번호가 증가하게 된다.
# 숫자가 제공되고 이 ID를 가진 수치가 이미 존재하면 활성화하고 참조를 반환한다.
# 이 수치가 존재하지 않으면 생성하여 반환하십시오. num이 문자열이면 창 제목은 이 숫자의 숫자로 설정된다.
# figsize : (float, float), optional, default: None
#  너비, 높이(인치) 제공되지 않으면 rcParams["그림"으로 기본 설정된다.그림 크기"](기본값: [6.4, 4.8]) = [6.4, 4.8].
## dpi : integer, optional, default: None
# 그림의 해상도 제공되지 않으면 rcParams["그림.dpi"](기본값: 100.0) = 100으로 기본 설정된다.
## facecolor : color spec
# 배경색 제공되지 않으면 rcParams["그림"으로 기본 설정된다.얼굴색"](기본값: '흰색') = 'w'
## edgecolor : color spec
# 테두리 색 제공되지 않으면 rcParams["그림.edge color"](기본값: '흰색') = 'w'로 기본 설정됨.
## frameon : bool, optional, default: True
# 거짓인 경우 그림 프레임 그리기를 억제하십시오.
## FigureClass : subclass of Figure
# 선택적으로 사용자 정의 그림 인스턴스를 사용하십시오.
## clear : bool, optional, default: False
# True와 수치가 이미 존재하면 삭제된다.
## Returns : Figure
# 반환되는 그림 인스턴스는 또한 백엔드의 new_figure_manager로 전달되며,
# 이를 통해 사용자 지정 그림 클래스를 fyplot 인터페이스에 연결할 수 있다.
# 추가 크와그kwargs는 그림 초기화 함수로 전달된다.
fig.canvas.set_window_title('Video Capture')
# 그림이 들어 있는 창의 제목 텍스트를 설정한다. 창이 없는 경우(예: PS 백엔드)에는 아무런 영향이 없다는 점에 유의하십시오.
plt.axis('off')
# 'on'	Turn on axis lines and labels. Same as True.
# 'off'	Turn off axis lines and labels. Same as False.
# 'equal'	Set equal scaling (i.e., make circles circular) by changing axis limits.
# 'scaled'	Set equal scaling (i.e., make circles circular) by changing dimensions of the plot box.
# 'tight'	Set limits just large enough to show all data.
# 'auto'	Automatic scaling (fill plot box with data).
# 'normal'	Same as 'auto'; deprecated.
# 'image'	'scaled' with axis limits equal to data limits.
# 'square'	Square plot; similar to 'scaled', but initially forcing xmax-xmin = ymax-ymin.

def init():
    global im
    retval, frame = cap.read() # 첫 프레임 캡처
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
##    return im,

def updateFrame(k):   # k가 뭔지 모르겠음....
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

ani = animation.FuncAnimation(fig, updateFrame, init_func=init, interval=50)
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

plt.show()
if cap.isOpened():
    cap.release()
