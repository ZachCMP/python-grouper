from tkinter import *
from tkinter import ttk
class OutputInterface:
  def __init__(self, master, groups=[]):
    self.master = master
    self.groups = groups
    self.default_width = 20
    self.frame = LabelFrame(master, text="Groups", padx=10, pady=10, bd=2, relief=RAISED)
    self.frame.pack(padx=10, pady=10, fill=Y, side=LEFT)

    self.groups_frame = Frame(self.frame, width=self.default_width)
    self.groups_frame.pack()

    self.group_frames = []

    self.refresh_groups()

  def refresh_groups(self):
    for frame in self.group_frames:
      frame.destroy()

    self.group_frames = []

    for i, group in enumerate(self.groups):
      frame = LabelFrame(self.groups_frame, text='Group {}'.format(i + 1), padx=10 )
      frame.pack(fill=BOTH, expand=1)

      for player in group:
        label = Label(frame, text=player)
        label.pack()

      self.group_frames.append(frame)

  def set_groups(self, groups):
    self.groups = groups
    self.refresh_groups()