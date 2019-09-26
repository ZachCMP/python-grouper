from tkinter import *
class InputInterface:
  def __init__(self, master, group_size, submit):
    self.master = master
    self.group_size = group_size
    self.playerlist = []
    self.submit = submit
    self.frame = LabelFrame(master, text="Players", padx=10, pady=10, bd=2, relief=RAISED)
    self.frame.pack(padx=10, pady=10, side=LEFT)

    # self.label = Label(self.frame, text="Player input", font=('Helvetica', 16))
    # self.label.pack(side=TOP)

    self.listbox = Listbox(self.frame, height=3)
    self.listbox.pack()

    self.message = Label(self.frame, text="Add players using the input box", justify=CENTER)
    self.message.pack(fill=X, expand=YES)

    self.textarea = Entry(self.frame)
    self.textarea.bind("<Return>", self.addplayer)
    self.textarea.pack()

    self.button_frame = Frame(self.frame)
    self.button_frame.pack()

    self.add_button = Button(self.button_frame, text="Add Player", command=self.addplayer)
    self.add_button.pack(side='left')

    self.remove_button = Button(self.button_frame, text="Remove Player", command=self.removeplayer)
    self.remove_button.pack(side='right')

    self.group_size_frame = Frame(self.frame)
    self.group_size_frame.pack(pady=10)

    self.group_size_label = Label(self.group_size_frame, text="Max Group Size", font=('Helvetica', 14))
    self.group_size_label.pack()

    self.group_size_entry = Entry(self.group_size_frame, justify=CENTER)
    self.group_size_entry.pack()
    self.group_size_entry.insert(0, str(self.group_size))

    self.submit_button = Button(self.frame, text="Submit Players", command=self.submit_players)
    self.submit_button.pack()

    self.refresh_list()
    # self.close_button = Button(self.frame, text="Submit Players", command=master.quit)
    # self.close_button.pack()

  def submit_players(self):
    group_size = self.group_size_entry.get()
    self.submit(self.playerlist, int(group_size))

  def refresh_list(self):
    self.listbox.delete(0, END)
    if (len(self.playerlist) > 2):
      self.listbox['height'] = len(self.playerlist) + 1
    else:
      self.listbox['height'] = 3
    for item in self.playerlist:
      self.listbox.insert(END, item)

  def removeplayer(self):
    ind = self.listbox.curselection()[0]
    self.playerlist.pop(ind)
    self.refresh_list()

  def addplayer(self, event=None):
    text = self.textarea.get()
    if (text.strip() != ''):
      self.playerlist.append(text)
      self.textarea.delete(0, END)
      self.refresh_list()