import tkinter as tk
from tkcalendar import Calendar

def show_calendar():
    cal = Calendar(root, selectmode='day', year=2024, month=4, day=14)
    cal.pack(fill='both', expand=True)

root = tk.Tk()
root.title("Calendário Interativo")

menu_frame = tk.Frame(root)
menu_frame.pack(side='top', fill='x')

day_btn = tk.Button(menu_frame, text='Dia', command=lambda: print("Visualização do Dia"))
day_btn.pack(side='left')

week_btn = tk.Button(menu_frame, text='Semana', command=lambda: print("Visualização da Semana"))
week_btn.pack(side='left')

month_btn = tk.Button(menu_frame, text='Mês', command=show_calendar)
month_btn.pack(side='left')

year_btn = tk.Button(menu_frame, text='Ano', command=lambda: print("Visualização do Ano"))
year_btn.pack(side='left')

note_frame = tk.Frame(root)
note_frame.pack(side='bottom', fill='both', expand=True)

note_label = tk.Label(note_frame, text="Escreva sua nota:")
note_label.pack(side='top')

note_entry = tk.Text(note_frame, height=10)
note_entry.pack(side='top', fill='both', expand=True)

root.mainloop()
