class father():  # 부모 클래스
    def handsome(self):
        print("잘생겼다")


class brother(father):  # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    '''아들'''


class sister(father):  # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    def pretty(self):
        print("예쁘다")

    def handsome(self):
        '''물려받았어요'''


brother = brother()
print('1')
brother.handsome()
print('2')

girl = sister()
print('3')
girl.handsome()
print('4')
girl.pretty()
print('5')

