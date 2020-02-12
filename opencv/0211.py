# 0211.py
import cv2
import matplotlib.pyplot as plt
#1
def handle_key_press(event):
    if event.key == 'escape':
        cap.release()   #cap 닫기
        plt.close()     #plt 닫기
def handle_close(evt):  # x 눌렀을경우
    print('Close figure!')
    cap.release()
#2 프로그램 시작
cap = cv2.VideoCapture('./data/vtest.avi') # 0번 카메라
#cap = cv2.VideoCapture(0) # 0번 카메라
plt.ion() # 대화모드 설정
# 대화형 모드는 ipython 및 일반 Python 쉘에서 적절한 백엔드와 함께 작동하지만 IDLE IDE에서는 작동하지 않는다.
# 기본 백엔드가 상호작용성을 지원하지 않는 경우, 백엔드란 무엇인가?에서 논의된 방법 중 하나를 사용하여
# 대화형 백엔드를 명시적으로 활성화할 수 있다.
fig = plt.figure(figsize=(10, 6))
# figsize : 2-tuple of floats, default: rcParams["figure.figsize"] (default: [6.4, 4.8])
#           Figure dimension (width, height) in inches.
# dpi : float, default: rcParams["figure.dpi"] (default: 100.0)
#        Dots per inch.
# facecolor : default: rcParams["figure.facecolor"] (default: 'white')
#        The figure patch facecolor.
# edgecolor : default: rcParams["figure.edgecolor"] (default: 'white')
#        The figure patch edge color.
# linewidth : float
#        The linewidth of the frame (i.e. the edge linewidth of the figure patch).
# frameon : bool, default: rcParams["figure.frameon"] (default: True)
#        If False, suppress drawing the figure background patch.
# subplotpars : SubplotParams
#   Subplot parameters. If not given, the default subplot parameters rcParams["figure.subplot.*"] are used.
# # tight_layout : bool or dict, default: rcParams["figure.autolayout"] (default: False)
#
# constrained_layout : bool
# fig.set_size_inches(10, 6)
# figure 함수를 통해 figure 객체 만들기
plt.axis('off')  # 픽셀값 안보여주기
#ax = fig.gca()
#ax.set_axis_off()
fig.canvas.set_window_title('Video Capture')
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)
retval, frame = cap.read() # 첫 프레임 캡처
# 제대로 프레임을 읽으면 ret값이 True, 실패하면 False가 나타납니다. fram에 읽은 프레임이 나옵니다
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#3
while True:
    retval, frame = cap.read() # 프레임 캡처
    if not retval:
        break
#    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    fig.canvas.draw()
#   fig.canvas.draw_idle()
    fig.canvas.flush_events()  # plt.pause(0.001)
if cap.isOpened():
    cap.release()