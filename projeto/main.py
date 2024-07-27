import print_reprograma as pr

opcao = " "
while(opcao != "s"):
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado I\nTerminal de vendas', tamanho=120, cor_barra="magenta", cor_texto="azul")
    pr.separador(120, cor_texto="azul")
    pr.imprimir("[S] Sair", tamanho=110, alinhar="fim", caracter="═", end="┤")
    opcao = input().lower()