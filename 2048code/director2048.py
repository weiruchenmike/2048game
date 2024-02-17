import random  
import math  
from model2048 import Game_model as GM 
from set2048 import GameCoreController as GCC
import set2048
class Game_director:
	def __init__(self):
		self.__controller = GCC()
		self.__model = GM()
################################################################################################################### 
	"""遊戲左鍵按下時或向左滑動屏幕時的算法"""
	def left(self):
		moveflag = False # moveflag 是否成功移動數字標誌位,如果有移動則為真值,原地圖不變則為假值(以利於後面GUI介面設計)
		# 將第一行都向左移動.如果有移動就返回True
		for line in set2048._map_data:
			if self.__model._left_move_aline(line):
				moveflag = True
		return moveflag
####################################################################################################################
	"""遊戲右鍵按下時或向右滑動屏幕時的算法
    選將屏幕進行左右對調，對調後，原來的向右滑動即為現在的向左滑動
    滑動完畢後，再次左右對調回來
    """
	def right(self):
		# 左右對調
		for r in set2048._map_data:
			r.reverse()
			moveflag = self.left() # 向左滑動
    # 再次左右對調
		for r in set2048._map_data:
			r.reverse()
		return moveflag
####################################################################################################################
	"""遊戲上鍵按下時或向上滑動屏幕時的算法
    先把每一列都自上而下放入一個列表中line中，然後執行向滑動，
    滑動完成後再將新位置擺回到原來的一列中
    """
	def up(self):
		moveflag = False
		line = [0, 0, 0, 0] # 先初始化一行，準備放入數據
		for col in range(4): # 先取出每一列
        # 把一列中的每一行數入放入到line中
			for row in range(4):
				line[row] = set2048._map_data[row][col]
        # 將當前列進行上移，即line 左移
			if self.__model._left_move_aline(line):
				moveflag = True
        # 把左移後的 line中的數據填充回原來的一列
			for row in range(4):
				set2048._map_data[row][col] = line[row]
		return moveflag
#####################################################################################################################
	"""遊戲下鍵按下時或向下滑動屏幕時的算法
    選將屏幕進行上下對調，對調後，原來的向下滑動即為現在的向上滑動
    滑動完畢後，再次上下對調回來
    """
	def down(self):
		set2048._map_data.reverse()
		moveflag = self.up() # 上滑
		set2048._map_data.reverse()
		return moveflag
if __name__=="__main__":
	v=Game_director()
	print(v.left())
	print(v.right())
	print(v.up())
	print(v.down())