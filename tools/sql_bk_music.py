import os, json

base_dir=os.path.dirname(os.path.abspath(__file__))
json_path=os.path.join(base_dir,'background_music.json')
sql_path=os.path.join(base_dir,'background_music.sql')

with open(json_path,'r',encoding='utf-8') as f: data=json.load(f)

def esc(v): return v.replace("'","''") if isinstance(v,str) else ''

rows=[]
for i in data:
    author=esc(i.get('author',''))
    name=esc(i.get('name',''))
    mp3=esc(i.get('mp3',''))
    buy=1 if str(i.get('buy','0'))=='1' else 0
    rows.append(f"('{author}','{name}','{mp3}',{buy})")

sql="INSERT INTO background_music (author,name,mp3,buy) VALUES\n"+",\n".join(rows)+";"

with open(sql_path,'w',encoding='utf-8') as f: f.write(sql)

print('OK ->',sql_path)
