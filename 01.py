'''
定义一个学生类，用来形容学生

'''
#定义一个空的类
class Stundet():
    # 一个空类，pass代表直接跳过
    #此处pass 必须有
    pass

#定义一个对象
xinxin = Stundet()

#定义一个类，用来描述python 的同学
class PythonStundent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "python"

    # 雪要注意
    #1.def Homework的缩进层级
    #2.系统默认由一个self参数
    def doHomework(self):
        print("在做作业！")

        # 推荐在函数末尾使用return语句
        return None

#实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStundent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传入参数
yueyue.doHomework()