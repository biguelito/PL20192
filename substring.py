# sub = input()
# for i in range(len(sub)):
#     for j in range(i+1, len(sub)+1):
#         print(sub[i:j])

# sub = input()
# k = 0
# final = len(sub)
# for i in range(1, (final**2)+1):
#     if i % final == 0:
#         print(sub[k:final+1])
#         k += 1
#     elif k >= i % final:
#         continue
#     else:
#         print(sub[k:i % final])

# def substring(sub, x = 0, y= 1):
#     if y == len(sub)+1:
#         x += 1
#         y = x + 1
#     print(sub[x:y])
#     if x == len(sub)-1:
#         return None
#     y += 1
#     return substring(sub, x, y)
#
# substring(input())
