from tkinter import Tk, filedialog
import os

root = Tk()
root.withdraw()

# 选择多个视频文件并升序排列
video_file = filedialog.askopenfilenames(filetypes=[('视频文件', '.mp4')])
video_list = list(video_file)
video_list.sort()

if os.path.isfile('video_list.txt'):  # 判断文件是否存在
    os.system('del /f /q video_list.txt')

if video_list:
    print('选择的视频文件：')
    for video in video_list:
        print(video)
        file = open('video_list.txt', 'a')  # 打开文件执行写入操作
        file.write("file '" + video + "'\n")
        file.close()

    print('输出的视频文件：')
    output = str(video_list[0]).split('/')[-1][0:18] + '.MP4'
    print(output)
    os.system(f'ffmpeg -f concat -safe 0 -i video_list.txt -c copy {output}')
    if os.path.isfile('video_list.txt'):  # 判断文件是否存在
        os.system('del /f /q video_list.txt')
else:
    print('没有选择任何文件')
