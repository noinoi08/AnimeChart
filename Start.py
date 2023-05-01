import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import webbrowser

import csv_Manager as csvM

class MakeApp:
    def __init__(self,master):
        self.master = master     
        self.file_path = csvM.check_csv_file()
        self.anime_list = csvM.load_data_from_csv(self.file_path)
        self.Day_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.Monday=[]
        self.Tuesday=[]
        self.Wednesday=[]
        self.Thursday=[]
        self.Friday=[]
        self.Saturday=[]
        self.Sunday=[]
        self.weekday_data = {
            'Monday': self.Monday,
            'Tuesday': self.Tuesday,
            'Wednesday': self.Wednesday,
            'Thursday': self.Thursday,
            'Friday': self.Friday,
            'Saturday': self.Saturday,
            'Sunday': self.Sunday
        }

        self.row_count = 2

        for anime in self.anime_list:
            if(anime.week=='Monday'):
                self.Monday.append(anime)
            if(anime.week=='Tuesday'):
                self.Tuesday.append(anime)
            if(anime.week=='Wednesday'):
                self.Wednesday.append(anime)
            if(anime.week=='Thursday'):
                self.Thursday.append(anime)
            if(anime.week=='Friday'):
                self.Friday.append(anime)
            if(anime.week=='Saturday'):
                self.Saturday.append(anime)
            if(anime.week=='Sunday'):
                self.Sunday.append(anime)

        self.make_app(master)

    # 各種ウィジェット作成関数.
    def make_app(self,master):
        count = self.row_count

        # 各種ウィジェットの作成.
        self.L_title = ttk.Label(master, text="アニメ早見表",font=("",12))
        self.B_test = ttk.Button(master, text="test", command=self.test)
        self.L_tag_time = ttk.Label(master, text="time")
        self.L_tag_site = ttk.Label(master, text="site")

        # # 各種ウィジェットの設置.
        self.L_title.grid(row= 0,column=0,columnspan=4)
        self.B_test.grid(row = 1,column=3, sticky=tk.E)
        self.L_tag_time.grid(row= 1,column=1,sticky=tk.EW)
        self.L_tag_site.grid(row= 1,column=2,sticky=tk.EW)
        
        #曜日ごとのウィジェットの設置.    
        for day in self.Day_list:
            data_list = self.weekday_data[day]
            self.B_day= tk.Button(master,text=day,command=lambda data_list = data_list, day = day:self.change_edit_window(master,data_list, day))
            self.B_day.grid(row=count,column=0,sticky=tk.W)
            count += 1
            if not (data_list):
                self.view_anime_title(master,'',count)
                count += 1

            for data in data_list:
                self.view_anime_title(master,data,count)
                count += 1
    
    def view_anime_title(self,master,data,count):
        if data:
            title = data.title
            time = data.time
            site = data.site
        else:
            title = "なし"
            time = "null"
            site = "null"
        self.B_watch = tk.Button(master,text="視聴",command=lambda data = data:self.referece_URL(data))
        self.L_AnimeTitle = ttk.Label(master,background="white",text=title,font=("",11))
        self.L_time = ttk.Label(master,background="white",text=time,font=("",11))
        self.L_site = ttk.Label(master,background="white",text=site,font=("",11))

        self.L_AnimeTitle.grid(row=count,column=0,stick=tk.EW)
        self.L_time.grid(row=count,column=1,stick=tk.EW)
        self.L_site.grid(row=count,column=2,stick=tk.EW)
        if not (title == "なし"):
            self.B_watch.grid(row=count,column=3,sticky=tk.NSEW)
    
    def referece_URL(self,data):
        url = data.url
        if not url:
            return
        if url.startswith("https://"):
            webbrowser.open_new(url)
        else:
            print("Record URL")
            return

    def make_edit_window(self,master, data_list, day):
        #id,title,week,time,evaluation,site,memo,url
        row_count = self.row_count
        self.L_edit_window_title = ttk.Label(master, text="編集中",font=("",12))
        self.B_back_start_window = ttk.Button(master, text="戻る", command=lambda:self.change_start_window(master))
        
        self.L_edit_window_title.grid(row=0, column=0, columnspan=4, sticky="e")
        self.B_back_start_window.grid(row=1,column=8, sticky=tk.EW)

        #アニメ情報追加入力用.
        self.L_title = tk.Label(master, text="title")
        self.L_week = tk.Label(master, text="week")
        self.L_time = tk.Label(master, text="time")
        self.L_evaluation = tk.Label(master, text="value")
        self.L_site = tk.Label(master, text="site")
        self.L_memo = tk.Label(master, text="memo")
        self.L_url = tk.Label(master,text = "url")
        # グリッド配置
        self.L_title.grid(row=2, column=0,sticky=tk.EW)
        self.L_week.grid(row=2, column=1,sticky=tk.EW)
        self.L_time.grid(row=2, column=2,sticky=tk.EW)
        self.L_evaluation.grid(row=2, column=3,sticky=tk.EW)
        self.L_site.grid(row=2, column=4,sticky=tk.EW)
        self.L_memo.grid(row=2, column=5,sticky=tk.EW)
        self.L_url.grid(row=2, column=6,sticky=tk.EW)
        row_count += 1
        #エントリーボックス設置
        self.E_title_to_add = tk.Entry(master)
        self.E_title_to_add.grid(row=row_count, column=0,sticky=tk.EW)
        self.CB_week_to_add = ttk.Combobox(master,textvariable=tk.StringVar(),width=12,values=self.Day_list,state="readonly")
        self.CB_week_to_add.grid(row=row_count, column=1,sticky=tk.EW)
        self.E_time_to_add = tk.Entry(master,width=10)
        self.E_time_to_add.grid(row=row_count, column=2,sticky=tk.EW)
        self.E_evaluation_to_add = tk.Entry(master,width=5)
        self.E_evaluation_to_add.grid(row=row_count, column=3,sticky=tk.EW)
        self.E_site_to_add = tk.Entry(master)
        self.E_site_to_add.grid(row=row_count, column=4,sticky=tk.EW)
        self.E_memo_to_add = tk.Entry(master)
        self.E_memo_to_add.grid(row=row_count, column=5,sticky=tk.EW)
        self.E_url_to_add = tk.Entry(master)
        self.E_url_to_add.grid(row=row_count, column=6,sticky=tk.EW)
        self.B_data_add = tk.Button(master,text="Add",command=lambda:self.add_new_anime_data(master,day))
        self.B_data_add.grid(row=row_count,column=7,sticky=tk.EW)

        row_count += 1

        self.edit_make_entry(master,row_count,data_list,day)

    def edit_make_entry(self,master,row_count,data_list,day):
        entry_list = dict()
        #エントリーボックス設置
        for i,data in enumerate(data_list):
            self.E_title = tk.Entry(master)
            self.E_title.grid(row=row_count, column=0,sticky=tk.EW,pady=10)
            self.E_title.insert(0,data.title)
            
            # self.E_week = tk.Entry(master,width=12)
            self.CB_week = ttk.Combobox(master,textvariable=tk.StringVar(),width=12,values=self.Day_list,state="readonly")
            self.CB_week.grid(row=row_count, column=1,sticky=tk.EW)
            index = self.Day_list.index(day)
            self.CB_week.set(self.Day_list[index])
            # self.E_week.grid(row=row_count, column=1,sticky=tk.EW)
            # self.E_week.insert(0,data.week)
            
            self.E_time = tk.Entry(master,width=10)
            self.E_time.grid(row=row_count, column=2,sticky=tk.EW)
            self.E_time.insert(0,data.time)
            
            self.E_evaluation = tk.Entry(master,width=5)
            self.E_evaluation.grid(row=row_count, column=3,sticky=tk.EW)
            self.E_evaluation.insert(0,data.evaluation)
            
            self.E_site = tk.Entry(master)
            self.E_site.grid(row=row_count, column=4,sticky=tk.EW)
            self.E_site.insert(0,data.site)
            
            self.E_memo = tk.Entry(master)
            self.E_memo.grid(row=row_count, column=5,sticky=tk.EW)
            self.E_memo.insert(0,data.memo)

            self.E_url = tk.Entry(master)
            self.E_url.grid(row=row_count, column=6,sticky=tk.EW)
            self.E_url.insert(0,data.url)

            title = self.E_title
            week = self.CB_week
            time = self.E_time
            value = self.E_evaluation
            site = self.E_site
            memo = self.E_memo
            url = self.E_url
            
            # 取得した情報をdataオブジェクトにセットする
            entry_list[i] = [title,week,time,value,site,memo,url]

            self.B_update_button = tk.Button(master,text="Update",command=lambda data = data_list[i],entry_list= entry_list[i]:self.Update_button(data,entry_list))
            self.B_update_button.grid(row=row_count,column=7,sticky=tk.EW)
            self.B_delete_button = tk.Button(master,text="Delete",command=lambda data = data_list[i],day=day:self.Delete_button(master,data,day))
            self.B_delete_button.grid(row=row_count,column=8,sticky=tk.EW)
            row_count += 1

    def add_new_anime_data(self,master,day):
        title = self.E_title_to_add.get()
        if not title:
            print("Please write title")
            return
        week = self.CB_week_to_add.get()
        time = self.E_time_to_add.get()
        evaluation = self.E_evaluation_to_add.get()
        site = self.E_site_to_add.get()
        memo = self.E_memo_to_add.get()
        url = self.E_url_to_add.get()
        csvM.add_data(self.file_path,title,week,time,evaluation,site,memo,url)
        self.reload_edit_window(master,day)

    def Update_button(self, data, entry_data):
        id = data.id
        title = entry_data[0].get()
        if not title:
            print("Please write title")
            return
        week = entry_data[1].get()
        time = entry_data[2].get()
        value = entry_data[3].get()
        site = entry_data[4].get()
        memo = entry_data[5].get()
        url = entry_data[6].get()
    
        csvM.Update_data(self.file_path,id,title,week,time,value,site,memo,url)
        print("Update!")

    def Delete_button(self,master,data,day):
        answer = messagebox.askyesno('Alert!', '本当に消しますか？')
        if answer:
            print('Delete!')
            id = data.id
            csvM.delete_data(id, self.file_path)
            self.reload_edit_window(master,day)
        else:
            print('cancel')

    ### 画面切り替え関数################
    def destroy_children(self,parent):
        for child in parent.winfo_children():
            child.destroy()

    def change_start_window(self,master):
        self.destroy_children(master)
        root.geometry("600x750")
        self.reload_csv()
        self.make_app(master)

    def change_edit_window(self, master,data_list,day):
        self.destroy_children(master)
        root.geometry("900x600")
        self.make_edit_window(master, data_list,day)

    def reload_edit_window(self,master,day):
        self.destroy_children(master)
        self.reload_csv()
        data_list = self.weekday_data[day]
        self.make_edit_window(master,data_list,day)

    # csv再ロード.
    def reload_csv(self):
        self.anime_list = csvM.load_data_from_csv(self.file_path)
        self.Monday.clear()
        self.Tuesday.clear()
        self.Wednesday.clear()
        self.Thursday.clear()
        self.Friday.clear()
        self.Saturday.clear()
        self.Sunday.clear()

        for anime in self.anime_list:
            if(anime.week=='Monday'):
                self.Monday.append(anime)
            if(anime.week=='Tuesday'):
                self.Tuesday.append(anime)
            if(anime.week=='Wednesday'):
                self.Wednesday.append(anime)
            if(anime.week=='Thursday'):
                self.Thursday.append(anime)
            if(anime.week=='Friday'):
                self.Friday.append(anime)
            if(anime.week=='Saturday'):
                self.Saturday.append(anime)
            if(anime.week=='Sunday'):
                self.Sunday.append(anime)

    ###################################

    def test(self):
        print("test")
        pass

# ルートウィンドウを作成.
root = tk.Tk()
root.title("アニメ早見表")
root.geometry("600x750")

frame = ttk.Frame(root)
frame.pack(fill='both', expand=True, pady=10)
frame.grid_columnconfigure(0,weight=1)

make = MakeApp(frame)

root.mainloop()