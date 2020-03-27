from flask import Flask, request, jsonify

import json
import jieba

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def postJson():
    if request.method == 'POST':
        data = json.loads(request.get_data().decode('utf-8'))
        print("get POST request data: ", data)

        answer = data["answer"]

        cleanText = "".join(c for c in answer if c not in (
        '；', '，', '。', '！', '：', '「', '」', '…', '、', '？', '【', '】', '.', ':', '?', ';', '!', '~', '`', '+', '-', '<',
        '>', '/', '[', ']', '{', '}', "'", '"'))

        words = jieba.cut(cleanText, cut_all=False)

        myHash = {};
        for word in words:
            if word in myHash:
                myHash[word] += 1
            else:
                myHash[word] = 1

        items = [(v, k) for k, v in myHash.items()]
        items.sort()
        items.reverse()
        items = [(k, v) for v, k in items]

        for (wrd, cnt) in items:
            ans = {
                'answer': wrd,
                'cnt': cnt
            }

        return jsonify(ans)

    elif request.method == 'GET':
        return 'ok!'


if __name__ == '__main__':
    app.run()
