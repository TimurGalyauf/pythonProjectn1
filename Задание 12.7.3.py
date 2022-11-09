
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
test_money = float(input("Планируемая сумма вклада:"))

TKB = 5.6*test_money
CKB = 5.9*test_money
VTB = 4.28*test_money
SBER = 4.0*test_money

deposit_list = [TKB, CKB, VTB, SBER]

print ("Максимальная сумма, которую вы можете заработать-", max(deposit_list))