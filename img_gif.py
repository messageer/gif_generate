import imageio
import os

# dir = 'D:/我的文档/Desktop/点/asift'
dir = 'D:/我的文档/Desktop/xhl1'

def create_gif(image_list, gif_name, duration=0.05):
    frames = []
    # print(len(image_list))
    for image_name in image_list:
        frames.append(imageio.imread(dir+'/'+image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main():
    duration = 1.0/3 #  每帧停留时长.。。
    image_list = os.listdir(dir+'/')
    image_list.sort(key=lambda x: int(x[:-4]))
    # print(image_list)
    gif_name = dir+'.gif'
    # print(gif_name)
    create_gif(image_list, gif_name, duration)

if __name__ == '__main__':
    main()