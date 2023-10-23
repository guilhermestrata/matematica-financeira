import math
import statistics

nums = [8,5,4,4,3,6,2,4,7,6,6,5,4,8,9,7,6,6,5,5,5,2,4,3,3]

def somar(nums):
    soma = 0
    for n in nums:
        soma = soma + n
    return soma
ma = (somar(nums))/len(nums)

lista_form = []
for i in range(len(nums)):
    xi = (nums[i] - ma)**2
    # print(f'{xi:,.4f}')
    lista_form.append(xi)
x = math.sqrt(sum(lista_form)/len(nums))
dm = sum(lista_form)/len(nums)

print(f'Média Aritmética: {ma}')
print(f'Desvio Padrão: {x:,.3f}')
print(f'Mediana da Distribuição: {statistics.median(nums)}')
print(f'Desvio Médio: {dm:,.2f}')


