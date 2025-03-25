import tkinter as tk
from tkinter import ttk, messagebox

class SistemaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro de Produtos")
        self.root.configure(bg='#f0f0f0')
        self.center_window()
        root.after(100, lambda: root.iconbitmap("icone.ico"))
        self.root.resizable(False, False)
        
        # Container principal
        main_container = ttk.Frame(self.root, padding="20 20 20 20")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Frame para entrada de dados
        input_frame = ttk.LabelFrame(main_container, text="Cadastro de Produtos", style="Custom.TLabelframe")
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Estilo personalizado
        style = ttk.Style()
        style.configure("Custom.TLabelframe", font=('Arial', 10, 'bold'))
        style.configure("TButton", font=('Arial', 10))
        
        # Campos de entrada
        ttk.Label(input_frame, text="Código:", font=('Arial', 10)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_codigo = ttk.Entry(input_frame, width=20, font=('Arial', 10))
        self.entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(input_frame, text="Descrição:", font=('Arial', 10)).grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_descricao = ttk.Entry(input_frame, width=40, font=('Arial', 10))
        self.entry_descricao.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        
        # Frame para botões
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=1, column=0, columnspan=4, pady=10)
        
        # Botões com estilo
        btn_style = {'width': 15, 'style': 'TButton'}
        
        self.btn_adicionar = ttk.Button(btn_frame, text="Adicionar", command=self.adicionar_produto, **btn_style)
        self.btn_adicionar.pack(side=tk.LEFT, padx=5)
        
        self.btn_modificar = ttk.Button(btn_frame, text="Modificar", command=self.modificar_produto, **btn_style)
        self.btn_modificar.pack(side=tk.LEFT, padx=5)
        

        self.btn_remover = ttk.Button(btn_frame, text="Remover", command=self.limpar_campos_produto, **btn_style)
        self.btn_remover.pack(side=tk.LEFT, padx=5)
        
        self.btn_exibir = ttk.Button(btn_frame, text="Atualizar", command=self.limpar_campos_produto, **btn_style)
        self.btn_exibir.pack(side=tk.LEFT, padx=5)

        # Frame para listagem de produtos
        list_frame = ttk.LabelFrame(main_container, text="Lista de Produtos", style="Custom.TLabelframe")
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview com scrollbar
        self.tree_produtos = ttk.Treeview(list_frame, columns=("codigo", "descricao"), show="headings", height=10)
        
        # Define as colunas
        self.tree_produtos.heading("codigo", text="Código")
        self.tree_produtos.heading("descricao", text="Descrição")
        
        # Configuração do tamanho das colunas
        self.tree_produtos.column("codigo", width=100, anchor="center")
        self.tree_produtos.column("descricao", width=400)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree_produtos.yview)
        self.tree_produtos.configure(yscrollcommand=scrollbar.set)
        
        # Posicionamento
        self.tree_produtos.pack(side="left", fill="both", expand=True, padx=(0, 10))
        scrollbar.pack(side="right", fill="y")
        
        # Bind de seleção para modificar
        self.tree_produtos.bind("<<TreeviewSelect>>", self.selecionar_produto)
        
        # Item selecionado para modificação
        self.item_selecionado = None
    
    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = 700
        height = 500

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    
    def adicionar_produto(self):
        codigo = self.entry_codigo.get()
        descricao = self.entry_descricao.get()
        
        if codigo and descricao:
            self.tree_produtos.insert("", "end", values=(codigo, descricao))
            self.limpar_campos_produto()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
    
    def modificar_produto(self):
        if not self.item_selecionado:
            messagebox.showwarning("Atenção", "Selecione um produto para modificar.")
            return
        
        codigo = self.entry_codigo.get()
        descricao = self.entry_descricao.get()
        
        if codigo and descricao:
            # Atualiza o item na Treeview
            self.tree_produtos.item(self.item_selecionado, values=(codigo, descricao))
            self.limpar_campos_produto()
            self.item_selecionado = None
            messagebox.showinfo("Sucesso", "Produto modificado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
    
    def selecionar_produto(self, event):
        # Obtém o item selecionado
        selected_item = self.tree_produtos.selection()
        
        if selected_item:
            # Salva a referência do item selecionado
            self.item_selecionado = selected_item[0]
            
            # Obtém os valores do item
            valores = self.tree_produtos.item(selected_item)['values']
            
            # Preenche os campos de entrada
            self.entry_codigo.delete(0, tk.END)
            self.entry_codigo.insert(0, valores[0])
            
            self.entry_descricao.delete(0, tk.END)
            self.entry_descricao.insert(0, valores[1])
    
    def limpar_campos_produto(self):
        self.entry_codigo.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.item_selecionado = None

def main():
    root = tk.Tk()
    
    app = SistemaCadastro(root)
    root.mainloop()

if __name__ == "__main__":
    main()