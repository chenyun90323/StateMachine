'''
状态机模型
'''
class StateMachine:
    def __init__(self):
        self.__handlers = {}        # 状态转移函数字典
        self.__state = None         # 目前状态

    # 参数name为状态名,handler为状态转移函数,end_state表明是否为最终状态
    def add_state(self, name, handler, end_state=0):
        name = name.upper() # 转换为大写
        self.__handlers[name] = handler

    def set_start(self, name):
        name = name.upper() # 转换为大写
        self.__state = name

    def state(self):
        return self.__state

    def run(self, arg=None):
        try:
            handler = self.__handlers[self.__state]
        except:
            raise Exception("must call .set_start() before .run()")

        self.__state = handler(arg).upper()
        return self.__state     # 经过状态转移函数变换到新状态

'''
测试
'''
def S(arg=None):
    return 'e'

def E(arg=None):
    return 's'

if __name__ == '__main__':
    sm = StateMachine()
    sm.add_state('s', S)
    sm.add_state('e', E)
    sm.set_start('s')

    print(sm.state())
    sm.run()
    print(sm.state())
    sm.run()
    print(sm.state())
