import json
import youtube_dl
from functools import reduce

forbidden_chars = "%:/\\<>*?？|！\n"
max_try = 5

if __name__ == "__main__":
    file_path = input("파일 이름 입력: ")
    file_extend = file_path.split('.')[-1]
    if file_extend == 'json':
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        clip_link = list(map(lambda x:[x['url'],x['title'],x['created_at'],x['gamename']], data))
        for item in clip_link:
            time = item[2].split("T")[0]
            title = reduce(lambda x,y: x.replace(y, "_"), list(forbidden_chars), item[1])
            game = reduce(lambda x,y: x.replace(y, "_"), list(forbidden_chars), item[3])
            err = 0
            while err < max_try:
                try:
                    ydl_opts = {
                        'outtmpl': f'({time} {game}) {title}.mp4',
                        'format': 'bestvideo/best'
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([item[0]])
                except:
                    err += 1
                else:
                    break  
    elif file_extend == 'txt':
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = file.read()
        clip_link = data.split("\n")
        ydl_opts = {
            'format': 'bestvideo/best'
            }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(clip_link)
