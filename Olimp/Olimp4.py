# Задача 4: Американские горки
# Аттракцион «Американские горки» представляет собой рельсовый трек, размещённый на опорах. Известна высота каждой опоры. Для рекламы аттракциона необходимо выделить один из его фрагментов (несколько подряд идущих опор с рельсовым треком) световой подсветкой. При этом необходимо выделить такой фрагмент трека, на котором была бы «горка» то есть на выделенном участке трека была бы точка, которая находилась бы строго выше начала и строго выше конца выделенного фрагмента трека.
#
# Владелец аттракциона для экономии хочет найти подходящий участок минимальной длины, удовлетворяющий условию наличию «горки» на этом участке.
#
# Входные данные
# Первая строка входных данных содержит число N – количество опор аттракциона. Следующие N строк содержат информацию о высотах опор при движении от начала к концу аттракциона. Все числа натуральные, не превосходящие 105.
#
# Выходные данные
# Программа должна вывести два числа – номер первой и последней подходящей опоры. Опоры нумеруются числами от 1 до N. Если фрагмента, удовлетворяющего условиям, не существует, программа должна вывести одно число 0. Если подходящих ответов несколько, нужно вывести любой из них.
#
# Система оценивания
# Решение, правильно работающее только для случаев, когда все входные числа не превосходят 100, будет оцениваться в 40 баллов.
#
# В 100 баллов будет оцениваться решение, правильно работающее, когда все числа не превосходят 10^5.

stages = int(input())
stats = []
for i in range(stages):
    stats.append(int(input()))
waves = []

while True:
    maximum = max(stats)
    leftBorder = stats.index(maximum) - 1
    RightBorder = stats.index(maximum) + 1
    while True:
        if stats[leftBorder] > stats[leftBorder - 1] and stats[RightBorder] > stats[RightBorder + 1]:
            waves.append([leftBorder, RightBorder])
            for i in range(RightBorder - leftBorder):
                stats.pop(leftBorder)
        try:
            if stats[leftBorder] == stats[leftBorder - 1]:
                leftBorder -= 1
            if stats[RightBorder] == stats[RightBorder + 1]:
                RightBorder += 1
        except IndexError:
            continue
print(waves)
