.data
arquivo_produtos: .asciiz "produtos2.txt"  # Arquivo de produtos
arquivo_temporario: .asciiz "temporario.txt"  # Arquivo temporário com a string a ser removida
arquivo_auxiliar: .asciiz "auxiliar.txt"  # Arquivo auxiliar para escrita
produto_remover: .space 1024  # Buffer para armazenar a string a ser removida
linha_procura: .space 1024  # Buffer para armazenar cada linha do arquivo de produtos
cod: .byte 0  # Buffer temporário para armazenar um caractere

.text
.globl main

main:
   













# numero de bytes do produto remover for diferente dos lidos, proxima linha, escreve no arquivo auxiliar
#