class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        cnt = min(children, money // 7)
        money -= cnt * 7
        children -= cnt
        if children == 0 and money != 0 or money == 3 and children == 1:
            cnt -= 1
        return cnt
