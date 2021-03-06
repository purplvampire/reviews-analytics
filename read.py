data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        # if count % 1000 == 0:
        #     print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料!')

# 求留言的平均長度
sum_len = 0
for d in data:
    sum_len += len(d) # sum_len = sum_len + len(d)
avg = sum_len / len(data) # 字串的總長/清單的總筆數
print('留言的平均長度為', avg, '個字元')


# print(data[0])
# print('-----------------------------------------------------------------')
# print(data[1])

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')

# 隨機撈出其中一筆留言
import random
x = random.randint(0, len(new))
print('以下是第', x, '筆留言')
print(new[x])

good = []                   # 建立good清單
for d in data:              # 在data清單中取出每一筆留言
    if 'good' in d:         # 如果d留言中有'good'字串(True)
        good.append(d)      # 將該留言加到good清單中
print('一共有', len(good), '筆留言提到Good')

# 隨機撈出其中一筆留言
y = random.randint(0, len(good))
print('這是第', y, '筆留言')
print(good[y])

# 快速篩選list comprehension
# output = [(number-1) for number in reference if number % 2 == 0]
# 輸出=[(運算式or變數) for 字串 in 清單 if 條件式]
 
good = [d for d in data if 'good' in d]
print(len(good)

# 列出True or False
bad = ['bad' in d for d in data]
print(bad)

bad = []
for d in data:
    bad.append('bad' in d)
print(bad)
