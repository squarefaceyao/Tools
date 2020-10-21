import youtube_dl

def main():
    # 设定
    destPath = '/Users/squareface/pornhub/'    # 音频文件存放的目标字串
    videoPage = 'https://cn.pornhub.com/view_video.php?viewkey=ph5ef51375206be'




    ydl_opts = {                              # 设定下载选项
                'outtmpl': destPath+'%(title)s.%(ext)s',
                'format': 'best',
                }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([videoPage])                 # 下载视频


if __name__ == '__main__':

    main()
