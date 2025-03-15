.data
buffer: .space 1024        # Buffer para armazenar o produto
newline: .asciiz "\n"      # Nova linha
output: .asciiz "Produto recebido: "  # Mensagem de saída
filename: .asciiz "produto.txt"  # Nome do arquivo temporário
file_error: .asciiz "Erro ao abrir o arquivo.\n"

.text
.globl main
main:
    # Abre o arquivo para leitura
    li $v0, 13             # Syscall para abrir arquivo
    la $a0, filename       # Nome do arquivo
    li $a1, 0              # Modo de leitura (0 = leitura)
    li $a2, 0              # Modo de permissão (não usado para leitura)
    syscall
    bltz $v0, error        # Se $v0 < 0, ocorreu um erro

    move $s0, $v0          # Salva o descritor do arquivo em $s0

    # Lê o conteúdo do arquivo
    li $v0, 14             # Syscall para ler arquivo
    move $a0, $s0          # Descritor do arquivo
    la $a1, buffer         # Buffer para armazenar o conteúdo
    li $a2, 1024           # Número máximo de bytes a serem lidos
    syscall

    # Fecha o arquivo
    li $v0, 16             # Syscall para fechar arquivo
    move $a0, $s0          # Descritor do arquivo
    syscall

    # Imprime a mensagem "Produto recebido:"
    li $v0, 4
    la $a0, output
    syscall

    # Imprime o produto recebido
    li $v0, 4
    la $a0, buffer
    syscall

    # Imprime uma nova linha
    li $v0, 4
    la $a0, newline
    syscall

    # Finaliza o programa
    li $v0, 10
    syscall

error:
    # Exibe mensagem de erro
    li $v0, 4
    la $a0, file_error
    syscall

    # Finaliza o programa
    li $v0, 10
    syscall