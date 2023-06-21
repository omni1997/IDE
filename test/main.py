import tkinter as tk
from tkinter import scrolledtext

FONT = ('Courier', 14)

key_active = [False] * 27

def press(event):
    #print('p <', event.char, '>')
    c = event.keysym
    if len(c) != 1: return
    i = ord(c) - 97
    if i < len(key_active):
        key_active[i] = True
        
def release(event):
    #print('r <', event.char, '>')
    c = event.keysym
    if len(c) != 1: return
    i = ord(c) - 97
    if i < len(key_active):
        key_active[i] = True
"""
def print_value(root):
    values = str()
    for i, v in enumerate(key_active):
        if v:
            values += chr(i+97)
    print(f'<{values}>', end='\r')
    root.after(100, lambda: print_value(root))
"""

print('[START]')
root = tk.Tk()
text_box = scrolledtext.ScrolledText(root, width=40, height=10, font=FONT)
text_box.pack(fill=tk.BOTH, expand=True)
text_box.bind('<KeyPress>', press)
text_box.bind('<KeyRelease>', release)
root.bind('<Escape>',lambda e: root.quit())
#print_value(root)
root.mainloop()
print('[ END ]')
