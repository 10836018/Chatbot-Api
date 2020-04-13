# Gensim 訓練中文詞向量練習

## OpenCC 繁簡轉換

- [OpenCC Python 使用方法](https://pypi.org/project/opencc-python-reimplemented/)
- [OpenCC Github](https://github.com/BYVoid/OpenCC)
```
pip install opencc-python-reimplemented
```

## 訓練步驟

1. 取得[維基百科數據](https://zh.wikipedia.org/wiki/Wikipedia:%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8B%E8%BD%BD) *( 選 `pages-articles.xml.bz2` 結尾的檔案 )*

2. 把下載的維基百科數據置於與專案同個目錄
```
python wiki_to_txt.py zhwiki-20200401-pages-articles.xml.bz2
```

3. 使用 OpenCC 把維基文章統一轉換為繁體中文 ( 轉換程式寫在`convert.py` )
- 使用 `convert.py`
```
python convert.py
```

- 直接使用 command line 轉換
```
python -m opencc -c s2tw -i wiki_texts.txt -o wiki_zh_tw.txt
```

4. jieba 斷詞
```
python segment.py
```

5. 使用 gensim 的 word2vec 模型進行訓練
```
python train.py
```

6. 測試模型
```
python demo.py
```

## 原始程式資料
#### [zake7749/word2vec-tutorial](https://github.com/zake7749/word2vec-tutorial)
#### [以 gensim 訓練中文詞向量](http://zake7749.github.io/2016/08/28/word2vec-with-gensim/)

