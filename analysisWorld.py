import pkuseg

from collections import Counter
from pprint import  pprint

content = []
with open("张小龙演讲.txt", encoding="utf-8") as f:
    content = f.read()

seg = pkuseg.pkuseg()
text = seg.cut(content)
counter = Counter(text)
pprint(counter.most_common(20))

stopwords = []

with open("stopword.txt", encoding="utf-8") as f:
    stopwords = f.read()

new_text = []

for w in text:
    if w not in stopwords:
        new_text.append(w)

counter = Counter(new_text)
pprint(counter.most_common(20))
