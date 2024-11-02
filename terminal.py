import tkinter as tk
from aura_commands import execute_command

root = tk.Tk()
root.title("Aura Virtual Router")
root.geometry("600x400")

text_area = tk.Text(root, wrap='word', bg='black', fg='white', font=('Courier', 12), insertbackground='white')
text_area.pack(expand=True, fill='both')

def execute_command_from_input(event):
    input_text = text_area.get("end-2c linestart", "end-1c").strip()
    if input_text.startswith("aura "):
        command = input_text[5:].strip()
        response = execute_command(command)
        text_area.insert(tk.END, f"\n{response}\n> ")
    else:
        text_area.insert(tk.END, "\n> ")
    text_area.see(tk.END)

text_area.bind('<Return>', execute_command_from_input)
text_area.insert(tk.END, "> ")
text_area.config(state=tk.DISABLED)
text_area.config(state=tk.NORMAL)

root.mainloop()
