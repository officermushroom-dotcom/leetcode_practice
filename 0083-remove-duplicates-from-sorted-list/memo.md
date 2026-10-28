step1
node.next = node.next.nextという考え方が思いつかなった。sortされてるのでset()を作る必要がなく隣同士の値だけ確認すればよいことに気づいた。
時間計算量O(n)、空間計算量O(1)

step2
ダミーノードの解法