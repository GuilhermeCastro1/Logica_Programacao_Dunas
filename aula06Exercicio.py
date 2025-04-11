#Tratamento de notas inválidas
#Condicional composta, entrada pelo usuário
nota = float(input("Qual a nota"))
if nota <= 0 or nota > 10:
    print("Erro: nota inválida. Digite um valor entre 0 a 10.")
elif nota >= 9:
    print("Aprovado")
elif nota >= 7:
    print("Recuperação")
else:
    print("Reprovado")