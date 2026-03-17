from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNmax(self):
        return self._model.nmax

    def getTmax(self):
        return self._model.tmax

    def reset(self,e):
        self._model.reset()
        self._view.txtT.value=str(self._model.t)
        self._view.lvOut.controls.clear()
        self._view.lvOut.controls.append(ft.Text("Inizia il gioco, indovina l numero a cui sto pensando"))
        self._view.update()


    def play(self,e):
        tentativoStr=self._view.txtInTentativo.value
        try:
            tentativo=int(tentativoStr)
        except ValueError:
            self._view.lvOut.controls.append(ft.Text("Errore, solo valori numerici"))
            self._view.update()
            return
        valore=self._model.play(tentativo)
        self._view.txtT.value = str(self._model.t)
        self._view.txtInTentativo.value = ""
        if valore==-1:
            self._view.lvOut.controls.append(ft.Text(f"Ritenta, il numero segreto è < di {tentativo}"))
            self._view.update()
            return
        elif valore==0:
            self._view.lvOut.controls.append(ft.Text(f"Bravo, hai indovinato! il valore corretto era {tentativo}",color="green"))
            self._view.update()
            return
        elif valore==1:
            self._view.lvOut.controls.append((ft.Text(f"Ritenta, il numero segreto è > di {tentativo}")))
            self._view.update()
            return
        else:
            self._view.lvOut.controls.append(ft.Text(f"Hai perso, il valore corretto era {self._model.segreto}",color="red"))
            self._view.update()
            return