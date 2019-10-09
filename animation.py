from graph import *
import math

bird_color = (51, 0, 29)

basic_bird_list = [(0, 0), (-5, 0), (-10, -1), (-15, -2),
                   (-20, -3.5), (-25, -6), (-30, -9),
                   (-35, -12.5), (-37.5, -15), (-40, -20),
                   (-30, -20), (-20, -18), (-10, -15),
                   (-5, -13), (0, -10), (3.5, -8), (5, -10),
                   (7, -13), (10, -16), (15, -18.5),
                   (20, -20), (30, -22), (40, -20)]


def move_vector_list_by(vector_list: list, shift: tuple):
    return list((point_vec[0] + shift[0], point_vec[1] + shift[1]) for point_vec in vector_list)


def scale_move_vector_list(vector_list, scale_factor, x_pos, y_pos, reflect):  # reflect is a bool
    refl = 1  # constant for reflection
    if reflect:
        refl = -1
    return list((p[0] * scale_factor * refl + x_pos, p[1] * scale_factor + y_pos) for p in vector_list)


def rotate_vector_list(vector_list, x_0, y_0, angle_rad):  # rotate around x_0, y_0
    a = angle_rad
    shifted_list = list((p[0] - x_0, p[1] - y_0) for p in vector_list)
    rotated_list = list(
        (p[0] * math.cos(a) - p[1] * math.sin(a), p[0] * math.sin(a) + p[1] * math.cos(a)) for p in shifted_list)
    return list((p[0] + x_0, p[1] + y_0) for p in rotated_list)


def draw_rotated_vector_list(vector_list, x_0, y_0, angle_rad):
    polygon(rotate_vector_list(vector_list, x_0, y_0, angle_rad))


def draw_scaled_bird(scale_factor, x_bird, y_bird, reflect):
    brushColor(bird_color)
    penColor(bird_color)
    polygon(scale_move_vector_list(basic_bird_list, scale_factor, x_bird, y_bird, reflect))


def draw_symmetrical_bird(x_bird, y_bird, scale_factor):
    draw_scaled_bird(scale_factor, x_bird, y_bird, False)
    draw_scaled_bird(scale_factor, x_bird, y_bird, True)


def bird(xb, yb, mb):  # changed by draw scaled bird
    polygon([(xb, yb), (xb - 5 * mb, yb), (xb - 10 * mb, yb - 1 * mb), (xb - 15 * mb, yb - 2 * mb),
             (xb - 20 * mb, yb - 3.5 * mb), (xb - 25 * mb, yb - 6 * mb), (xb - 30 * mb, yb - 9 * mb),
             (xb - 35 * mb, yb - 12.5 * mb), (xb - 37.5 * mb, yb - 15 * mb), (xb - 40 * mb, yb - 20 * mb),
             (xb - 30 * mb, yb - 20 * mb), (xb - 20 * mb, yb - 18 * mb), (xb - 10 * mb, yb - 15 * mb),
             (xb - 5 * mb, yb - 13 * mb), (xb, yb - 10 * mb), (xb + 3.5 * mb, yb - 8 * mb), (xb + 5 * mb, yb - 10 * mb),
             (xb + 7 * mb, yb - 13 * mb), (xb + 10 * mb, yb - 16 * mb), (xb + 15 * mb, yb - 18.5 * mb),
             (xb + 20 * mb, yb - 20 * mb), (xb + 30 * mb, yb - 22 * mb), (xb + 40 * mb, yb - 20 * mb)])


xf1 = [35, 50, 65, 80, 95, 110, 125, 140, 155, 170, 185, 200, 215, 230, 245]
yf1 = [(-pnt ** 2.95) * 0.00001 + 190 for pnt in xf1]
xf2 = [615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670, 675, 680, 685, 690, 695, 700, 705, 710, 715, 720]
yf2 = [math.sin(math.pi / 85 * pnt - 21.16) * 75 / 2 + 88 for pnt in xf2]
xf3 = [25, 35, 45, 55, 65, 75, 85, 95, 105, 125, 135]
yf3 = [0.02727 * pnt ** 2 - 4.0909 * pnt + 349.77 for pnt in xf3]
xf4 = [520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640]
yf4 = [math.sin(math.pi / 235 * pnt - 3.58) * 65 + 265 for pnt in xf4]
xf5 = [365, 375, 385, 395, 405, 415, 425, 435, 445, 455]
yf5 = [math.sin(-math.pi / 450 * pnt + 4.71) * 350 / 2 + 300 for pnt in xf5]
xf6 = [675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 1000]
yf6 = [math.sin(math.pi / 275 * pnt - 6.71) * 170 / 2 + 377 for pnt in xf6]
enumerate(xf1)
enumerate(yf1)
enumerate(xf2)
enumerate(yf2)
enumerate(xf3)
enumerate(yf3)
enumerate(xf4)
enumerate(yf4)
enumerate(xf5)
enumerate(yf5)
canvasSize(1000, 500)
windowSize(1000, 500)

back_mountain = [(1000, 160), (10, 225), (20, 185), (xf1[0], yf1[0]), (xf1[1], yf1[1]), (xf1[2], yf1[2]),
                 (xf1[3], yf1[4]),
                 (xf1[5], yf1[5]), (xf1[6], yf1[6]), (xf1[7], yf1[7]), (xf1[8], yf1[8]), (xf1[9], yf1[9]),
                 (xf1[10], yf1[10]),
                 (xf1[11], yf1[11]), (xf1[12], yf1[12]), (xf1[13], yf1[13]), (xf1[14], yf1[14]), (325, 100), (350, 125),
                 (435, 175), (490, 165), (515, 180), (565, 130), (595, 140), (615, 125), (xf2[0], yf2[0]),
                 (xf2[1], yf2[1]),
                 (xf2[2], yf2[2]), (xf2[3], yf2[3]), (xf2[4], yf2[4]), (xf2[5], yf2[5]), (xf2[6], yf2[6]),
                 (xf2[7], yf2[7]),
                 (xf2[8], yf2[8]), (xf2[9], yf2[9]), (xf2[10], yf2[10]), (xf2[11], yf2[11]), (xf2[12], yf2[12]),
                 (xf2[13], yf2[13]), (xf2[14], yf2[14]), (xf2[15], yf2[15]), (xf2[16], yf2[16]), (xf2[17], yf2[17]),
                 (xf2[18], yf2[18]), (xf2[19], yf2[19]), (xf2[20], yf2[20]), (750, 115), (790, 110), (840, 135),
                 (930, 120)]

middle_mountain = [(1000, 300), (0, 350), (0, 245), (5, 245), (25, 265), (xf3[0], yf3[0]), (xf3[1], yf3[1]),
                   (xf3[2], yf3[2]),
                   (xf3[3], yf3[3]), (xf3[4], yf3[4]), (xf3[5], yf3[5]), (xf3[6], yf3[6]), (xf3[7], yf3[7]),
                   (xf3[8], yf3[8]),
                   (xf3[9], yf3[9]), (xf3[10], yf3[10]), (175, 240), (235, 275), (255, 215), (320, 235), (385, 270),
                   (520, 250),
                   (xf4[0], yf4[0]), (xf4[1], yf4[1]), (xf4[2], yf4[2]), (xf4[3], yf4[3]), (xf4[4], yf4[4]),
                   (xf4[5], yf4[5]),
                   (xf4[6], yf4[6]), (xf4[7], yf4[7]), (xf4[8], yf4[8]), (xf4[9], yf4[9]), (xf4[10], yf4[10]),
                   (xf4[11], yf4[11]),
                   (750, 250), (800, 210), (835, 235), (860, 205), (930, 210), (1000, 160)]


penColor(255, 255, 0)
brushColor(255, 255, 0)
circle(475, 95, 50)


def shift_birds():
    penColor(255, 204, 153)
    brushColor(255, 204, 153)
    rectangle(0, 0, 1000, 100)
    penColor(255, 229, 204)
    brushColor(255, 229, 204)
    polygon([(0, 100), (1000, 100), (1000, 215), (0, 200)])
    penColor(255, 255, 153)
    brushColor(255, 255, 153)
    polygon([(0, 200), (1000, 215), (1000, 300), (0, 350)])
    penColor(188, 143, 143)
    brushColor(188, 143, 143)
    polygon([(0, 350), (1000, 300), (1000, 500), (0, 500)])

    penColor(225, 153, 51)
    brushColor(255, 153, 51)
    draw_rotated_vector_list(back_mountain, 500, 100, 0.13)
    penColor(153, 0, 0)
    brushColor(153, 0, 0)
    draw_rotated_vector_list(middle_mountain, 500, 300, 0.13)
    penColor(51, 0, 51)
    brushColor(51, 0, 51)
    polygon(
        [(1000, 500), (0, 500), (0, 240), (100, 265), (200, 365), (xf5[0], yf5[0]), (xf5[1], yf5[1]), (xf5[2], yf5[2]),
         (xf5[3], yf5[3]), (xf5[4], yf5[4]), (xf5[5], yf5[5]), (xf5[6], yf5[6]), (xf5[7], yf5[7]), (xf5[8], yf5[8]),
         (xf5[9], yf5[9]), (650, 435), (675, 450), (xf6[0], yf6[0]), (xf6[1], yf6[1]), (xf6[2], yf6[2]),
         (xf6[3], yf6[3]), (xf6[4], yf6[4]), (xf6[5], yf6[5]), (xf6[6], yf6[6]), (xf6[7], yf6[7]), (xf6[8], yf6[8]),
         (xf6[9], yf6[9]), (xf6[10], yf6[10]), (xf6[11], yf6[11]), (xf6[12], yf6[12])])

    global basic_bird_list
    basic_bird_list = move_vector_list_by(basic_bird_list, (2.5, 0))
    draw_scaled_bird(1, 750, 400, 1)
    draw_scaled_bird(0.8, 650, 330, False)
    draw_scaled_bird(0.5, 775, 340, False)
    draw_scaled_bird(0.5, 675, 350, True)
    draw_scaled_bird(0.5, 475, 207, False)
    draw_scaled_bird(0.5, 475, 170, True)
    draw_scaled_bird(0.5, 425, 225, True)
    draw_scaled_bird(0.5, 415, 160, False)


onTimer(shift_birds, 50)

run()
