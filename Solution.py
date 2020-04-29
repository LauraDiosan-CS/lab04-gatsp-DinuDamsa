class Solution:
    def __init__(self, path, value):
        self.__path = path
        self.__value = value

    def getPath(self):
        return self.__path

    def getValue(self):
        return self.__value

    def __str__(self):
        return str(len(self.__path)) + "\n" + self.__pathString() + str(self.__value)

    def __pathString(self):
        ret = ""
        for el in self.__path:
            ret += str(el + 1) + ","
        return ret[:len(ret) - 1] + "\n"
