import random

from pygments.lexers import q


class Model(object):
    def __init__(self):
        self._nmax=100
        self._tmax=6
        self._t=self._tmax
        self._segreto=None
        self.reset()



    def reset(self):
        """azzzera stato del gioco, imposta segreto tra 0 e nmax e riazzera i tentativi"""
        self._segreto=random.randint(0,self._nmax)
        self._t=self._tmax
        print(self._segreto)

    def play(self,tentativo):
        """metodo riceve un valore intero che è tentativo e confronta con segreto,
        restituendo -1 (se più piccolo), 0 (se uguale), 1 (se maggiore) o 2 (no tentativi rimasti)"""
        self._t-=1
        if tentativo==self._segreto:
            return 0
        elif self._t==0:
            return 2
        elif tentativo>self._segreto:
            return -1
        else:
            return 1

    @property
    def nmax(self):
        return self._nmax
    @property
    def tmax(self):
        return self._tmax
    @property
    def t(self):
        return self._t
    @property
    def segreto(self):
        return self._segreto

if __name__=="__main__":
    m=Model()
    print(m.reset())
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(40))
    print(m.play(50))
    print(m.play(60))