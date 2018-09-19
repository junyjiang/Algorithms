class Solution:
    """
    解题思路：
    1.将A+B转化为位运算：即A+B可以表示为A⊕B+(A&B)<<1
    2.需要处理溢出问题
    3.参考https://shawnhardy.me/index.php/2018/02/26/lintcode-001-a-b-wen-ti/
    """
    def aplusb(self, a, b):
        while b != 0:
            a, b = (a ^ b) & 0xFFFFFFFF,((a & b) <<1)
        return a

if __name__ == '__main__':
    a = int(input())
    b = int (input())
    print(Solution().aplusb(a,b))