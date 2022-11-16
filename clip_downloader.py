import json
import youtube_dl

if __name__ == "__main__":
    file_path = input("파일 이름 입력: ")
    file_extend = file_path.split('.')[-1]
    if file_extend == 'json':
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        clip_link = list(map(lambda x:x['url'], data))
    elif file_extend == 'txt':
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = file.read()
        clip_link = data.split("\n")
    ydl_opts = {
        'format': 'bestvideo/best'
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(clip_link)
