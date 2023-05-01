import csv    
import os

class Data_factor:
    def __init__(self,id,title,week,time,evaluation,site,memo,url):
        self.id = id
        self.title = title
        self.week = week                if week else "null"
        self.time = time                if time else "null"
        self.evaluation = evaluation    if evaluation else "null"
        self.site = site                if site else "null"
        self.week = week                if week else "null"
        self.memo = memo                if memo else "null"
        self.url = url                if url else "null"

def check_csv_file():
    file_path = 'anime_list.csv'
    if not os.path.isfile(file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # ヘッダー行を書き込み
            writer.writerow(['id', 'title', 'week', 'time', 'evaluation', 'site', 'memo', 'url'])
            print("make file")
    return file_path

def load_data_from_csv(file_path):
    anime_list = []
    with open(file_path, 'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) # skip header row
        for row in reader:
            id = row[0]
            title = row[1]
            week = row[2]
            time = row[3]
            evaluation = row[4]
            site = row[5]
            memo = row[6]
            url = row[7]
            data = Data_factor(id,title,week,time,evaluation,site,memo,url)
            anime_list.append(data)
    return anime_list

def add_data(file_path,title,week,time,evaluation,site,memo,url):
    #新しいidを取得
    with open(file_path, 'r',encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        if len(reader) == 0:
            id = 1
        else:
            max_id = max([int(row['id']) for row in reader])
            id = max_id + 1

    with open(file_path, 'a', newline='\n',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # ヘッダー行を書き込む
        if csvfile.tell() == 0:
            writer.writerow(['id','title','week','time','evaluation','site','memo','url'])
            csvfile.write('\n')
        # タスクの情報を新しい行に書き込む
        writer.writerow([str(id),title,week,time,evaluation,site,memo,url])

def Update_data(file_path,id,title,week,time,evaluation,site,memo,url):
    # csvファイルを読み込む
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    for i, row in enumerate(data):
        if row[0] == id:
            # 上書きする行のインデックスと上書きするデータ
            overwrite_data = [id,title,week,time,evaluation,site,memo,url]

            # csvファイルを読み込む
            with open(file_path, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                data = list(reader)

            # 指定された行を上書きする 
            # data[int(id)] = overwrite_data
            data[int(id)] = overwrite_data
            # csvファイルに上書き保存する
            with open(file_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            break

def delete_data(id, file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        f.seek(0)
        reader = csv.reader(f)
        rows = list(reader)

    for i, row in enumerate(rows):
        if row[0] == id:
            rows.pop(i)
            break

    with open(file_path, 'w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
 
print("import csvManager!")

