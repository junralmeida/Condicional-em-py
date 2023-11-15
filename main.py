salario = float(input('Digite seu salário:'))
prestacao_emprestimo = float(input('Digite o valor da prestação:'))
porcetagem_salario_emprestimo = (prestacao_emprestimo * 100) / salario
limite_prestacao = 0.2 * salario

if prestacao_emprestimo > limite_prestacao:
    print('Emprestimo não cedido')

else:
    print('Emprestimo cedido')

print(f'Porcentagem do salário em relação a pretação do empréstimo:{porcetagem_salario_emprestimo:.2f}%')