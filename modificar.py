import subprocess

# Função para coletar o produto
def coletar_codigo():
    codigo = input("Digite o código do produto que deseja modificar o nome: ")
    return codigo

def coletar_nome_produto():
    nome = input("Digite o novo nome do produto: ")
    return nome


# Função para salvar o produto em um arquivo temporário
def salvar_codigo(produto, arquivo="temporario.txt"):
    with open(arquivo, "w") as f:
        f.write(produto)

def salvar_delimitador(arquivo="temporario.txt"):
    with open(arquivo, "a") as f:
        f.write(";")

def salvar_nome(produto, arquivo="temporario.txt"):
    with open(arquivo, "a") as f:
        f.write(produto)

# Função para chamar o script .bat
def executar_bat():
    comando = "modificar.bat"  # Nome do script .bat
    subprocess.run(comando, shell=True)
   
def executar_bat_leitura():
    comando = "leitura.bat"  # Nome do script .bat
    subprocess.run(comando, shell=True)



# Fluxo principal
if __name__ == "__main__":
    executar_bat_leitura()
    codigo = coletar_codigo()  # Coleta o produto
    nome = coletar_nome_produto()
    salvar_codigo(codigo)      # Salva o produto em um arquivo
    salvar_delimitador()
    salvar_nome(nome)
    executar_bat()               # Chama o script .bat
    