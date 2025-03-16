import subprocess

# Função para coletar o produto
def coletar_produto():
    produto = input("Digite o produto que deseja deletar: ")
    return produto

# Função para salvar o produto em um arquivo temporário
def salvar_produto(produto, arquivo="temporario2.txt"):
    with open(arquivo, "w") as f:
        f.write(produto)

# Função para chamar o script .bat
def executar_bat():
    comando = "remocao.bat"  # Nome do script .bat
    subprocess.run(comando, shell=True)

# Fluxo principal
if __name__ == "__main__":
    produto = coletar_produto()  # Coleta o produto
    salvar_produto(produto)      # Salva o produto em um arquivo
    executar_bat()               # Chama o script .bat