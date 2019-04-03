data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f: # 將檔案中每一串留言叫出來
        data.append(line)   # 將每串留言放入data清單中
        count += 1  # count = count + 1
        if count % 10000 == 0: # 當餘數=0則印出
            print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料!')

print(data[0])  # 印出第1筆留言

# 文字記數

wc = {} # word_count

for d in data:              # 將清單中每筆留言呼叫出來
    words = d.split()       # 將留言中每個字切割成一個清單
    for word in words:      # 將清單中每個字呼叫出來
        if word in wc:      # 若字有出現在wc字典中
            wc[word] += 1   # 則將字典中這個word的值+1
        else:               # 若字沒出現在wc字典中
            wc[word] = 1    # 則將字典中這個word的值設為1放入字典中
for word in wc:
    if wc[word] > 10000:    # 字典中key的值超過 10000
        print(word, wc[word])   # 印出key跟value(當查詢wc的key時,會印出key的值)
print(len(wc))              # 字典中key的數量加總
print(wc['Allen'])          # 印出字典中Allen的次數(value)

# 設計一個迴圈
while True:
    word = input('請輸入要查找的單字:') # 將輸入的值代入變數word中
    if word == 'q':
        break   # 跳出迴圈
    if word in wc:  # 若字典中有word變數
        print(word, '出現的使用次數為:', wc[word])  # 顯示key跟value(次數加總)
    else:
        print('這個字不存在!')  # 印出不存在的訊息
print('感謝使用本查詢功能') # 結束通知



