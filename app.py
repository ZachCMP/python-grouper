from tkinter import *

from lib.gui.InputInterface import InputInterface
from lib.gui.OutputInterface import OutputInterface
from lib.make_groups import make_groups

class App:
  def __init__(self):
    self.root = Tk()
    self.root.title('Player Grouper')

    self.player_list = []
    self.group_list = []
    self.group_size = 4

    self.input_gui = InputInterface(self.root, self.group_size, self.submit)
    self.output_gui = OutputInterface(self.root)

    self.root.mainloop()

  def submit(self, player_list, group_size):
    self.player_list = player_list
    self.group_list = make_groups(player_list, group_size)
    self.output_gui.set_groups(self.group_list)


app = App()