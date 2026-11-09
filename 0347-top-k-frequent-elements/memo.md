step1
heapqの操作でリストの中にタプルが入っている場合初めの要素で比較されることを知らなった。
とりあえず実装したが名前など改善できるところがあるのでstep2で改善する。
mを異なる要素の数とする
時間計算量O(n + mlog(k))
空間計算量O(max(m, k))

step2
変数名やpushを外に出して簡略化した
https://github.com/skypenguins/coding-practice/pull/53/changes
を参考にしてバケットソートの解法を書いた

step3
バケットソートを練習