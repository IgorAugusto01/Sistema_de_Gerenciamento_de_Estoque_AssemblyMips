import subprocess
import tkinter as tk
from tkinter import messagebox
import os

def executar_assembly():
    try:
        print("Executando o arquivo .bat...")
        resultado = subprocess.run(
            ["executar.bat"],  # Caminho completo se necessário
            capture_output=True,
            check=True,
        )

        # Decodifica a saída manualmente, tratando erros de codificação
        stdout = resultado.stdout.decode("cp1252", errors="replace")
        stderr = resultado.stderr.decode("cp1252", errors="replace")

        print("Arquivo .bat executado com sucesso.")
        print("Saída do terminal:", stdout)

        # Exibe a saída do terminal na interface gráfica
        saida_texto.delete(1.0, tk.END)
        if stdout:
            saida_texto.insert(tk.END, stdout)
        else:
            saida_texto.insert(tk.END, "Nenhuma saída foi gerada.")

    except subprocess.CalledProcessError as e:
        print("Erro ao executar o arquivo .bat:", stderr)
        messagebox.showerror("Erro", f"Erro ao executar o Assembly:\n{stderr}")
        
# Cria a interface gráfica
root = tk.Tk()
root.title("Interface Gráfica com MIPS Assembly")

# Botão para executar o Assembly
botao_executar = tk.Button(root, text="Executar Assembly", command=executar_assembly)
botao_executar.pack(pady=10)

# Área de texto para exibir a saída do terminal
saida_texto = tk.Text(root, height=20, width=80)
saida_texto.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()