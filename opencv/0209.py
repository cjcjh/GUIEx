# 0209.py
'''
 pip install youtube_dl
 pip install pafy
'''
import cv2, pafy
url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)   # pafy 할 객체 선언
# pafy.new(video_url[, basic=True][, gdata=False][, signature=True][, size=False][, callback=None])
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest(preftype='mp4')     # 'mp4','3gp','webm','flv'
print('best.resolution', best.resolution)  # best.resolution 이 안나옴......흠......

cap=cv2.VideoCapture(best.url)
while(True):
        retval, frame = cap.read()
        if not retval:
                break
        cv2.imshow('frame', frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,100,200)
        # cv2.Canny(img, 100: minimum thresholding value, 200: maximum thresholding value)
        cv2.imshow('edges', edges)

        key = cv2.waitKey(25)
        if key == 27: # Esc
                break
cv2.destroyAllWindows()
