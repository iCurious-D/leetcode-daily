""" 3568. 清理教室的最少移动     中等
给你一个 m x n 的网格图 classroom，其中一个学生志愿者负责清理散布在教室里的垃圾。网格图中的每个单元格是以下字符之一：
'S' ：学生的起始位置
'L' ：必须收集的垃圾（收集后，该单元格变为空白）
'R' ：重置区域，可以将学生的能量恢复到最大值，无论学生当前的能量是多少（可以多次使用）
'X' ：学生无法通过的障碍物
'.' ：空白空间
同时给你一个整数 energy，表示学生的最大能量容量。学生从起始位置 'S' 开始，带着 energy 的能量出发。
每次移动到相邻的单元格（上、下、左或右）会消耗 1 单位能量。
如果能量为 0，学生此时只有处在 'R' 格子时可以继续移动，此区域会将能量恢复到 最大 能量值 energy。
返回收集所有垃圾所需的 最少 移动次数，如果无法完成，返回 -1。

示例 1：输入: classroom = ["S.", "XL"], energy = 2;          输出: 2
解释:学生从单元格 (0, 0) 开始，带着 2 单位的能量。由于单元格 (1, 0) 有一个障碍物 'X'，学生无法直接向下移动。
收集所有垃圾的有效移动序列如下：移动 1：从 (0, 0) → (0, 1)，消耗 1 单位能量，剩余 1 单位。
移动 2：从 (0, 1) → (1, 1)，收集垃圾 'L'。学生通过 2 次移动收集了所有垃圾。因此，输出为 2。
示例 2：输入: classroom = ["LS", "RL"], energy = 4;          输出: 3
解释:学生从单元格 (0, 1) 开始，带着 4 单位的能量。收集所有垃圾的有效移动序列如下：
移动 1：从 (0, 1) → (0, 0)，收集第一个垃圾 'L'，消耗 1 单位能量，剩余 3 单位。
移动 2：从 (0, 0) → (1, 0)，到达 'R' 重置区域，恢复能量为 4。
移动 3：从 (1, 0) → (1, 1)，收集第二个垃圾 'L'。学生通过 3 次移动收集了所有垃圾。因此，输出是 3。
示例 3：输入: classroom = ["L.S", "RXL"], energy = 3;        输出: -1
解释:没有有效路径可以收集所有 'L'。

提示：
1 <= m == classroom.length <= 20
1 <= n == classroom[i].length <= 20
classroom[i][j] 是 'S'、'L'、'R'、'X' 或 '.' 之一
1 <= energy <= 50
网格图中恰好有 一个 'S'。
网格图中 最多 有 10 个 'L' 单元格。

"""
from collections import deque


def minMoves(classroom: list[str], energy: int) -> int:
    m, n = len(classroom), len(classroom[0])  # 网格行数 m、列数 n

    sr = sc = -1  # 学生起点 S 的行列坐标
    garbage = []  # 按发现顺序记录所有垃圾 L 的坐标

    # ---- 第一步：扫描网格，定位起点和所有垃圾 ----
    for i in range(m):
        for j in range(n):
            if classroom[i][j] == 'S':  # 找到学生起始位置
                sr, sc = i, j
            elif classroom[i][j] == 'L':  # 找到垃圾，记录坐标
                garbage.append((i, j))

    L = len(garbage)  # 垃圾总数
    if L == 0:  # 没有垃圾，不用动
        return 0

    # ---- 第二步：建立垃圾坐标 → 位索引的映射 ----
    # 例如第 0 个垃圾对应 mask 的第 0 位，第 1 个对应第 1 位……
    gar_pos = {}  # {(r, c): bit_index}
    for idx, (r, c) in enumerate(garbage):
        gar_pos[(r, c)] = idx

    gar_mask = (1 << L) - 1  # 所有位都为 1 的目标 mask，表示全部收集

    # ---- 第三步：BFS ----
    # 队列元素：(当前行, 当前列, 已收集掩码, 剩余能量, 已走步数)
    queue = deque()
    queue.append((sr, sc, 0, energy, 0))  # 从起点出发，mask=0（没收集），能量满，步数 0

    # 核心剪枝字典：key = (row, col, mask)，value = 到达该状态时的最大能量
    # 同一个 (位置, 收集状态)，能量越高越优；低能量的状态可以直接丢弃
    best = {(sr, sc, 0): energy}

    while queue:  # 队列不空就一直扩展
        r, c, mask, eng, steps = queue.popleft()  # 取出队首状态

        # 如果这个状态已经被更优的能量访问过，跳过（延迟剪枝）
        if best.get((r, c, mask), -1) > eng:
            continue

        # ---- 第四步：向四个方向扩展 ----
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 上、下、左、右
            nr, nc = r + dr, c + dc  # 相邻格子的坐标

            # 越界或障碍物，跳过
            if nr < 0 or nr >= m or nc < 0 or nc >= n or classroom[nr][nc] == 'X':
                continue

            neng = eng - 1  # 走一步消耗 1 能量
            if neng < 0:  # 能量不够
                continue
            # 踩到 R 格，能量回满
            if classroom[nr][nc] == 'R':
                neng = energy

            # 如果新格子是垃圾，更新收集掩码
            nmask = mask
            if (nr, nc) in gar_pos:
                nmask |= (1 << gar_pos[(nr, nc)])

            # 所有垃圾都收集了，BFS 保证第一次到达就是最少步数
            if nmask == gar_mask:
                return steps + 1

            # 能量为 0 时
            if neng == 0:
                continue

                # 剪枝：只有能量严格更优时才入队
            key = (nr, nc, nmask)
            if neng > best.get(key, -1):
                best[key] = neng
                queue.append((nr, nc, nmask, neng, steps + 1))

    return -1  # 队列耗尽，无法收集全部垃圾


if __name__ == '__main__':
    print(minMoves(["S.", "XL"], 2))
    print(minMoves(["LS", "RL"], 4))
    print(minMoves(["L.S", "RXL"], 3))












