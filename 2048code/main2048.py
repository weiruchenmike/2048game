from tkinter import * #https://www.itread01.com/content/1547705544.html
from tkinter import messagebox
from model2048 import Game_model as GM 
from set2048 import GameCoreController as GCC
from director2048 import Game_director as GD
import set2048

class Game_ui:
    def __init__(self):
        self.__controller = GCC()
        self.__model = GM() 
        self.__director = GD()
    def main(self):
        self.__controller.reset() # 先重新設置遊戲數據
        self.root = Tk() # 創建tkinter窗口
        self.root.title('2048(choozmo)') # 設置標題文字
        self.root.resizable(width=False, height=False) # 固定寬和高
        # 設置遊戲中每個數據對應色塊的顏色
        mapcolor = {
        0: ("#cdc1b4", "#776e65"),
        2: ("#eee4da", "#776e65"),
        4: ("#ede0c8", "#f9f6f2"),
        8: ("#f2b179", "#f9f6f2"),
        16: ("#f59563", "#f9f6f2"),
        32: ("#f67c5f", "#f9f6f2"),
        64: ("#f65e3b", "#f9f6f2"),
        128: ("#edcf72", "#f9f6f2"),
        256: ("#edcc61", "#f9f6f2"),
        512: ("#e4c02a", "#f9f6f2"),
        1024: ("#e2ba13", "#f9f6f2"),
        2048: ("#ecc400", "#f9f6f2"),
        }
        # 以下是鍵盤映射
        keymap = {
            'a': self.__director.left,
            'd': self.__director.right,
            'w': self.__director.up,
            's': self.__director.down,
            'Left':self.__director.left,
            'Right': self.__director.right,
            'Up': self.__director.up,
            'Down': self.__director.down,
            'q': self.root.quit,
            }
        game_bg_color = "#bbada0" # 創建一個frame窗口，此創建將容納全部的widget 部件
        frame = Frame(self.root, bg=game_bg_color) #https://blog.csdn.net/m0_37264397/article/details/79101311
        frame.grid(sticky=N+E+W+S)
        # 設置顯示分數的Label
        label = Label(frame, text='分數', font=("黑體", 30, "bold"),
                bg="#bbada0", fg="#eee4da")
        label.grid(row=4, column=0, padx=5, pady=5)
        label_score = Label(frame, text='0', font=("黑體", 30, "bold"),
                bg="#bbada0", fg="#ffffff")
        label_score.grid(row=4, columnspan=2, column=1, padx=5, pady=5)
            
        

# 初始化圖形界面
        # 創建4x4的數字塊
        map_labels = [] # 遊戲各方塊的lable Widget
        for r in range(4):
            row = []
            for c in range(len(set2048._map_data[0])):
                value = set2048._map_data[r][c]
                text = str(value) if value else ''
                label = Label(frame, text=text, width=4, height=2,
                            font=("黑體", 30, "bold"))
                label.grid(row=r, column=c, padx=5, pady=5, sticky=N+E+W+S) #https://www.tutorialspoint.com/python/tk_grid.htm
                row.append(label)
            map_labels.append(row)        
        '''刷新界面函數
        根據計算出的frame地圖數據,更新各個Label的設置
        '''
        def update_ui(self):            
            for r in range(4):
                for c in range(len(set2048._map_data[0])):
                    number = set2048._map_data[r][c] # 設置數字
                    label = map_labels[r][c] # 選中Lable控件
                    label['text'] = str(number) if number else ''
                    label['bg'] = mapcolor[number][0]
                    label['foreground'] = mapcolor[number][1]
            label_score['text'] = str(self.__controller.get_score()) # 重設置分數        
        def reset_game():
            self.__controller.reset()
            update_ui(self)
        # 以下設置重新開始按鈕
        restart_button = Button(frame, text='重新開始', font=("黑體", 16, "bold"),
                                    bg="#8f7a66", fg="#f9f6f2", command=reset_game)
        restart_button.grid(row=4, column=3, padx=5, pady=5)
        def on_key_down(event):
            # '鍵盤按下處理函數'
            keysym = event.keysym
            if keysym in keymap:
                if keymap[keysym]():  # 如果有數字移動
                    self.__controller.fill2()  # 填充一個新的2
                    update_ui(self)
            if self.__controller.is_win():
                mb = messagebox.askyesno(
                title="you win", message="遊戲結束!\n是否退出遊戲!")
                if mb:
                    self.root.quit()
                else:
                    self.__controller.reset()
                    update_ui(self)
            if self.__controller.is_gameover():
                mb = messagebox.askyesno(
                title="gameover", message="遊戲結束!\n是否退出遊戲!")
                if mb:
                    self.root.quit()
                else:
                    self.__controller.reset()
                    update_ui(self)
    # 設置焦點能接收按鍵事件
        frame.bind("<Key>", on_key_down) #https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        frame.focus_set() #https://blog.51cto.com/1344839/1901654
        update_ui(self) # 更新界面
        self.root.mainloop() # 進入tkinter主事件循環
if __name__=="__main__":
    v=Game_ui()
    v.main() # 啟動遊戲