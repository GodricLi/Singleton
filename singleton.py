# _*_ coding=utf-8 _*_


# 单例模式
# 重写__new__方法
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        # 关键在于每一次实例化，我们都返回这同一个instance对象
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()
print(id(a))
print(id(b))


# 使用元类
# 基于元类实现单例模式,比如数据库对象,实例化时参数都一样,就没必要重复产生对象,浪费内存
class Meta(type):

    def __init__(self, name, bases, class_dict):
        super(Meta, self).__init__(name, bases, class_dict)
        self._instance = None

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Meta, self).__call__(*args, **kwargs)
        return self._instance


class MetaClass(metaclass=Meta):
    def __init__(self, host='127.0.0.1', port='3306'):
        self.host = host
        self.port = port


c = MetaClass()
d = MetaClass()
print(id(c))
print(id(d))
