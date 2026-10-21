""" 3863. 将一个字符串排序的最小操作次数   中等
给你一个由小写英文字母组成的字符串 s。
在一次操作中，你可以选择 s 的任意 子字符串（但 不能 是整个字符串），并将其按 非降序字母顺序 进行 排序。
返回使 s 按 非降序 排列所需的 最小 操作次数。如果无法做到，则返回 -1。

示例 1：输入： s = "dog";     输出： 1
解释：将子字符串 "og" 排序为 "go"。现在，s = "dgo"，已按升序排列。因此，答案是 1。
示例 2：输入： s = "card";    输出： 2
解释：将子字符串 "car" 排序为 "acr"，得到 s = "acrd"。
将子字符串 "rd" 排序为 "dr"，得到 s = "acdr"，已按升序排列。因此，答案是 2。
示例 3：输入： s = "gf";      输出： -1
解释：在给定提示下，无法对 s 进行排序。因此，答案是 -1。

提示：
1 <= s.length <= 10^5
s 仅由小写英文字母组成。

"""
def minOperations(s: str) -> int:
    n = len(s)
    if all(s[i] <= s[i + 1] for i in range(n - 1)):
        return 0
    if n == 2:
        return -1

    mn, mx = min(s), max(s)
    if s[0] == mn or s[-1] == mx:
        return 1

    tmp_s = s[1:-1]
    if mn in tmp_s or mx in tmp_s:
        return 2

    return 3

    # n = len(s)
    # if all(a <= b for a, b in zip(s, s[1:])):
    #     return 0
    # if n == 2:
    #     return -1
    # i, j = s.index(min(s)), s.rindex(max(s))
    # # mn 已在首位 或 mx 已在末位 → 一步
    # # mn 能被"排到首位"（i <= n-2）或 mx 能被"排到末位"（j >= 1）→ 两步
    # # 否则 mn 死锁在末位、mx 死锁在首位 → 三步
    # return 1 if (i == 0 or j == n - 1) else 2 if (i < n - 1 or j > 0) else 3


if __name__ == '__main__':
    print(minOperations("dog"))
    print(minOperations("card"))
    print(minOperations("gf"))



