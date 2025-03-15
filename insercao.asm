.data
arquivo_temporario: .asciiz "temporario.txt"  # Nome do arquivo temporário
arquivo_produtos: .asciiz "produtos.txt"      # Nome do arquivo de produtos
quebra_de_linha: .byte '\n'                   # Caractere de quebra de linha
linha: .space 1024                            # Buffer para armazenar a linha lida

.text
.globl main

main:
    jal ler_arquivo_temporario                 # Chama a função para ler o arquivo temporário
    jal escrever_arquivo_produtos              # Chama a função para escrever no arquivo de produtos
    li $v0, 10                                # Encerra o programa
    syscall

ler_arquivo_temporario:
    # Abrir o arquivo temporário para leitura
    li $v0, 13                                # Código do syscall para abrir arquivo
    la $a0, arquivo_temporario                # Endereço do nome do arquivo
    li $a1, 0                                 # Modo de abertura: leitura (0)
    syscall
    move $s0, $v0                             # Salva o descritor do arquivo em $s0

    # Ler o conteúdo do arquivo
    li $v0, 14                                # Código do syscall para leitura de arquivo
    move $a0, $s0                             # Descritor do arquivo
    la $a1, linha                             # Buffer para armazenar os dados lidos
    li $a2, 1024                              # Número máximo de bytes a serem lidos
    syscall

    # Contar o número de caracteres lidos
    li $t0, 0                                 # Inicializa o contador de caracteres
    la $a1, linha                             # Endereço do buffer de leitura
    jal contar_caracteres                     # Chama a função para contar caracteres

    # Fechar o arquivo temporário
    li $v0, 16                                # Código do syscall para fechar arquivo
    move $a0, $s0                             # Descritor do arquivo
    syscall

    jr $ra                                    # Retorna ao chamador

contar_caracteres:
    loop:
        lb $t1, 0($a1)                        # Carrega o próximo byte do buffer
        beq $t1, $zero, loop_end              # Se for zero (fim da string), sai do loop
        addi $t0, $t0, 1                      # Incrementa o contador de caracteres
        addi $a1, $a1, 1                      # Avança para o próximo byte do buffer
        j loop                                 # Repete o loop
    loop_end:
    jr $ra                                    # Retorna ao chamador

escrever_arquivo_produtos:
    # Abrir o arquivo de produtos para escrita
    li $v0, 13                                # Código do syscall para abrir arquivo
    la $a0, arquivo_produtos                  # Endereço do nome do arquivo
    li $a1, 9                                 # Modo de abertura: escrita com criação (9)
    syscall
    move $s0, $v0                             # Salva o descritor do arquivo em $s0

    # Escrever o conteúdo no arquivo de produtos
    li $v0, 15                                # Código do syscall para escrita em arquivo
    move $a0, $s0                             # Descritor do arquivo
    la $a1, linha                             # Buffer com os dados a serem escritos
    move $a2, $t0                             # Número de caracteres a serem escritos
    syscall

    # Escrever a quebra de linha no arquivo de produtos
    li $v0, 15                                # Código do syscall para escrita em arquivo
    move $a0, $s0                             # Descritor do arquivo
    la $a1, quebra_de_linha                   # Buffer com o caractere de quebra de linha
    li $a2, 1                                 # Número de bytes a serem escritos (1)
    syscall

    # Fechar o arquivo de produtos
    li $v0, 16                                
    move $a0, $s0                             
    syscall

    jr $ra                                   