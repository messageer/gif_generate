import imageio
import os
import cv2
import numpy as np

dir = 'D:/我的文档/Desktop/video/1.MP4'

def create_gif(dir, gif_name, duration=0.05):
    frames = []
    cap = cv2.VideoCapture(dir)
    for i in range(30):  #25
        ret, videoFrame = cap.read()
        if(not ret):
            return
        videoFrame = np.array(videoFrame)
        videoFrame = videoFrame[:, :, [2, 1, 0]]
        frames.append(videoFrame)
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main():
    duration = 0.3   # 每帧停留时长
    gif_name = dir+'.gif'
    create_gif(dir, gif_name, duration)

if __name__ == '__main__':
    main()