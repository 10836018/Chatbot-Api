from opencc import OpenCC


# Initial
cc = OpenCC('s2tw')
train_data = open('wiki_texts.txt', 'r', encoding='utf-8').read()
train_data = cc.convert(train_data)

open('wiki_zh_tw.txt', 'w', encoding='utf-8').write(train_data)