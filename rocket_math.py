import math
import matplotlib.pyplot as h_t
import matplotlib.pyplot as v_t
import matplotlib.pyplot as t_t

c = 0.22
p_v = 1.2
s = 0.0019625
v = 243
h_list = list()
flag = True
time_1 = 0
s_rocket = 0
s_list = list()
tick = 0
x_list = list()
flag_up = True
v_list = list()
t_list = list()
c_abs = 1700
q = 0
print("                     Rocket Math v0.35                     ")
print("---------------------Параметры ракеты---------------------")
p_engine = float(input("Полный импульс ТТРД: "))
m_rocket = float(input("Масса ракеты(с топливом), кг: "))
v_parash = float(input("Скорость приземления на парашюте, м/с: "))
d_golov = float(input("Диаметр головного обтекателя(ГС), мм: "))
c = float(input("Коэффициент сопротивления(зависит от формы ГС): "))
m_golov = float(input("Масса ГС(для расчёта нагрева), г: "))
print("---------------------Параметры полёта---------------------")
m_golov = m_golov * 0.001
d_golov = d_golov * 0.001
s = 3.14 * (d_golov/2) ** 2

v_rocket = 1e7
v_rocket = p_engine / m_rocket
h_rocket = (v_rocket ** 2) / (2 * 9.81)
t_rocket = math.sqrt(2 * h_rocket / 9.81)
v = -v_rocket
v_rocket = v_rocket - 7
while flag:
    tick += 0.1
    if v_rocket > 0 and flag_up:
        s_bit_up = 0.1 * v_rocket
        s_rocket += s_bit_up
        s_list.append(s_rocket)
        f = 0.2 * c * p_v * s * v_rocket ** 2
        q = q + (0.5 * c * p_v * s * v_rocket ** 3 * 0.1)
        t_K = q / (c_abs * m_golov)
        t_K = t_K * 0.85
        t_list.append(t_K)
        v_rocket -= 0.981 + f/m_rocket
    else:
        if s_rocket < 0:
            flag = False
        flag_up = False
        s_bit_up = 0.1 * v_rocket
        s_rocket += s_bit_up
        s_list.append(s_rocket)
        v_rocket = - v_parash
        t_K = t_K * 0.995
        t_list.append(t_K)
    x_list.append(tick)
    v_list.append(v_rocket)
print("Максимальная скорость:", max(v_list), "м/с")
print("Максимальная высота(апогей):", max(s_list), "м")
print("Максимальная температура ГС:", max(t_list), "°C")
print("Общее время полёта:", tick, "с")
print("----------------------------------------------------------")
h_t.title('Высота от времени')
h_t.plot(x_list, s_list)
h_t.show()
v_t.title('Скорость от времени')
v_t.plot(x_list, v_list)
v_t.show()
min_length = min(len(x_list), len(t_list))
x_list = x_list[:min_length]
t_list = t_list[:min_length]
h_t.title('Температура ГС от времени')
t_t.plot(x_list, t_list)
t_t.show()