import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class SistemaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Estoque")
        self.root.configure(bg='#f0f0f0')
        self.center_window(self.root, 700, 500)
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
        
        self.tree_produtos = ttk.Treeview(list_frame, columns=("codigo", "descricao"), show="headings", height=10) #scroll
        
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

        self.btn_exibir = ttk.Button(btn_frame, text="Exibir", command=self.remover_produto, **btn_style)
        self.btn_exibir.pack(side=tk.LEFT, padx=5)
    
    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    
    def abrir_janela_adicionar(self):
        janela_adicionar = tk.Toplevel(self.root)
        janela_adicionar.after(100, lambda: janela_adicionar.iconbitmap("icone.ico"))
        janela_adicionar.title("Adicionar Produto")
        janela_adicionar.resizable(False, False)
        self.center_window(janela_adicionar, 300, 150)

        novo_codigo = str(len(self.tree_produtos.get_children()) + 1) #enumerando codigo automaticamente

        ttk.Label(janela_adicionar, text="Nome:", font=('Arial', 10)).pack(pady=(21, 5))
        entry_descricao = ttk.Entry(janela_adicionar, width=30, font=('Arial', 10))
        entry_descricao.pack(pady=5)

        def adicionar():
            descricao = entry_descricao.get()
            
            if descricao:
                self.tree_produtos.insert("", "end", values=(novo_codigo, descricao))
                messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
                janela_adicionar.destroy()
            else:
                messagebox.showwarning("Atenção", "Por favor, preencha o nome!")

        btn_adicionar = ttk.Button(janela_adicionar, text="Adicionar", command=adicionar)
        btn_adicionar.pack(pady=10)
    
    def abrir_janela_modificar(self):
        selected_item = self.tree_produtos.selection() # veerifica se foi selecionado algo
        
        if not selected_item:
            messagebox.showwarning("Atenção", "Selecione um produto para modificar.")
            return
        
        
        janela_modificar = tk.Toplevel(self.root)
        janela_modificar.after(100, lambda: janela_modificar.iconbitmap("icone.ico"))
        janela_modificar.title("Modificar Produto")
        janela_modificar.geometry("300x150")
        self.center_window(janela_modificar, 300, 150)
        janela_modificar.resizable(False, False)

        #valor do item selecionado
        valores_atual = self.tree_produtos.item(selected_item[0])['values']

        # nova descirção
        ttk.Label(janela_modificar, text="Novo Produto:", font=('Arial', 10)).pack(pady=(21, 5))
        entry_novo_produto = ttk.Entry(janela_modificar, width=30, font=('Arial', 10))
        entry_novo_produto.pack(pady=5)
        entry_novo_produto.insert(0, valores_atual[1])  #preenche com descrição atual

        def modificar():
            novo_produto = entry_novo_produto.get()
            
            if novo_produto:
                # atualiza treeview
                self.tree_produtos.item(selected_item[0], values=(valores_atual[0], novo_produto))
                messagebox.showinfo("Sucesso", "Produto modificado com sucesso!")
                janela_modificar.destroy()
            else:
                messagebox.showwarning("Atenção", "Por favor, preencha a descrição!")

        btn_modificar = ttk.Button(janela_modificar, text="Modificar", command=modificar)
        btn_modificar.pack(pady=10)
    
    def remover_produto(self):
        # verifica se tem seleção
        selected_item = self.tree_produtos.selection()
        
        if not selected_item:
            messagebox.showwarning("Atenção", "Selecione um produto para remover.")
            return

        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja remover este produto?")
        
        if resposta:
            self.tree_produtos.delete(selected_item[0])
            messagebox.showinfo("Sucesso", "Produto removido com sucesso!")

def main():
    root = tk.Tk()
    
    app = SistemaCadastro(root)
    root.mainloop()

if __name__ == "__main__":
    main()