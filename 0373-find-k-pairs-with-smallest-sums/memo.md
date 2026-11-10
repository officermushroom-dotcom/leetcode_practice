## step1
O(n^2log(n^2))の解法はすぐ思いついてが入力が10^5なためTLEになると思われる。
->memory limit exceededになった。memoryのエラーは今までなったことがなかった。計算すると10^5 * 10^5 * 8 = 10^10 * 8 = 80 GB　そりゃあエラーなるかという感じ

## step2
https://github.com/KaoKao1233/LeetCodeArai60/pull/10/changes#diff-312f719eb83f0b23e5dea8cf80f5a573d1eef20f2221d406b905fcf39a1a951bR5-R11
のコードを参考にした。step1と考え方は似ていいるがnums1とnums2を表としてとらえることでheapに追加するペアを絞れるということらしい。はじめ感覚的にわかりずらかったが図に書いたりして理解した。
時間計算量O(nlog(n))
空間計算量O(min(n, k))

seenの解法
https://github.com/hayashi-ay/leetcode/pull/66/changes

indexで管理する解法
https://github.com/MA-yo-TA/leetcode/pull/11/changes

## step3
heapの練習にstep2を三回練習
