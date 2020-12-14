##################################################
# Author: Victoralm (Victor Almeida)
# Copyright: Copyright 2020, DesligamentoAgendado.py
## Credits: [Victoralm]
# Version: 1.0.0
## Mmaintainer: Victoralm
###########################################

import os
import platform
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import re


class DeslPC:

    horas = 0
    minutos = 0
    segundos = 0
    #

    def __init__(self, root):
        """
        docstring
        """
        root.title("Desligamento Agendado")

        # Imagem no mesmo diretório do script
        photo = ImageTk.PhotoImage(Image.open("powerdown.png"))
        root.iconphoto(False, photo)

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        """
        Registrando o evento:
        Define que deve executar o método check_num quando o evento ocorre
        """
        check_num_wrapper = (root.register(self.check_num), '%P')

        ttk.Label(mainframe, text="Ajuste em quanto tempo o PC deve ser desligado:", padding="3").grid(
            column=0, row=0, sticky=W, columnspan=6)
        self.horas = StringVar()
        ttk.Label(mainframe, text="Horas", padding="3").grid(
            column=0, row=1, sticky=E, pady=(10, 0))
        """
        validate='key' => Define que o evento é chamado a cada tecla pressionada
        validatecommand=check_num_wrapper => Define qual evento deve ser chamado
        """
        horas_entry = ttk.Entry(mainframe, width=7, textvariable=self.horas,
                                validate='key', validatecommand=check_num_wrapper)
        horas_entry.grid(column=1, row=1, sticky=W, pady=(10, 0))

        self.minutos = StringVar()
        ttk.Label(mainframe, text="Minutos", padding="3").grid(
            column=2, row=1, sticky=E, pady=(10, 0))
        minutos_entry = ttk.Entry(mainframe, width=7, textvariable=self.minutos,
                                  validate='key', validatecommand=check_num_wrapper)
        minutos_entry.grid(column=3, row=1, sticky=W, pady=(10, 0))

        if platform.system() != 'Linux':
            self.segundos = StringVar()
            ttk.Label(mainframe, text="Segundos", padding="3").grid(
                column=4, row=1, sticky=E, pady=(10, 0))
            segundos_entry = ttk.Entry(
                mainframe, width=7, textvariable=self.segundos, validate='key', validatecommand=check_num_wrapper)
            segundos_entry.grid(column=5, row=1, sticky=W, pady=(10, 0))

        ttk.Button(mainframe, text="Agendar Desligamento",
                   command=self.agendarDeslPC).grid(column=0, row=2, sticky=E, columnspan=3, pady=(25, 0))
        ttk.Button(mainframe, text="Cancelar Desligamento",
                   command=self.calcelarDeslPC).grid(column=3, row=2, sticky=E, columnspan=3, pady=(25, 0))

        root.bind("<Return>", self.agendarDeslPC)

    def check_num(self, newval):
        """
        Fazendo a validação das entradas nas entries
        """
        return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5

    def agendarDeslPC(self, *args):
        """
        docstring
        """
        try:
            if not self.horas.get():
                HrInt = 0
            else:
                HrInt = int(self.horas.get())

            if not self.minutos.get():
                MnInt = 0
            else:
                MnInt = int(self.minutos.get())

            if platform.system() != 'Linux':
                if not self.segundos.get():
                    SgInt = 0
                else:
                    SgInt = int(self.segundos.get())

            if HrInt > 0 or MnInt > 0 or SgInt > 0:
                if platform.system() == 'Windows':
                    tempo = int(((HrInt * 60) * 60) + (MnInt * 60) + SgInt)
                    os.system('shutdown -s -t {0}'.format(tempo))

                if platform.system() == 'Linux':
                    tempo = int((HrInt * 60) + MnInt)
                    os.system('shutdown -h {0}'.format(tempo))
        except ValueError:
            pass

    def calcelarDeslPC(self):
        """
        docstring
        """
        try:
            if platform.system() == 'Windows':
                os.system('shutdown -a')
            if platform.system() == 'Linux':
                os.system('shutdown -c')
        except ValueError:
            pass


root = Tk()
DeslPC(root)
root.mainloop()
