
"""
2048遊戲
本模塊已完整實現2048遊戲的算法及分數的計算算法
本遊戲的界面採用python 標準庫 tkinter 來實現
此界面的佈局採用tkinter中的grid佈局
"""


import random  # 導入隨機模塊random,主要用於隨機生成新的數字及數字擺方位置
import math  # 導入數學模塊,用來計算分數
_map_data = [
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
		]

# _map_data 綁定一個 4 x 4 列表,此列表為2048遊戲地圖，初始值如下:
class GameCoreController:
	#獲取沒有數字的方格的數量,如果數量為0則說有無法填充新數據，遊戲即將結束
	def get_space_count(self):
		self.count = 0
		count = self.count
		for r in _map_data:
			count += r.count(0)
		return count
	 #獲取遊戲的分數,得分規則是每次有兩個數加在一起則生成相應的分數。
     #如 2 和 2 合併後得4分, 8 和 8 分併後得 16分.
     #根據一個大於2的數字就可以知道他共合併了多少次，可以直接算出分數:
     #如:
     #   4 一定由兩個2合併，得4分
     #  8 一定由兩個4合併,則計:8 + 4 + 4 得16分
     #  ... 以此類推'''
	def get_score(self):
		self.score = 0
		score = self.score
		for r in _map_data:
			for c in r:
				score += 0 if c < 4 else c * int((math.log(c, 2) - 1.0))
		return score
	

	'''填充2到空位置，如果填度成功返回True,如果已滿，則返回False'''
	def fill2(self):
		blank_count = self.get_space_count()# 得到地圖上空白位置的個數
		if 0 == blank_count:
			return False
    # 生成隨機位置, 如，當只有四個空時，則生成0~3的數，代表自左至右，自上而下的空位置
		pos = random.randrange(0, blank_count)
		offset = 0
		for row in _map_data:  # row為行row
			for col in range(4):  # col 為列，column
				if 0 == row[col]:
					if offset == pos:
                    # 把2填充到第row行，第col列的位置，返回True
						row[col] = 2
						return True
					offset += 1
	def reset(self):#'''重新設置遊戲數據,將地圖恢復為初始狀態，並加入兩個數據 2 作用初始狀態'''
		_map_data[:] = [] 
		for j in range(4):
			_map_data.append([0, 0, 0, 0])
    # 在空白地圖上填充兩個2
		self.fill2()
		self.fill2()
	def is_gameover(self):
		#判斷遊戲是否結束,如果結束返回True,否是返回False

		for r in _map_data:
        # 如果水平方向還有0,則遊戲沒有結束
			if r.count(0):
				return False
        # 水平方向如果有兩個相鄰的元素相同，應當是可以合併的，則遊戲沒有結束
			for i in range(3):
				if r[i] == r[i + 1]:
					return False
		for c in range(4):
        # 豎直方向如果有兩個相鄰的元素相同，應當可以合併的，則遊戲沒有結束
			for r in range(3):
				if _map_data[r][c] == _map_data[r + 1][c]:
					return False
		return True	
	def is_win(self):
		#判斷遊戲是否結束,如果結束返回True,否是返回False
		for r in _map_data:
	        # 如果還沒有2048,則遊戲沒有結束
			if r.count(2048):
				return True
		return False
if __name__ =="__main__":
	v = GameCoreController()
	v.reset()
	print(_map_data)


