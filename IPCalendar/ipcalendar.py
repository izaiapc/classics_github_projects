import tkinter as tk

def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except:
        resultado.set("Erro")

root = tk.Tk()
root.title("Calculadora")

entrada = tk.Entry(root, width=20, font=("Arial", 14))
entrada.grid(row=0, column=0, columnspan=4)

botao_1 = tk.Button(root, text="1", command=lambda: entrada.insert(tk.END, "1"))
botao_1.grid(row=1, column=0)
botao_2 = tk.Button(root, text="2", command=lambda: entrada.insert(tk.END, "2"))
botao_2.grid(row=1, column=1)
botao_3 = tk.Button(root, text="3", command=lambda: entrada.insert(tk.END, "3"))
botao_3.grid(row=1, column=2)
botao_soma = tk.Button(root, text="+", command=lambda: entrada.insert(tk.END, "+"))
botao_soma.grid(row=1, column=3)

botao_4 = tk.Button(root, text="4", command=lambda: entrada.insert(tk.END, "4"))
botao_4.grid(row=2, column=0)
botao_5 = tk.Button(root, text="5", command=lambda: entrada.insert(tk.END, "5"))
botao_5.grid(row=2, column=1)
botao_6 = tk.Button(root, text="6", command=lambda: entrada.insert(tk.END, "6"))
botao_6.grid(row=2, column=2)
botao_subtracao = tk.Button(root, text="-", command=lambda: entrada.insert(tk.END, "-"))
botao_subtracao.grid(row=2, column=3)

botao_7 = tk.Button(root, text="7", command=lambda: entrada.insert(tk.END, "7"))
botao_7.grid(row=3, column=0)
botao_8 = tk.Button(root, text="8", command=lambda: entrada.insert(tk.END, "8"))
botao_8.grid(row=3, column=1)
botao_9 = tk.Button(root, text="9", command=lambda: entrada.insert(tk.END, "9"))
botao_9.grid(row=3, column=2)
botao_multiplicacao = tk.Button(root, text="*", command=lambda: entrada.insert(tk.END, "*"))
botao_multiplicacao.grid(row=3, column=3)

botao_limpar = tk.Button(root, text="C", command=lambda: entrada.delete(0, tk.END))
botao_limpar.grid(row=4, column=0)
botao_0 = tk.Button(root, text="0", command=lambda: entrada.insert(tk.END, "0"))
botao_0.grid(row=4, column=1)
botao_igual = tk.Button(root, text="=", command=calcular)
botao_igual.grid(row=4, column=2)
botao_divisao = tk.Button(root, text="/", command=lambda: entrada.insert(tk.END, "/"))
botao_divisao.grid(row=4, column=3)

resultado = tk.StringVar()
resultado_label = tk.Label(root, textvariable=resultado, font=("Arial", 14))
resultado_label.grid(row=5, column=0, columnspan=4, sticky="we")

root.mainloop()
