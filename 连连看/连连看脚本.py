# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:连连看脚本.py
@Time:2022/5/11 16:57

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
# -*- coding:utf-8 -*-
import cv2
import numpy as np
import win32api
import win32gui
import win32con
from PIL import ImageGrab
import time
import random

# 窗体标题  用于定位游戏窗体
WINDOW_TITLE = "QQ游戏 - 连连看角色版"
# 时间间隔随机生成 [MIN,MAX]
TIME_INTERVAL_MAX = 0
TIME_INTERVAL_MIN = 0
# 游戏区域距离顶点的x偏移
MARGIN_LEFT = 10
# 游戏区域距离顶点的y偏移
MARGIN_HEIGHT = 180
# 横向的方块数量
H_NUM = 19
# 纵向的方块数量
V_NUM = 11
# 方块宽度
POINT_WIDTH = 31
# 方块高度
POINT_HEIGHT = 35
# 空图像编号
EMPTY_ID = 0
# 切片处理时候的左上、右下坐标：
SUB_LT_X = 8
SUB_LT_Y = 8
SUB_RB_X = 27
SUB_RB_Y = 27
# 游戏的最多消除次数
MAX_ROUND = 200


def getGameWindow():
    # FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
    window = win32gui.FindWindow(None, WINDOW_TITLE)

    # 没有定位到游戏窗体
    while not window:
        print('Failed to locate the game window , reposition the game window after 10 seconds...')
        time.sleep(10)
        window = win32gui.FindWindow(None, WINDOW_TITLE)

    # 定位到游戏窗体
    # 置顶游戏窗口
    win32gui.SetForegroundWindow(window)
    pos = win32gui.GetWindowRect(window)
    print("Game windows at " + str(pos))
    return (pos[0], pos[1])


def getScreenImage():
    print('Shot screen...')
    # 获取屏幕截图 Image类型对象
    scim = ImageGrab.grab()
    scim.save('screen.png')
    # 用opencv读取屏幕截图
    # 获取ndarray
    return cv2.imread("screen.png")


def getAllSquare(screen_image, game_pos):
    print('Processing pictures...')
    # 通过游戏窗体定位
    # 加上偏移量获取游戏区域
    game_x = game_pos[0] + MARGIN_LEFT
    game_y = game_pos[1] + MARGIN_HEIGHT

    # 从游戏区域左上开始
    # 把图像按照具体大小切割成相同的小块
    # 切割标准是按照小块的横纵坐标
    all_square = []
    for x in range(0, H_NUM):
        for y in range(0, V_NUM):
            # ndarray的切片方法 ：[纵坐标起始位置：纵坐标结束为止，横坐标起始位置：横坐标结束位置]
            square = screen_image[game_y + y * POINT_HEIGHT:game_y + (y + 1) * POINT_HEIGHT,
                     game_x + x * POINT_WIDTH:game_x + (x + 1) * POINT_WIDTH]
            all_square.append(square)

    # 因为有些图片的边缘会造成干扰，所以统一把图片往内缩小一圈
    # 对所有的方块进行处理 ，去掉边缘一圈后返回
    finalresult = []
    for square in all_square:
        s = square[SUB_LT_Y:SUB_RB_Y, SUB_LT_X:SUB_RB_X]
        finalresult.append(s)
    return finalresult


# 判断列表中是否存在相同图形
# 存在返回进行判断图片所在的id
# 否则返回-1
def isImageExist(img, img_list):
    i = 0
    for existed_img in img_list:
        # 两个图片进行比较 返回的是两个图片的标准差
        b = np.subtract(existed_img, img)
        # 若标准差全为0 即两张图片没有区别
        if not np.any(b):
            return i
        i = i + 1
    return -1


def getAllSquareTypes(all_square):
    print("Init pictures types...")
    types = []
    # number列表用来记录每个id的出现次数
    number = []
    # 当前出现次数最多的方块
    # 这里我们默认出现最多的方块应该是空白块
    nowid = 0;
    for square in all_square:
        nid = isImageExist(square, types)
        # 如果这个图像不存在则插入列表
        if nid == -1:
            types.append(square)
            number.append(1);
        else:
            # 若这个图像存在则给计数器 + 1
            number[nid] = number[nid] + 1
            if (number[nid] > number[nowid]):
                nowid = nid
    # 更新EMPTY_ID
    # 即判断在当前这张图中的空白块id
    global EMPTY_ID
    EMPTY_ID = nowid
    print('EMPTY_ID = ' + str(EMPTY_ID))
    return types


# 将二维图片矩阵转换为二维数字矩阵
# 注意因为在上面对截屏切片时是以列为优先切片的
# 所以生成的record二维矩阵每行存放的其实是游戏屏幕中每列的编号
# 换个说法就是record其实是游戏屏幕中心对称后的列表
def getAllSquareRecord(all_square_list, types):
    print("Change map...")
    record = []
    line = []
    for square in all_square_list:
        num = 0
        for type in types:
            res = cv2.subtract(square, type)
            if not np.any(res):
                line.append(num)
                break
            num += 1
        # 每列的数量为V_NUM
        # 那么当当前的line列表中存在V_NUM个方块时我们认为本列处理完毕
        if len(line) == V_NUM:
            print(line);
            record.append(line)
            line = []
    return record


def canConnect(x1, y1, x2, y2, r):
    result = r[:]

    # 如果两个图像中有一个为0 直接返回False
    if result[x1][y1] == EMPTY_ID or result[x2][y2] == EMPTY_ID:
        return False
    if x1 == x2 and y1 == y2:
        return False
    if result[x1][y1] != result[x2][y2]:
        return False
    # 判断横向连通
    if horizontalCheck(x1, y1, x2, y2, result):
        return True
    # 判断纵向连通
    if verticalCheck(x1, y1, x2, y2, result):
        return True
    # 判断一个拐点可连通
    if turnOnceCheck(x1, y1, x2, y2, result):
        return True
    # 判断两个拐点可连通
    if turnTwiceCheck(x1, y1, x2, y2, result):
        return True
    # 不可联通返回False
    return False


def horizontalCheck(x1, y1, x2, y2, result):
    if x1 == x2 and y1 == y2:
        return False
    if x1 != x2:
        return False
    startY = min(y1, y2)
    endY = max(y1, y2)
    # 判断两个方块是否相邻
    if (endY - startY) == 1:
        return True
    # 判断两个方块通路上是否都是0，有一个不是，就说明不能联通，返回false
    for i in range(startY + 1, endY):
        if result[x1][i] != EMPTY_ID:
            return False
    return True


def verticalCheck(x1, y1, x2, y2, result):
    if x1 == x2 and y1 == y2:
        return False

    if y1 != y2:
        return False
    startX = min(x1, x2)
    endX = max(x1, x2)
    # 判断两个方块是否相邻
    if (endX - startX) == 1:
        return True
    # 判断两方块儿通路上是否可连。
    for i in range(startX + 1, endX):
        if result[i][y1] != EMPTY_ID:
            return False
    return True


def turnOnceCheck(x1, y1, x2, y2, result):
    if x1 == x2 or y1 == y2:
        return False

    cx = x1
    cy = y2
    dx = x2
    dy = y1
    # 拐点为空，从第一个点到拐点并且从拐点到第二个点可通，则整条路可通。
    if result[cx][cy] == EMPTY_ID:
        if horizontalCheck(x1, y1, cx, cy, result) and verticalCheck(cx, cy, x2, y2, result):
            return True
    if result[dx][dy] == EMPTY_ID:
        if verticalCheck(x1, y1, dx, dy, result) and horizontalCheck(dx, dy, x2, y2, result):
            return True
    return False


def turnTwiceCheck(x1, y1, x2, y2, result):
    if x1 == x2 and y1 == y2:
        return False

    # 遍历整个数组找合适的拐点
    for i in range(0, len(result)):
        for j in range(0, len(result[1])):
            # 不为空不能作为拐点
            if result[i][j] != EMPTY_ID:
                continue
            # 不和被选方块在同一行列的不能作为拐点
            if i != x1 and i != x2 and j != y1 and j != y2:
                continue
            # 作为交点的方块不能作为拐点
            if (i == x1 and j == y2) or (i == x2 and j == y1):
                continue
            if turnOnceCheck(x1, y1, i, j, result) and (
                    horizontalCheck(i, j, x2, y2, result) or verticalCheck(i, j, x2, y2, result)):
                return True
            if turnOnceCheck(i, j, x2, y2, result) and (
                    horizontalCheck(x1, y1, i, j, result) or verticalCheck(x1, y1, i, j, result)):
                return True
    return False


def autoRelease(result, game_x, game_y):
    # 遍历地图
    for i in range(0, len(result)):
        for j in range(0, len(result[0])):
            # 当前位置非空
            if result[i][j] != EMPTY_ID:
                # 再次遍历地图 寻找另一个满足条件的图片
                for m in range(0, len(result)):
                    for n in range(0, len(result[0])):
                        if result[m][n] != EMPTY_ID:
                            # 若可以执行消除
                            if canConnect(i, j, m, n, result):
                                # 消除的两个位置设置为空
                                result[i][j] = EMPTY_ID
                                result[m][n] = EMPTY_ID
                                print('Remove ：' + str(i + 1) + ',' + str(j + 1) + ' and ' + str(m + 1) + ',' + str(
                                    n + 1))

                                # 计算当前两个位置的图片在游戏中应该存在的位置
                                x1 = game_x + j * POINT_WIDTH
                                y1 = game_y + i * POINT_HEIGHT
                                x2 = game_x + n * POINT_WIDTH
                                y2 = game_y + m * POINT_HEIGHT

                                # 模拟鼠标点击第一个图片所在的位置
                                win32api.SetCursorPos((x1 + 15, y1 + 18))
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1 + 15, y1 + 18, 0, 0)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1 + 15, y1 + 18, 0, 0)

                                # 等待随机时间 ，防止检测
                                time.sleep(random.uniform(TIME_INTERVAL_MIN, TIME_INTERVAL_MAX))

                                # 模拟鼠标点击第二个图片所在的位置
                                win32api.SetCursorPos((x2 + 15, y2 + 18))
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x2 + 15, y2 + 18, 0, 0)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2 + 15, y2 + 18, 0, 0)
                                time.sleep(random.uniform(TIME_INTERVAL_MIN, TIME_INTERVAL_MAX))
                                # 执行消除后返回True
                                return True
    return False


def autoRemove(squares, game_pos):
    game_x = game_pos[0] + MARGIN_LEFT
    game_y = game_pos[1] + MARGIN_HEIGHT
    # 重复一次消除直到到达最多消除次数
    while True:
        if not autoRelease(squares, game_x, game_y):
            # 当不再有可消除的方块时结束 ， 返回消除数量
            return


if __name__ == '__main__':
    random.seed()
    # i. 定位游戏窗体
    game_pos = getGameWindow()
    print("====是否找到窗口===", game_pos)
    time.sleep(1)
    # ii. 获取屏幕截图
    screen_image = getScreenImage()
    # iii. 对截图切片，形成一张二维地图
    all_square_list = getAllSquare(screen_image, game_pos)
    # iv. 获取所有类型的图形，并编号
    types = getAllSquareTypes(all_square_list)
    # v. 讲获取的图片地图转换成数字矩阵
    result = np.transpose(getAllSquareRecord(all_square_list, types))
    # vi. 执行消除 , 并输出消除数量
    print(' ' + str(autoRemove(result, game_pos)))
