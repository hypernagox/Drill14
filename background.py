import random
import server

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        # fill here
        self.cw = get_canvas_width() # 화면의 너비
        self.ch = get_canvas_height() # 화면의 너비
        self.w = self.image.w # 이미지의 너비와 높이
        self.h = self.image.h
        pass

    def draw(self):
        # fill here
        # 클리핑되고 시작 영역 (left,bottom) , 크기는 화면의 너비와 높이
        # 너비 픽셀이 홀수여야 중심으로 정확히 간다
        # to origin 함수는 피벗을 좌하단으로 보낸다.
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom, self.cw, self.ch,
            0, 0
        )
        pass

    def update(self):
        # fill here
        self.window_left =  int(server.boy.x) - self.cw // 2 # 소년의 좌표에서 캔버스 크기 //2 를뺀다
        self.window_bottom = int(server.boy.y) - self.ch // 2

        self.window_left = clamp(0,self.window_left ,self.w - self.cw - 1) # 윈도우 left 최소값 0 , 최대값은 전체이미지 너비에서 캔버스 너비만큼 뺀것이 최대값
        self.window_bottom = clamp(0, self.window_bottom, self.h - self.ch - 1)  #윈도우 바텀 최대값 이미지 높이 - 캔버스 높이
        pass

    def handle_event(self, event):
        pass






class TileBackground:

    def __init__(self):
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = 800 * 3
        self.h = 600 * 3

        # fill here



    def update(self):
        pass

    def draw(self):
        self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, self.h - self.ch - 1)

        # fill here
        pass


cx = 900 % 800
cy = 700 // 600





class InfiniteBackground:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h



    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)                        # quadrant 3
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h)                 # quadrant 2
        self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)                 # quadrant 4
        self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)          # quadrant 1

    def update(self):

        # quadrant 3
        self.q3l = (int(server.boy.x) - self.cw // 2) % self.w
        self.q3b = (int(server.boy.y) - self.ch // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)

        # quadrant 2
        self.q2l = 0
        self.q2b = 0
        self.q2w = 0
        self.q2h = 0

        # quadrand 4
        self.q4l = 0
        self.q4b = 0
        self.q4w = 0
        self.q4h = 0

        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = 0
        self.q1h = 0


    def handle_event(self, event):
        pass





