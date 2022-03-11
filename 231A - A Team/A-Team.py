view2 = 0
n = int(input())

for i in range(0, n):
    view = input()
    if view.count('1') >= 2:
        view2 += 1

print(view2)
