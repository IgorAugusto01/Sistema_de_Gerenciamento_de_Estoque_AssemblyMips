import tkinter as tk
import os
import subprocess
from tkinter import ttk, messagebox, simpledialog

class SistemaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Estoque")
        self.root.configure(bg='#f0f0f0')
        self.centralizar_janela(self.root, 700, 500)
        root.after(100, lambda: root.iconbitmap("icone.ico"))
        self.root.resizable(False, False)
        
        # main
        main_container = ttk.Frame(self.root, padding="20 20 20 20")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        style = ttk.Style()
        style.configure("Custom.TLabelframe", font=('Arial', 10, 'bold'))
        style.configure("TButton", font=('Arial', 10))

        #lista de produto
        list_frame = ttk.LabelFrame(main_container, text="Lista de Produtos", style="Custom.TLabelframe")
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree_produtos = ttk.Treeview(list_frame, columns=("codigo", "descricao"), show="headings", height=10)
        
        self.tree_produtos.heading("codigo", text="Código")
        self.tree_produtos.heading("descricao", text="Descrição")
        
        self.tree_produtos.column("codigo", width=100, anchor="center")
        self.tree_produtos.column("descricao", width=400)
        
        #scroll
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree_produtos.yview)
        self.tree_produtos.configure(yscrollcommand=scrollbar.set)
        self.tree_produtos.pack(side="left", fill="both", expand=True, padx=(0, 10))
        scrollbar.pack(side="right", fill="y")

        btn_frame = ttk.Frame(main_container)
        btn_frame.pack(pady=5)
        
        btn_style = {'width': 15, 'style': 'TButton'}
        
        self.btn_adicionar = ttk.Button(btn_frame, text="Adicionar", command=self.abrir_janela_adicionar, **btn_style)
        self.btn_adicionar.pack(side=tk.LEFT, padx=5)
        
        self.btn_modificar = ttk.Button(btn_frame, text="Modificar", command=self.abrir_janela_modificar, **btn_style)
        self.btn_modificar.pack(side=tk.LEFT, padx=5)

        self.btn_remover = ttk.Button(btn_frame, text="Remover", command=self.remover_produto, **btn_style)
        self.btn_remover.pack(side=tk.LEFT, padx=5)

        self.btn_exibir = ttk.Button(btn_frame, text="Exibir", command=self.exibir_produtos, **btn_style)
        self.btn_exibir.pack(side=tk.LEFT, padx=5)
    
    def centralizar_janela(self, janela, lar, alt):
        a = janela.winfo_screenwidth()
        b = janela.winfo_screenheight()

        x = (a / 2) - (lar / 2)
        y = (b / 2) - (alt / 2)

        janela.geometry(f'{lar}x{alt}+{int(x)}+{int(y)}')
    
    def abrir_janela_adicionar(self):
        janela_adicionar = tk.Toplevel(self.root)
        janela_adicionar.after(100, lambda: janela_adicionar.iconbitmap("icone.ico"))
        janela_adicionar.title("Adicionar Produto")
        janela_adicionar.resizable(False, False)
        self.centralizar_janela(janela_adicionar, 300, 150)

        novo_codigo = str(len(self.tree_produtos.get_children()) + 1)

        ttk.Label(janela_adicionar, text="Nome:", font=('Arial', 10)).pack(pady=(21, 5))
        entry_descricao = ttk.Entry(janela_adicionar, width=30, font=('Arial', 10))
        entry_descricao.pack(pady=5)

        # Add upper case conversion while typing
        def converter_maiusculas(*args):
            texto = entry_descricao.get().upper()
            entry_descricao.delete(0, tk.END)
            entry_descricao.insert(0, texto)

        entry_descricao.bind('<KeyRelease>', converter_maiusculas)

        def adicionar():
            descricao = entry_descricao.get()
            
            if descricao:
                # Executa o arquivo de inserção
                try:
                    subprocess.Popen('insercao.bat', shell=True)
                    # Escreve o nome em maiúsculas no arquivo temporario.txt
                    with open('temporario.txt', 'w', encoding='utf-8') as arquivo:
                        arquivo.write(descricao.upper())
                
                    # Insere na árvore de produtos
                    self.tree_produtos.insert("", "end", values=(novo_codigo, descricao))
                    messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao executar insercao.bat: {str(e)}")
                
                janela_adicionar.destroy()
            else:
                messagebox.showwarning("Atenção", "Por favor, preencha o nome!")

        btn_adicionar = ttk.Button(janela_adicionar, text="Adicionar", command=adicionar)
        btn_adicionar.pack(pady=10)
    
    def abrir_janela_modificar(self):
        selected_item = self.tree_produtos.selection()
        
        if not selected_item:
            messagebox.showwarning("Atenção", "Selecione um produto para modificar.")
            return
        
        janela_modificar = tk.Toplevel(self.root)
        janela_modificar.after(100, lambda: janela_modificar.iconbitmap("icone.ico"))
        janela_modificar.title("Modificar Produto")
        janela_modificar.geometry("300x150")
        self.centralizar_janela(janela_modificar, 300, 150)
        janela_modificar.resizable(False, False)

        valores_atual = self.tree_produtos.item(selected_item[0])['values']

        ttk.Label(janela_modificar, text="Novo Produto:", font=('Arial', 10)).pack(pady=(21, 5))
        entry_novo_produto = ttk.Entry(janela_modificar, width=30, font=('Arial', 10))
        entry_novo_produto.pack(pady=5)
        entry_novo_produto.insert(0, valores_atual[1])

        # Add upper case conversion while typing
        def converter_maiusculas(*args):
            texto = entry_novo_produto.get().upper()
            entry_novo_produto.delete(0, tk.END)
            entry_novo_produto.insert(0, texto)

        entry_novo_produto.bind('<KeyRelease>', converter_maiusculas)

        def modificar():
            novo_produto = entry_novo_produto.get()
            
            if novo_produto:
                # Escreve o código e nome no arquivo temporario.txt
                with open('temporario.txt', 'w', encoding='utf-8') as arquivo:
                    arquivo.write(f"{valores_atual[0]};{novo_produto}")
                
                # Atualiza a árvore de produtos
                self.tree_produtos.item(selected_item[0], values=(valores_atual[0], novo_produto))
                
                # Executa o arquivo de modificação
                try:
                    subprocess.Popen('modificar.bat', shell=True)
                    messagebox.showinfo("Sucesso", "Produto modificado com sucesso!")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao executar modificar.bat: {str(e)}")
                
                janela_modificar.destroy()
            else:
                messagebox.showwarning("Atenção", "Por favor, preencha a descrição!")

        btn_modificar = ttk.Button(janela_modificar, text="Modificar", command=modificar)
        btn_modificar.pack(pady=10)
    
    def remover_produto(self):
        selected_item = self.tree_produtos.selection()
        
        if not selected_item:
            messagebox.showwarning("Atenção", "Selecione um produto para remover.")
            return

        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja remover este produto?")
        
        if resposta:
            # Obter os valores do produto selecionado
            valores_produto = self.tree_produtos.item(selected_item[0])['values']
            codigo = valores_produto[0]
            produto = valores_produto[1]

            # Remover da lista de produtos
            self.tree_produtos.delete(selected_item[0])

            # Remover do arquivo produtos.txt
            try:
                with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()
                
                with open('produtos.txt', 'w', encoding='utf-8') as arquivo:
                    for linha in linhas:
                        if f'COD:{codigo};' not in linha:
                            arquivo.write(linha)
                
                # Salvar o código do produto removido em temporario.txt
                with open('temporario.txt', 'w', encoding='utf-8') as arquivo:
                    arquivo.write(f"{codigo}")
                
                # Executa o arquivo de remoção
                subprocess.Popen('remocao.bat', shell=True)
                
                messagebox.showinfo("Sucesso", "Produto removido com sucesso!")
            
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover produto: {str(e)}")

    def exibir_produtos(self):
        #limpando a arvore
        for item in self.tree_produtos.get_children():
            self.tree_produtos.delete(item)

        try:
            with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
                
            for linha in linhas:
                if 'COD:' in linha and 'REMOVIDO' not in linha:
                    # remove o espaço e divide a linha
                    partes = linha.strip().split(';')
                    codigo = partes[0].split(':')[1].strip()
                    produto = partes[1].split(':')[1].strip('|')
                    
                    # aplica na arvore
                    self.tree_produtos.insert("", "end", values=(codigo, produto))
        
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'produtos.txt' não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo: {str(e)}")

def main():
    root = tk.Tk()
    
    app = SistemaCadastro(root)
    root.mainloop()

if __name__ == "__main__":
    main()