# 딕셔너리 = 연관 배열, 해시같은 대응 관계를 나타내는 자료형, key와 value 한쌍으로 갖는 자료형
# = {key1:Value1, key2:Value2, key3:Value3, .......}
# dix = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}

a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)
del a[1]    # key = 1 인 key:value 삭제
print(a)
print(a.get(3)) # key로 value 얻기
print(3 in a)     # 해당 key 가 딕셔너리 안에 있는지 확인
print('3' in a)
print('name' in a)
a.clear()   # key:value 지우기
print(a)

# a.keys = ['name', 'phone', 'birth']
# print(a)
# a.values = (['pey', '0119993323', '1118'])
# print(a)
