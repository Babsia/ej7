class Hora:
    __hora=''
    __min=''
    __segundos=''
    def __init__(self,h,m,s):
        self.__hora=h
        self.__min=m
        self.__segundos=s
    def Mostrar(self):
        print("hora:{} minutos:{} segundos:{}".format(self.__hora,self.__min,self.__segundos))
    def geth(self):
        return self.__hora
    def getm(self):
        return self.__min
    def gets(self):
        return self.__segundos
