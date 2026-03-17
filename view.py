from tkinter.constants import CENTER

import flet as ft
from pygments.lexers import q


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",color="blue", size=24)
        self._page.update()

        self.txtNmax=ft.TextField(label="Numero Max",value=self._controller.getNmax(), disabled=True)
        self.txtTmax=ft.TextField(label="Numero Tentativi massimo", value=self._controller.getTmax(), disabled=True)
        self.txtT=ft.TextField(label="Tentativi Rimanenti", disabled=True)

        self.row1=ft.Row(controls=[self.txtNmax,self.txtTmax,self.txtT])

        self.txtInTentativo=ft.TextField(label="Valore",disabled=False)
        self.btnReset=ft.ElevatedButton(text="Nuova Partita",on_click=self._controller.reset)
        self.play=ft.ElevatedButton(text="Indovina",on_click=self._controller.play)
        self.row2=ft.Row(controls=[self.txtInTentativo,self.btnReset,self.play])

        self.lvOut=ft.ListView(expand=True)
        self.row3=ft.Row(controls=[self.lvOut])

        self._page.add(self.row1,self.row2,self.row3)


    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()