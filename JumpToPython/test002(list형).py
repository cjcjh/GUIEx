a = [1, 2, 3, 4, 5]
b = a[1:3]  #슬라이싱 기법으로 리스트생성
print(b)
print(a)
del a[2:]   #list 요소 삭제
print(a)
a.append(0)  # list 요소 추가
print(a)
a.sort() # 요소 정렬
print(a)
a.reverse() # list 역순으로 뒤집기
print(a)
print(a.index(0)) # 요소 위치 반환 : index
a.insert(0, 4) # 첫번째 요소(0)에 값(4) 삽입
print(a)
a.remove(1)  # 요소중에 맨처음 나오는 값(1) 삭제
print(a)
#a.pop()     # 리스트의 맨 마지막 요소 돌려주고 그 요소 삭제
a.pop(1)    # 2번째 요소 뽑아 삭제
print(a)
print(a.count(0))  # 요소 = 0 의 개수
#a.extend([8, 2, 7]) # a리스트에 리스트 추가
a += [8,2,7]    #윗줄과 같음
print(a)


