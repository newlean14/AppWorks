import math


xxx = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"


def neg(a):
    return str(a).replace("0", "2").replace("1", "0").replace("2", "1")


def con(a, b):
    num = -1
    answer = []
    while num <= 30:
        num = num + 1
        value = str((int(a[num]) * int(b[num])))
        answer.append(value)
    return ''.join(answer)


def dis(a, b):
    num1 = -1
    answer = []
    while num1 <= 30:
        num1 = num1 + 1
        value1 = str((int(a[num1]) + int(b[num1]))).replace("2", "0")
        answer.append(value1)
    return ''.join(answer)


def mod(a, b):
    f = int(math.pow(2, 32))
    value3 = int(a, 2)
    value4 = int(b, 2)
    return bin((value3 + value4) % f)[2:].zfill(32)


def mod_1(a):
    return (447 - a) % 512


def rot_r(a, b):
    return a[32 - b:32] + a[0:(32 - b)]


def sh_r(a, b):
    return "0"*b + a[0:(32 - b)]


def sig_0(a):
    return dis(dis(rot_r(a, 7), rot_r(a, 18)), sh_r(a, 3))


def sig_1(a):
    return dis(dis(rot_r(a, 17), rot_r(a, 19)), sh_r(a, 10))


def ch(a, b, c):
    return dis(con(a, b), con(neg(a), c))


def maj(a, b, c):
    return dis(dis(con(a, b), con(a, c)), con(b, c))


def sum_0(a):
    return dis(dis(rot_r(a, 2), rot_r(a, 13)), rot_r(a, 22))


def sum_1(a):
    return dis(dis(rot_r(a, 6), rot_r(a, 11)), rot_r(a, 25))


def sha():
    typed_len = int(len(xxx))
    num2 = -1
    answer1 = []
    while num2 <= typed_len-2:
        num2 = num2 + 1
        value5 = bin(ord(xxx[num2]))[2:].zfill(8)
        answer1.append(value5)
    return ''.join(answer1) + ("1" + "0" * int(mod_1(int(typed_len * 8))) + bin(typed_len * 8)[2:].zfill(64))


# 質數
def prime_or_not(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    else:
        return True


def get_first_n_prime(n):
    while True:
        if prime_or_not(n):
            yield n
        n += 1


def get_nth_prime_number(n, initial_number=2):
    count = 0
    for next_prime in get_first_n_prime(initial_number):
        count += 1
        if count < n:
            continue
        else:
            return next_prime
# 質數


def initiate_hash_two(a):
    sqr__ = math.pow(get_nth_prime_number(a, 2), 1 / 2) - math.floor(math.pow(get_nth_prime_number(a, 2), 1 / 2))
    return bin(math.floor(sqr__ * math.pow(16, 8)))[2:].zfill(32)


def initiate_hash_three(a):
    sqr__ = math.pow(get_nth_prime_number(a, 2), 1 / 3) - math.floor(math.pow(get_nth_prime_number(a, 2), 1 / 3))
    return bin(math.floor(sqr__ * math.pow(16, 8)))[2:].zfill(32)


def w_n(a):
    return str(sha()[32 * (a - 1):32 * a])


def seventeen(a):
    return mod(mod(mod(sig_1(w_n(a - 2)), w_n(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


W17 = seventeen(17)
W18 = seventeen(18)


def seventeen_0(a):
    if a <= 16:
        return str(sha()[32 * (a - 1):32 * a])
    elif 17 <= a <= 18:
        return seventeen(a)


def seventeen_1(a):
    if a <= 18:
        return seventeen_0(a)
    elif 19 <= a <= 20:
        return mod(mod(mod(sig_1(seventeen_0(a - 2)), w_n(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_2(a):
    if a <= 20:
        return seventeen_1(a)
    elif 21 <= a <= 22:
        return mod(mod(mod(sig_1(seventeen_1(a - 2)), w_n(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_3(a):
    if a <= 22:
        return seventeen_2(a)
    elif a == 23:
        return mod(mod(mod(sig_1(seventeen_2(a - 2)), w_n(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))
    elif a == 24:
        return mod(mod(mod(sig_1(seventeen_2(a - 2)), seventeen_2(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_4(a):
    if a <= 24:
        return seventeen_3(a)
    elif 25 <= a <= 26:
        return mod(mod(mod(sig_1(seventeen_3(a - 2)), seventeen_3(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_5(a):
    if a <= 26:
        return seventeen_4(a)
    elif 27 <= a <= 28:
        return mod(mod(mod(sig_1(seventeen_4(a - 2)), seventeen_4(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_6(a):
    if a <= 28:
        return seventeen_5(a)
    elif 29 <= a <= 30:
        return mod(mod(mod(sig_1(seventeen_5(a - 2)), seventeen_5(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_7(a):
    if a <= 30:
        return seventeen_6(a)
    elif a == 31:
        return mod(mod(mod(sig_1(seventeen_6(a - 2)), seventeen_6(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))
    elif a == 32:
        return mod(mod(mod(sig_1(seventeen_6(a - 2)), seventeen_6(a - 7)), sig_0(seventeen_6(a - 15))), w_n(a - 16))


def s_v_8(a):
    s_v_7 = seventeen_7
    if a <= 32:
        return s_v_7(a)
    elif 33 <= a <= 34:
        return mod(mod(mod(sig_1(s_v_7(a - 2)), s_v_7(a - 7)), sig_0(s_v_7(a - 15))), s_v_7(a - 16))


def s_v_9(a):
    if a <= 34:
        return s_v_8(a)
    elif 35 <= a <= 36:
        return mod(mod(mod(sig_1(s_v_8(a - 2)), s_v_8(a - 7)), sig_0(s_v_8(a - 15))), s_v_8(a - 16))


def s_v_10(a):
    if a <= 36:
        return s_v_9(a)
    elif 37 <= a <= 38:
        return mod(mod(mod(sig_1(s_v_9(a - 2)), s_v_9(a - 7)), sig_0(s_v_9(a - 15))), s_v_9(a - 16))


def s_v_11(a):
    if a <= 38:
        return s_v_10(a)
    elif 39 <= a <= 40:
        return mod(mod(mod(sig_1(s_v_10(a - 2)), s_v_10(a - 7)), sig_0(s_v_10(a - 15))), s_v_10(a - 16))


def s_v_12(a):
    if a <= 40:
        return s_v_11(a)
    elif 41 <= a <= 42:
        return mod(mod(mod(sig_1(s_v_11(a - 2)), s_v_11(a - 7)), sig_0(s_v_11(a - 15))), s_v_11(a - 16))


def s_v_13(a):
    if a <= 42:
        return s_v_12(a)
    elif 43 <= a <= 44:
        return mod(mod(mod(sig_1(s_v_12(a - 2)), s_v_12(a - 7)), sig_0(s_v_12(a - 15))), s_v_12(a - 16))


def s_v_14(a):
    if a <= 44:
        return s_v_13(a)
    elif 45 <= a <= 46:
        return mod(mod(mod(sig_1(s_v_13(a - 2)), s_v_13(a - 7)), sig_0(s_v_13(a - 15))), s_v_13(a - 16))


def s_v_15(a):
    if a <= 46:
        return s_v_14(a)
    elif 47 <= a <= 48:
        return mod(mod(mod(sig_1(s_v_14(a - 2)), s_v_14(a - 7)), sig_0(s_v_14(a - 15))), s_v_14(a - 16))


def s_v_16(a):
    if a <= 48:
        return s_v_15(a)
    elif 49 <= a <= 50:
        return mod(mod(mod(sig_1(s_v_15(a - 2)), s_v_15(a - 7)), sig_0(s_v_15(a - 15))), s_v_15(a - 16))


def s_v_17(a):
    if a <= 50:
        return s_v_16(a)
    elif 51 <= a <= 52:
        return mod(mod(mod(sig_1(s_v_16(a - 2)), s_v_16(a - 7)), sig_0(s_v_16(a - 15))), s_v_16(a - 16))


def s_v_18(a):
    if a <= 52:
        return s_v_17(a)
    elif 53 <= a <= 54:
        return mod(mod(mod(sig_1(s_v_17(a - 2)), s_v_17(a - 7)), sig_0(s_v_17(a - 15))), s_v_17(a - 16))


def s_v_19(a):
    if a <= 54:
        return s_v_18(a)
    elif 55 <= a <= 56:
        return mod(mod(mod(sig_1(s_v_18(a - 2)), s_v_18(a - 7)), sig_0(s_v_18(a - 15))), s_v_18(a - 16))


def s_v_20(a):
    if a <= 56:
        return s_v_19(a)
    elif 57 <= a <= 58:
        return mod(mod(mod(sig_1(s_v_19(a - 2)), s_v_19(a - 7)), sig_0(s_v_19(a - 15))), s_v_19(a - 16))


def s_v_21(a):
    if a <= 58:
        return s_v_20(a)
    elif 59 <= a <= 60:
        return mod(mod(mod(sig_1(s_v_20(a - 2)), s_v_20(a - 7)), sig_0(s_v_20(a - 15))), s_v_20(a - 16))


def s_v_22(a):
    if a <= 60:
        return s_v_21(a)
    elif 61 <= a <= 62:
        return mod(mod(mod(sig_1(s_v_21(a - 2)), s_v_21(a - 7)), sig_0(s_v_21(a - 15))), s_v_21(a - 16))


def s_v_23(a):
    if a <= 62:
        return s_v_22(a)
    elif 63 <= a <= 64:
        return mod(mod(mod(sig_1(s_v_22(a - 2)), s_v_22(a - 7)), sig_0(s_v_22(a - 15))), s_v_22(a - 16))


# 001


def t__1(a):
    t_1 = initiate_hash_two(8)
    t_2 = sum_1(initiate_hash_two(5))
    t_3 = ch(initiate_hash_two(5), initiate_hash_two(6), initiate_hash_two(7))
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(initiate_hash_two(1))
    t_2 = maj(initiate_hash_two(1), initiate_hash_two(2), initiate_hash_two(3))
    return mod(t_1, t_2)


ini_8 = initiate_hash_two(7)
ini_7 = initiate_hash_two(6)
ini_6 = initiate_hash_two(5)
ini_5 = mod(initiate_hash_two(4), t__1(1))
ini_4 = initiate_hash_two(3)
ini_3 = initiate_hash_two(2)
ini_2 = initiate_hash_two(1)
ini_1 = mod(t__1(1), t__2())


# 002


def t__1(a):
    t_1 = ini_8
    t_2 = sum_1(ini_5)
    t_3 = ch(ini_5, ini_6, ini_7)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1)
    t_2 = maj(ini_1, ini_2, ini_3)
    return mod(t_1, t_2)


ini_8_02 = ini_7
ini_7_02 = ini_6
ini_6_02 = ini_5
ini_5_02 = mod(ini_4, t__1(2))
ini_4_02 = ini_3
ini_3_02 = ini_2
ini_2_02 = ini_1
ini_1_02 = mod(t__1(2), t__2())


# 003


def t__1(a):
    t_1 = ini_8_02
    t_2 = sum_1(ini_5_02)
    t_3 = ch(ini_5_02, ini_6_02, ini_7_02)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_02)
    t_2 = maj(ini_1_02, ini_2_02, ini_3_02)
    return mod(t_1, t_2)


ini_8_03 = ini_7_02
ini_7_03 = ini_6_02
ini_6_03 = ini_5_02
ini_5_03 = mod(ini_4_02, t__1(3))
ini_4_03 = ini_3_02
ini_3_03 = ini_2_02
ini_2_03 = ini_1_02
ini_1_03 = mod(t__1(3), t__2())


# 004


def t__1(a):
    t_1 = ini_8_03
    t_2 = sum_1(ini_5_03)
    t_3 = ch(ini_5_03, ini_6_03, ini_7_03)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_03)
    t_2 = maj(ini_1_03, ini_2_03, ini_3_03)
    return mod(t_1, t_2)


ini_8_04 = ini_7_03
ini_7_04 = ini_6_03
ini_6_04 = ini_5_03
ini_5_04 = mod(ini_4_03, t__1(4))
ini_4_04 = ini_3_03
ini_3_04 = ini_2_03
ini_2_04 = ini_1_03
ini_1_04 = mod(t__1(4), t__2())


# 005


def t__1(a):
    t_1 = ini_8_04
    t_2 = sum_1(ini_5_04)
    t_3 = ch(ini_5_04, ini_6_04, ini_7_04)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_04)
    t_2 = maj(ini_1_04, ini_2_04, ini_3_04)
    return mod(t_1, t_2)


ini_8_05 = ini_7_04
ini_7_05 = ini_6_04
ini_6_05 = ini_5_04
ini_5_05 = mod(ini_4_04, t__1(5))
ini_4_05 = ini_3_04
ini_3_05 = ini_2_04
ini_2_05 = ini_1_04
ini_1_05 = mod(t__1(5), t__2())


# 006


def t__1(a):
    t_1 = ini_8_05
    t_2 = sum_1(ini_5_05)
    t_3 = ch(ini_5_05, ini_6_05, ini_7_05)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_05)
    t_2 = maj(ini_1_05, ini_2_05, ini_3_05)
    return mod(t_1, t_2)


ini_8_06 = ini_7_05
ini_7_06 = ini_6_05
ini_6_06 = ini_5_05
ini_5_06 = mod(ini_4_05, t__1(6))
ini_4_06 = ini_3_05
ini_3_06 = ini_2_05
ini_2_06 = ini_1_05
ini_1_06 = mod(t__1(6), t__2())


# 007


def t__1(a):
    t_1 = ini_8_06
    t_2 = sum_1(ini_5_06)
    t_3 = ch(ini_5_06, ini_6_06, ini_7_06)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_06)
    t_2 = maj(ini_1_06, ini_2_06, ini_3_06)
    return mod(t_1, t_2)


ini_8_07 = ini_7_06
ini_7_07 = ini_6_06
ini_6_07 = ini_5_06
ini_5_07 = mod(ini_4_06, t__1(7))
ini_4_07 = ini_3_06
ini_3_07 = ini_2_06
ini_2_07 = ini_1_06
ini_1_07 = mod(t__1(7), t__2())


# 008


def t__1(a):
    t_1 = ini_8_07
    t_2 = sum_1(ini_5_07)
    t_3 = ch(ini_5_07, ini_6_07, ini_7_07)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_07)
    t_2 = maj(ini_1_07, ini_2_07, ini_3_07)
    return mod(t_1, t_2)


ini_8_08 = ini_7_07
ini_7_08 = ini_6_07
ini_6_08 = ini_5_07
ini_5_08 = mod(ini_4_07, t__1(8))
ini_4_08 = ini_3_07
ini_3_08 = ini_2_07
ini_2_08 = ini_1_07
ini_1_08 = mod(t__1(8), t__2())


# 009


def t__1(a):
    t_1 = ini_8_08
    t_2 = sum_1(ini_5_08)
    t_3 = ch(ini_5_08, ini_6_08, ini_7_08)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_08)
    t_2 = maj(ini_1_08, ini_2_08, ini_3_08)
    return mod(t_1, t_2)


ini_8_09 = ini_7_08
ini_7_09 = ini_6_08
ini_6_09 = ini_5_08
ini_5_09 = mod(ini_4_08, t__1(9))
ini_4_09 = ini_3_08
ini_3_09 = ini_2_08
ini_2_09 = ini_1_08
ini_1_09 = mod(t__1(9), t__2())


# 0010


def t__1(a):
    t_1 = ini_8_09
    t_2 = sum_1(ini_5_09)
    t_3 = ch(ini_5_09, ini_6_09, ini_7_09)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_09)
    t_2 = maj(ini_1_09, ini_2_09, ini_3_09)
    return mod(t_1, t_2)


ini_8_010 = ini_7_09
ini_7_010 = ini_6_09
ini_6_010 = ini_5_09
ini_5_010 = mod(ini_4_09, t__1(10))
ini_4_010 = ini_3_09
ini_3_010 = ini_2_09
ini_2_010 = ini_1_09
ini_1_010 = mod(t__1(10), t__2())


# 0011


def t__1(a):
    t_1 = ini_8_010
    t_2 = sum_1(ini_5_010)
    t_3 = ch(ini_5_010, ini_6_010, ini_7_010)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_010)
    t_2 = maj(ini_1_010, ini_2_010, ini_3_010)
    return mod(t_1, t_2)


ini_8_011 = ini_7_010
ini_7_011 = ini_6_010
ini_6_011 = ini_5_010
ini_5_011 = mod(ini_4_010, t__1(11))
ini_4_011 = ini_3_010
ini_3_011 = ini_2_010
ini_2_011 = ini_1_010
ini_1_011 = mod(t__1(11), t__2())


# 0012


def t__1(a):
    t_1 = ini_8_011
    t_2 = sum_1(ini_5_011)
    t_3 = ch(ini_5_011, ini_6_011, ini_7_011)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_011)
    t_2 = maj(ini_1_011, ini_2_011, ini_3_011)
    return mod(t_1, t_2)


ini_8_012 = ini_7_011
ini_7_012 = ini_6_011
ini_6_012 = ini_5_011
ini_5_012 = mod(ini_4_011, t__1(12))
ini_4_012 = ini_3_011
ini_3_012 = ini_2_011
ini_2_012 = ini_1_011
ini_1_012 = mod(t__1(12), t__2())


# 0013


def t__1(a):
    t_1 = ini_8_012
    t_2 = sum_1(ini_5_012)
    t_3 = ch(ini_5_012, ini_6_012, ini_7_012)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_012)
    t_2 = maj(ini_1_012, ini_2_012, ini_3_012)
    return mod(t_1, t_2)


ini_8_013 = ini_7_012
ini_7_013 = ini_6_012
ini_6_013 = ini_5_012
ini_5_013 = mod(ini_4_012, t__1(13))
ini_4_013 = ini_3_012
ini_3_013 = ini_2_012
ini_2_013 = ini_1_012
ini_1_013 = mod(t__1(13), t__2())


# 0014


def t__1(a):
    t_1 = ini_8_013
    t_2 = sum_1(ini_5_013)
    t_3 = ch(ini_5_013, ini_6_013, ini_7_013)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_013)
    t_2 = maj(ini_1_013, ini_2_013, ini_3_013)
    return mod(t_1, t_2)


ini_8_014 = ini_7_013
ini_7_014 = ini_6_013
ini_6_014 = ini_5_013
ini_5_014 = mod(ini_4_013, t__1(14))
ini_4_014 = ini_3_013
ini_3_014 = ini_2_013
ini_2_014 = ini_1_013
ini_1_014 = mod(t__1(14), t__2())


# 0015


def t__1(a):
    t_1 = ini_8_014
    t_2 = sum_1(ini_5_014)
    t_3 = ch(ini_5_014, ini_6_014, ini_7_014)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_014)
    t_2 = maj(ini_1_014, ini_2_014, ini_3_014)
    return mod(t_1, t_2)


ini_8_015 = ini_7_014
ini_7_015 = ini_6_014
ini_6_015 = ini_5_014
ini_5_015 = mod(ini_4_014, t__1(15))
ini_4_015 = ini_3_014
ini_3_015 = ini_2_014
ini_2_015 = ini_1_014
ini_1_015 = mod(t__1(15), t__2())


# 0016


def t__1(a):
    t_1 = ini_8_015
    t_2 = sum_1(ini_5_015)
    t_3 = ch(ini_5_015, ini_6_015, ini_7_015)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_015)
    t_2 = maj(ini_1_015, ini_2_015, ini_3_015)
    return mod(t_1, t_2)


ini_8_016 = ini_7_015
ini_7_016 = ini_6_015
ini_6_016 = ini_5_015
ini_5_016 = mod(ini_4_015, t__1(16))
ini_4_016 = ini_3_015
ini_3_016 = ini_2_015
ini_2_016 = ini_1_015
ini_1_016 = mod(t__1(16), t__2())


# 0017


def t__1(a):
    t_1 = ini_8_016
    t_2 = sum_1(ini_5_016)
    t_3 = ch(ini_5_016, ini_6_016, ini_7_016)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_016)
    t_2 = maj(ini_1_016, ini_2_016, ini_3_016)
    return mod(t_1, t_2)


ini_8_017 = ini_7_016
ini_7_017 = ini_6_016
ini_6_017 = ini_5_016
ini_5_017 = mod(ini_4_016, t__1(17))
ini_4_017 = ini_3_016
ini_3_017 = ini_2_016
ini_2_017 = ini_1_016
ini_1_017 = mod(t__1(17), t__2())


# 0018


def t__1(a):
    t_1 = ini_8_017
    t_2 = sum_1(ini_5_017)
    t_3 = ch(ini_5_017, ini_6_017, ini_7_017)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_017)
    t_2 = maj(ini_1_017, ini_2_017, ini_3_017)
    return mod(t_1, t_2)


ini_8_018 = ini_7_017
ini_7_018 = ini_6_017
ini_6_018 = ini_5_017
ini_5_018 = mod(ini_4_017, t__1(18))
ini_4_018 = ini_3_017
ini_3_018 = ini_2_017
ini_2_018 = ini_1_017
ini_1_018 = mod(t__1(18), t__2())


# 0019


def t__1(a):
    t_1 = ini_8_018
    t_2 = sum_1(ini_5_018)
    t_3 = ch(ini_5_018, ini_6_018, ini_7_018)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_018)
    t_2 = maj(ini_1_018, ini_2_018, ini_3_018)
    return mod(t_1, t_2)


ini_8_019 = ini_7_018
ini_7_019 = ini_6_018
ini_6_019 = ini_5_018
ini_5_019 = mod(ini_4_018, t__1(19))
ini_4_019 = ini_3_018
ini_3_019 = ini_2_018
ini_2_019 = ini_1_018
ini_1_019 = mod(t__1(19), t__2())


# 0020


def t__1(a):
    t_1 = ini_8_019
    t_2 = sum_1(ini_5_019)
    t_3 = ch(ini_5_019, ini_6_019, ini_7_019)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_019)
    t_2 = maj(ini_1_019, ini_2_019, ini_3_019)
    return mod(t_1, t_2)


ini_8_020 = ini_7_019
ini_7_020 = ini_6_019
ini_6_020 = ini_5_019
ini_5_020 = mod(ini_4_019, t__1(20))
ini_4_020 = ini_3_019
ini_3_020 = ini_2_019
ini_2_020 = ini_1_019
ini_1_020 = mod(t__1(20), t__2())


# 0021


def t__1(a):
    t_1 = ini_8_020
    t_2 = sum_1(ini_5_020)
    t_3 = ch(ini_5_020, ini_6_020, ini_7_020)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_020)
    t_2 = maj(ini_1_020, ini_2_020, ini_3_020)
    return mod(t_1, t_2)


ini_8_021 = ini_7_020
ini_7_021 = ini_6_020
ini_6_021 = ini_5_020
ini_5_021 = mod(ini_4_020, t__1(21))
ini_4_021 = ini_3_020
ini_3_021 = ini_2_020
ini_2_021 = ini_1_020
ini_1_021 = mod(t__1(21), t__2())


# 0022


def t__1(a):
    t_1 = ini_8_021
    t_2 = sum_1(ini_5_021)
    t_3 = ch(ini_5_021, ini_6_021, ini_7_021)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_021)
    t_2 = maj(ini_1_021, ini_2_021, ini_3_021)
    return mod(t_1, t_2)


ini_8_022 = ini_7_021
ini_7_022 = ini_6_021
ini_6_022 = ini_5_021
ini_5_022 = mod(ini_4_021, t__1(22))
ini_4_022 = ini_3_021
ini_3_022 = ini_2_021
ini_2_022 = ini_1_021
ini_1_022 = mod(t__1(22), t__2())


# 0023


def t__1(a):
    t_1 = ini_8_022
    t_2 = sum_1(ini_5_022)
    t_3 = ch(ini_5_022, ini_6_022, ini_7_022)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_022)
    t_2 = maj(ini_1_022, ini_2_022, ini_3_022)
    return mod(t_1, t_2)


ini_8_023 = ini_7_022
ini_7_023 = ini_6_022
ini_6_023 = ini_5_022
ini_5_023 = mod(ini_4_022, t__1(23))
ini_4_023 = ini_3_022
ini_3_023 = ini_2_022
ini_2_023 = ini_1_022
ini_1_023 = mod(t__1(23), t__2())


# 0024


def t__1(a):
    t_1 = ini_8_023
    t_2 = sum_1(ini_5_023)
    t_3 = ch(ini_5_023, ini_6_023, ini_7_023)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_023)
    t_2 = maj(ini_1_023, ini_2_023, ini_3_023)
    return mod(t_1, t_2)


ini_8_024 = ini_7_023
ini_7_024 = ini_6_023
ini_6_024 = ini_5_023
ini_5_024 = mod(ini_4_023, t__1(24))
ini_4_024 = ini_3_023
ini_3_024 = ini_2_023
ini_2_024 = ini_1_023
ini_1_024 = mod(t__1(24), t__2())


# 0025


def t__1(a):
    t_1 = ini_8_024
    t_2 = sum_1(ini_5_024)
    t_3 = ch(ini_5_024, ini_6_024, ini_7_024)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_024)
    t_2 = maj(ini_1_024, ini_2_024, ini_3_024)
    return mod(t_1, t_2)


ini_8_025 = ini_7_024
ini_7_025 = ini_6_024
ini_6_025 = ini_5_024
ini_5_025 = mod(ini_4_024, t__1(25))
ini_4_025 = ini_3_024
ini_3_025 = ini_2_024
ini_2_025 = ini_1_024
ini_1_025 = mod(t__1(25), t__2())


# 0026


def t__1(a):
    t_1 = ini_8_025
    t_2 = sum_1(ini_5_025)
    t_3 = ch(ini_5_025, ini_6_025, ini_7_025)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_025)
    t_2 = maj(ini_1_025, ini_2_025, ini_3_025)
    return mod(t_1, t_2)


ini_8_026 = ini_7_025
ini_7_026 = ini_6_025
ini_6_026 = ini_5_025
ini_5_026 = mod(ini_4_025, t__1(26))
ini_4_026 = ini_3_025
ini_3_026 = ini_2_025
ini_2_026 = ini_1_025
ini_1_026 = mod(t__1(26), t__2())


# 0027


def t__1(a):
    t_1 = ini_8_026
    t_2 = sum_1(ini_5_026)
    t_3 = ch(ini_5_026, ini_6_026, ini_7_026)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_026)
    t_2 = maj(ini_1_026, ini_2_026, ini_3_026)
    return mod(t_1, t_2)


ini_8_027 = ini_7_026
ini_7_027 = ini_6_026
ini_6_027 = ini_5_026
ini_5_027 = mod(ini_4_026, t__1(27))
ini_4_027 = ini_3_026
ini_3_027 = ini_2_026
ini_2_027 = ini_1_026
ini_1_027 = mod(t__1(27), t__2())


# 0028


def t__1(a):
    t_1 = ini_8_027
    t_2 = sum_1(ini_5_027)
    t_3 = ch(ini_5_027, ini_6_027, ini_7_027)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_027)
    t_2 = maj(ini_1_027, ini_2_027, ini_3_027)
    return mod(t_1, t_2)


ini_8_028 = ini_7_027
ini_7_028 = ini_6_027
ini_6_028 = ini_5_027
ini_5_028 = mod(ini_4_027, t__1(28))
ini_4_028 = ini_3_027
ini_3_028 = ini_2_027
ini_2_028 = ini_1_027
ini_1_028 = mod(t__1(28), t__2())


# 0029


def t__1(a):
    t_1 = ini_8_028
    t_2 = sum_1(ini_5_028)
    t_3 = ch(ini_5_028, ini_6_028, ini_7_028)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_028)
    t_2 = maj(ini_1_028, ini_2_028, ini_3_028)
    return mod(t_1, t_2)


ini_8_029 = ini_7_028
ini_7_029 = ini_6_028
ini_6_029 = ini_5_028
ini_5_029 = mod(ini_4_028, t__1(29))
ini_4_029 = ini_3_028
ini_3_029 = ini_2_028
ini_2_029 = ini_1_028
ini_1_029 = mod(t__1(29), t__2())


# 0030


def t__1(a):
    t_1 = ini_8_029
    t_2 = sum_1(ini_5_029)
    t_3 = ch(ini_5_029, ini_6_029, ini_7_029)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_029)
    t_2 = maj(ini_1_029, ini_2_029, ini_3_029)
    return mod(t_1, t_2)


ini_8_030 = ini_7_029
ini_7_030 = ini_6_029
ini_6_030 = ini_5_029
ini_5_030 = mod(ini_4_029, t__1(30))
ini_4_030 = ini_3_029
ini_3_030 = ini_2_029
ini_2_030 = ini_1_029
ini_1_030 = mod(t__1(30), t__2())


# 0031


def t__1(a):
    t_1 = ini_8_030
    t_2 = sum_1(ini_5_030)
    t_3 = ch(ini_5_030, ini_6_030, ini_7_030)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_030)
    t_2 = maj(ini_1_030, ini_2_030, ini_3_030)
    return mod(t_1, t_2)


ini_8_031 = ini_7_030
ini_7_031 = ini_6_030
ini_6_031 = ini_5_030
ini_5_031 = mod(ini_4_030, t__1(31))
ini_4_031 = ini_3_030
ini_3_031 = ini_2_030
ini_2_031 = ini_1_030
ini_1_031 = mod(t__1(31), t__2())


# 0032


def t__1(a):
    t_1 = ini_8_031
    t_2 = sum_1(ini_5_031)
    t_3 = ch(ini_5_031, ini_6_031, ini_7_031)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_031)
    t_2 = maj(ini_1_031, ini_2_031, ini_3_031)
    return mod(t_1, t_2)


ini_8_032 = ini_7_031
ini_7_032 = ini_6_031
ini_6_032 = ini_5_031
ini_5_032 = mod(ini_4_031, t__1(32))
ini_4_032 = ini_3_031
ini_3_032 = ini_2_031
ini_2_032 = ini_1_031
ini_1_032 = mod(t__1(32), t__2())


# 0033


def t__1(a):
    t_1 = ini_8_032
    t_2 = sum_1(ini_5_032)
    t_3 = ch(ini_5_032, ini_6_032, ini_7_032)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_032)
    t_2 = maj(ini_1_032, ini_2_032, ini_3_032)
    return mod(t_1, t_2)


ini_8_033 = ini_7_032
ini_7_033 = ini_6_032
ini_6_033 = ini_5_032
ini_5_033 = mod(ini_4_032, t__1(33))
ini_4_033 = ini_3_032
ini_3_033 = ini_2_032
ini_2_033 = ini_1_032
ini_1_033 = mod(t__1(33), t__2())


# 0034


def t__1(a):
    t_1 = ini_8_033
    t_2 = sum_1(ini_5_033)
    t_3 = ch(ini_5_033, ini_6_033, ini_7_033)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_033)
    t_2 = maj(ini_1_033, ini_2_033, ini_3_033)
    return mod(t_1, t_2)


ini_8_034 = ini_7_033
ini_7_034 = ini_6_033
ini_6_034 = ini_5_033
ini_5_034 = mod(ini_4_033, t__1(34))
ini_4_034 = ini_3_033
ini_3_034 = ini_2_033
ini_2_034 = ini_1_033
ini_1_034 = mod(t__1(34), t__2())


# 0035


def t__1(a):
    t_1 = ini_8_034
    t_2 = sum_1(ini_5_034)
    t_3 = ch(ini_5_034, ini_6_034, ini_7_034)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_034)
    t_2 = maj(ini_1_034, ini_2_034, ini_3_034)
    return mod(t_1, t_2)


ini_8_035 = ini_7_034
ini_7_035 = ini_6_034
ini_6_035 = ini_5_034
ini_5_035 = mod(ini_4_034, t__1(35))
ini_4_035 = ini_3_034
ini_3_035 = ini_2_034
ini_2_035 = ini_1_034
ini_1_035 = mod(t__1(35), t__2())


# 0036


def t__1(a):
    t_1 = ini_8_035
    t_2 = sum_1(ini_5_035)
    t_3 = ch(ini_5_035, ini_6_035, ini_7_035)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_035)
    t_2 = maj(ini_1_035, ini_2_035, ini_3_035)
    return mod(t_1, t_2)


ini_8_036 = ini_7_035
ini_7_036 = ini_6_035
ini_6_036 = ini_5_035
ini_5_036 = mod(ini_4_035, t__1(36))
ini_4_036 = ini_3_035
ini_3_036 = ini_2_035
ini_2_036 = ini_1_035
ini_1_036 = mod(t__1(36), t__2())


# 0037


def t__1(a):
    t_1 = ini_8_036
    t_2 = sum_1(ini_5_036)
    t_3 = ch(ini_5_036, ini_6_036, ini_7_036)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_036)
    t_2 = maj(ini_1_036, ini_2_036, ini_3_036)
    return mod(t_1, t_2)


ini_8_037 = ini_7_036
ini_7_037 = ini_6_036
ini_6_037 = ini_5_036
ini_5_037 = mod(ini_4_036, t__1(37))
ini_4_037 = ini_3_036
ini_3_037 = ini_2_036
ini_2_037 = ini_1_036
ini_1_037 = mod(t__1(37), t__2())


# 0038


def t__1(a):
    t_1 = ini_8_037
    t_2 = sum_1(ini_5_037)
    t_3 = ch(ini_5_037, ini_6_037, ini_7_037)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_037)
    t_2 = maj(ini_1_037, ini_2_037, ini_3_037)
    return mod(t_1, t_2)


ini_8_038 = ini_7_037
ini_7_038 = ini_6_037
ini_6_038 = ini_5_037
ini_5_038 = mod(ini_4_037, t__1(38))
ini_4_038 = ini_3_037
ini_3_038 = ini_2_037
ini_2_038 = ini_1_037
ini_1_038 = mod(t__1(38), t__2())


# 0039


def t__1(a):
    t_1 = ini_8_038
    t_2 = sum_1(ini_5_038)
    t_3 = ch(ini_5_038, ini_6_038, ini_7_038)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_038)
    t_2 = maj(ini_1_038, ini_2_038, ini_3_038)
    return mod(t_1, t_2)


ini_8_039 = ini_7_038
ini_7_039 = ini_6_038
ini_6_039 = ini_5_038
ini_5_039 = mod(ini_4_038, t__1(39))
ini_4_039 = ini_3_038
ini_3_039 = ini_2_038
ini_2_039 = ini_1_038
ini_1_039 = mod(t__1(39), t__2())


# 0040


def t__1(a):
    t_1 = ini_8_039
    t_2 = sum_1(ini_5_039)
    t_3 = ch(ini_5_039, ini_6_039, ini_7_039)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_039)
    t_2 = maj(ini_1_039, ini_2_039, ini_3_039)
    return mod(t_1, t_2)


ini_8_040 = ini_7_039
ini_7_040 = ini_6_039
ini_6_040 = ini_5_039
ini_5_040 = mod(ini_4_039, t__1(40))
ini_4_040 = ini_3_039
ini_3_040 = ini_2_039
ini_2_040 = ini_1_039
ini_1_040 = mod(t__1(40), t__2())


# 0041


def t__1(a):
    t_1 = ini_8_040
    t_2 = sum_1(ini_5_040)
    t_3 = ch(ini_5_040, ini_6_040, ini_7_040)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_040)
    t_2 = maj(ini_1_040, ini_2_040, ini_3_040)
    return mod(t_1, t_2)


ini_8_041 = ini_7_040
ini_7_041 = ini_6_040
ini_6_041 = ini_5_040
ini_5_041 = mod(ini_4_040, t__1(41))
ini_4_041 = ini_3_040
ini_3_041 = ini_2_040
ini_2_041 = ini_1_040
ini_1_041 = mod(t__1(41), t__2())


# 0042


def t__1(a):
    t_1 = ini_8_041
    t_2 = sum_1(ini_5_041)
    t_3 = ch(ini_5_041, ini_6_041, ini_7_041)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_041)
    t_2 = maj(ini_1_041, ini_2_041, ini_3_041)
    return mod(t_1, t_2)


ini_8_042 = ini_7_041
ini_7_042 = ini_6_041
ini_6_042 = ini_5_041
ini_5_042 = mod(ini_4_041, t__1(42))
ini_4_042 = ini_3_041
ini_3_042 = ini_2_041
ini_2_042 = ini_1_041
ini_1_042 = mod(t__1(42), t__2())


# 0043


def t__1(a):
    t_1 = ini_8_042
    t_2 = sum_1(ini_5_042)
    t_3 = ch(ini_5_042, ini_6_042, ini_7_042)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_042)
    t_2 = maj(ini_1_042, ini_2_042, ini_3_042)
    return mod(t_1, t_2)


ini_8_043 = ini_7_042
ini_7_043 = ini_6_042
ini_6_043 = ini_5_042
ini_5_043 = mod(ini_4_042, t__1(43))
ini_4_043 = ini_3_042
ini_3_043 = ini_2_042
ini_2_043 = ini_1_042
ini_1_043 = mod(t__1(43), t__2())


# 0044


def t__1(a):
    t_1 = ini_8_043
    t_2 = sum_1(ini_5_043)
    t_3 = ch(ini_5_043, ini_6_043, ini_7_043)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_043)
    t_2 = maj(ini_1_043, ini_2_043, ini_3_043)
    return mod(t_1, t_2)


ini_8_044 = ini_7_043
ini_7_044 = ini_6_043
ini_6_044 = ini_5_043
ini_5_044 = mod(ini_4_043, t__1(44))
ini_4_044 = ini_3_043
ini_3_044 = ini_2_043
ini_2_044 = ini_1_043
ini_1_044 = mod(t__1(44), t__2())


# 0045


def t__1(a):
    t_1 = ini_8_044
    t_2 = sum_1(ini_5_044)
    t_3 = ch(ini_5_044, ini_6_044, ini_7_044)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_044)
    t_2 = maj(ini_1_044, ini_2_044, ini_3_044)
    return mod(t_1, t_2)


ini_8_045 = ini_7_044
ini_7_045 = ini_6_044
ini_6_045 = ini_5_044
ini_5_045 = mod(ini_4_044, t__1(45))
ini_4_045 = ini_3_044
ini_3_045 = ini_2_044
ini_2_045 = ini_1_044
ini_1_045 = mod(t__1(45), t__2())


# 0046


def t__1(a):
    t_1 = ini_8_045
    t_2 = sum_1(ini_5_045)
    t_3 = ch(ini_5_045, ini_6_045, ini_7_045)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_045)
    t_2 = maj(ini_1_045, ini_2_045, ini_3_045)
    return mod(t_1, t_2)


ini_8_046 = ini_7_045
ini_7_046 = ini_6_045
ini_6_046 = ini_5_045
ini_5_046 = mod(ini_4_045, t__1(46))
ini_4_046 = ini_3_045
ini_3_046 = ini_2_045
ini_2_046 = ini_1_045
ini_1_046 = mod(t__1(46), t__2())


# 0047


def t__1(a):
    t_1 = ini_8_046
    t_2 = sum_1(ini_5_046)
    t_3 = ch(ini_5_046, ini_6_046, ini_7_046)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_046)
    t_2 = maj(ini_1_046, ini_2_046, ini_3_046)
    return mod(t_1, t_2)


ini_8_047 = ini_7_046
ini_7_047 = ini_6_046
ini_6_047 = ini_5_046
ini_5_047 = mod(ini_4_046, t__1(47))
ini_4_047 = ini_3_046
ini_3_047 = ini_2_046
ini_2_047 = ini_1_046
ini_1_047 = mod(t__1(47), t__2())


# 0048


def t__1(a):
    t_1 = ini_8_047
    t_2 = sum_1(ini_5_047)
    t_3 = ch(ini_5_047, ini_6_047, ini_7_047)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_047)
    t_2 = maj(ini_1_047, ini_2_047, ini_3_047)
    return mod(t_1, t_2)


ini_8_048 = ini_7_047
ini_7_048 = ini_6_047
ini_6_048 = ini_5_047
ini_5_048 = mod(ini_4_047, t__1(48))
ini_4_048 = ini_3_047
ini_3_048 = ini_2_047
ini_2_048 = ini_1_047
ini_1_048 = mod(t__1(48), t__2())


# 0049


def t__1(a):
    t_1 = ini_8_048
    t_2 = sum_1(ini_5_048)
    t_3 = ch(ini_5_048, ini_6_048, ini_7_048)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_048)
    t_2 = maj(ini_1_048, ini_2_048, ini_3_048)
    return mod(t_1, t_2)


ini_8_049 = ini_7_048
ini_7_049 = ini_6_048
ini_6_049 = ini_5_048
ini_5_049 = mod(ini_4_048, t__1(49))
ini_4_049 = ini_3_048
ini_3_049 = ini_2_048
ini_2_049 = ini_1_048
ini_1_049 = mod(t__1(49), t__2())


# 0050


def t__1(a):
    t_1 = ini_8_049
    t_2 = sum_1(ini_5_049)
    t_3 = ch(ini_5_049, ini_6_049, ini_7_049)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_049)
    t_2 = maj(ini_1_049, ini_2_049, ini_3_049)
    return mod(t_1, t_2)


ini_8_050 = ini_7_049
ini_7_050 = ini_6_049
ini_6_050 = ini_5_049
ini_5_050 = mod(ini_4_049, t__1(50))
ini_4_050 = ini_3_049
ini_3_050 = ini_2_049
ini_2_050 = ini_1_049
ini_1_050 = mod(t__1(50), t__2())


# 0051


def t__1(a):
    t_1 = ini_8_050
    t_2 = sum_1(ini_5_050)
    t_3 = ch(ini_5_050, ini_6_050, ini_7_050)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_050)
    t_2 = maj(ini_1_050, ini_2_050, ini_3_050)
    return mod(t_1, t_2)


ini_8_051 = ini_7_050
ini_7_051 = ini_6_050
ini_6_051 = ini_5_050
ini_5_051 = mod(ini_4_050, t__1(51))
ini_4_051 = ini_3_050
ini_3_051 = ini_2_050
ini_2_051 = ini_1_050
ini_1_051 = mod(t__1(51), t__2())


# 0052


def t__1(a):
    t_1 = ini_8_051
    t_2 = sum_1(ini_5_051)
    t_3 = ch(ini_5_051, ini_6_051, ini_7_051)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_051)
    t_2 = maj(ini_1_051, ini_2_051, ini_3_051)
    return mod(t_1, t_2)


ini_8_052 = ini_7_051
ini_7_052 = ini_6_051
ini_6_052 = ini_5_051
ini_5_052 = mod(ini_4_051, t__1(52))
ini_4_052 = ini_3_051
ini_3_052 = ini_2_051
ini_2_052 = ini_1_051
ini_1_052 = mod(t__1(52), t__2())


# 0053


def t__1(a):
    t_1 = ini_8_052
    t_2 = sum_1(ini_5_052)
    t_3 = ch(ini_5_052, ini_6_052, ini_7_052)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_052)
    t_2 = maj(ini_1_052, ini_2_052, ini_3_052)
    return mod(t_1, t_2)


ini_8_053 = ini_7_052
ini_7_053 = ini_6_052
ini_6_053 = ini_5_052
ini_5_053 = mod(ini_4_052, t__1(53))
ini_4_053 = ini_3_052
ini_3_053 = ini_2_052
ini_2_053 = ini_1_052
ini_1_053 = mod(t__1(53), t__2())


# 0054


def t__1(a):
    t_1 = ini_8_053
    t_2 = sum_1(ini_5_053)
    t_3 = ch(ini_5_053, ini_6_053, ini_7_053)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_053)
    t_2 = maj(ini_1_053, ini_2_053, ini_3_053)
    return mod(t_1, t_2)


ini_8_054 = ini_7_053
ini_7_054 = ini_6_053
ini_6_054 = ini_5_053
ini_5_054 = mod(ini_4_053, t__1(54))
ini_4_054 = ini_3_053
ini_3_054 = ini_2_053
ini_2_054 = ini_1_053
ini_1_054 = mod(t__1(54), t__2())


# 0055


def t__1(a):
    t_1 = ini_8_054
    t_2 = sum_1(ini_5_054)
    t_3 = ch(ini_5_054, ini_6_054, ini_7_054)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_054)
    t_2 = maj(ini_1_054, ini_2_054, ini_3_054)
    return mod(t_1, t_2)


ini_8_055 = ini_7_054
ini_7_055 = ini_6_054
ini_6_055 = ini_5_054
ini_5_055 = mod(ini_4_054, t__1(55))
ini_4_055 = ini_3_054
ini_3_055 = ini_2_054
ini_2_055 = ini_1_054
ini_1_055 = mod(t__1(55), t__2())


# 0056


def t__1(a):
    t_1 = ini_8_055
    t_2 = sum_1(ini_5_055)
    t_3 = ch(ini_5_055, ini_6_055, ini_7_055)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_055)
    t_2 = maj(ini_1_055, ini_2_055, ini_3_055)
    return mod(t_1, t_2)


ini_8_056 = ini_7_055
ini_7_056 = ini_6_055
ini_6_056 = ini_5_055
ini_5_056 = mod(ini_4_055, t__1(56))
ini_4_056 = ini_3_055
ini_3_056 = ini_2_055
ini_2_056 = ini_1_055
ini_1_056 = mod(t__1(56), t__2())


# 0057


def t__1(a):
    t_1 = ini_8_056
    t_2 = sum_1(ini_5_056)
    t_3 = ch(ini_5_056, ini_6_056, ini_7_056)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_056)
    t_2 = maj(ini_1_056, ini_2_056, ini_3_056)
    return mod(t_1, t_2)


ini_8_057 = ini_7_056
ini_7_057 = ini_6_056
ini_6_057 = ini_5_056
ini_5_057 = mod(ini_4_056, t__1(57))
ini_4_057 = ini_3_056
ini_3_057 = ini_2_056
ini_2_057 = ini_1_056
ini_1_057 = mod(t__1(57), t__2())


# 0058


def t__1(a):
    t_1 = ini_8_057
    t_2 = sum_1(ini_5_057)
    t_3 = ch(ini_5_057, ini_6_057, ini_7_057)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_057)
    t_2 = maj(ini_1_057, ini_2_057, ini_3_057)
    return mod(t_1, t_2)


ini_8_058 = ini_7_057
ini_7_058 = ini_6_057
ini_6_058 = ini_5_057
ini_5_058 = mod(ini_4_057, t__1(58))
ini_4_058 = ini_3_057
ini_3_058 = ini_2_057
ini_2_058 = ini_1_057
ini_1_058 = mod(t__1(58), t__2())


# 0059


def t__1(a):
    t_1 = ini_8_058
    t_2 = sum_1(ini_5_058)
    t_3 = ch(ini_5_058, ini_6_058, ini_7_058)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_058)
    t_2 = maj(ini_1_058, ini_2_058, ini_3_058)
    return mod(t_1, t_2)


ini_8_059 = ini_7_058
ini_7_059 = ini_6_058
ini_6_059 = ini_5_058
ini_5_059 = mod(ini_4_058, t__1(59))
ini_4_059 = ini_3_058
ini_3_059 = ini_2_058
ini_2_059 = ini_1_058
ini_1_059 = mod(t__1(59), t__2())


# 0060


def t__1(a):
    t_1 = ini_8_059
    t_2 = sum_1(ini_5_059)
    t_3 = ch(ini_5_059, ini_6_059, ini_7_059)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_059)
    t_2 = maj(ini_1_059, ini_2_059, ini_3_059)
    return mod(t_1, t_2)


ini_8_060 = ini_7_059
ini_7_060 = ini_6_059
ini_6_060 = ini_5_059
ini_5_060 = mod(ini_4_059, t__1(60))
ini_4_060 = ini_3_059
ini_3_060 = ini_2_059
ini_2_060 = ini_1_059
ini_1_060 = mod(t__1(60), t__2())


# 0061


def t__1(a):
    t_1 = ini_8_060
    t_2 = sum_1(ini_5_060)
    t_3 = ch(ini_5_060, ini_6_060, ini_7_060)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_060)
    t_2 = maj(ini_1_060, ini_2_060, ini_3_060)
    return mod(t_1, t_2)


ini_8_061 = ini_7_060
ini_7_061 = ini_6_060
ini_6_061 = ini_5_060
ini_5_061 = mod(ini_4_060, t__1(61))
ini_4_061 = ini_3_060
ini_3_061 = ini_2_060
ini_2_061 = ini_1_060
ini_1_061 = mod(t__1(61), t__2())


# 0062


def t__1(a):
    t_1 = ini_8_061
    t_2 = sum_1(ini_5_061)
    t_3 = ch(ini_5_061, ini_6_061, ini_7_061)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_061)
    t_2 = maj(ini_1_061, ini_2_061, ini_3_061)
    return mod(t_1, t_2)


ini_8_062 = ini_7_061
ini_7_062 = ini_6_061
ini_6_062 = ini_5_061
ini_5_062 = mod(ini_4_061, t__1(62))
ini_4_062 = ini_3_061
ini_3_062 = ini_2_061
ini_2_062 = ini_1_061
ini_1_062 = mod(t__1(62), t__2())


# 0063


def t__1(a):
    t_1 = ini_8_062
    t_2 = sum_1(ini_5_062)
    t_3 = ch(ini_5_062, ini_6_062, ini_7_062)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_062)
    t_2 = maj(ini_1_062, ini_2_062, ini_3_062)
    return mod(t_1, t_2)


ini_8_063 = ini_7_062
ini_7_063 = ini_6_062
ini_6_063 = ini_5_062
ini_5_063 = mod(ini_4_062, t__1(63))
ini_4_063 = ini_3_062
ini_3_063 = ini_2_062
ini_2_063 = ini_1_062
ini_1_063 = mod(t__1(63), t__2())


# 0064


def t__1(a):
    t_1 = ini_8_063
    t_2 = sum_1(ini_5_063)
    t_3 = ch(ini_5_063, ini_6_063, ini_7_063)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_063)
    t_2 = maj(ini_1_063, ini_2_063, ini_3_063)
    return mod(t_1, t_2)


ini_8_064 = ini_7_063
ini_7_064 = ini_6_063
ini_6_064 = ini_5_063
ini_5_064 = mod(ini_4_063, t__1(64))
ini_4_064 = ini_3_063
ini_3_064 = ini_2_063
ini_2_064 = ini_1_063
ini_1_064 = mod(t__1(64), t__2())


def w_n(a):
    return str(sha()[32 * (a + 15):32 * (a + 16)])


def seventeen(a):
    return mod(mod(mod(sig_1(w_n(a - 2)), w_n(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


W17 = seventeen(17)
W18 = seventeen(18)


def seventeen_0(a):
    if a <= 16:
        return str(sha()[32 * (a + 15):32 * (a + 16)])
    elif 17 <= a <= 18:
        return seventeen(a)


def seventeen_1(a):
    if a <= 18:
        return seventeen_0(a)
    elif 19 <= a <= 20:
        return mod(mod(mod(sig_1(seventeen_0(a - 2)), w_n(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_2(a):
    if a <= 20:
        return seventeen_1(a)
    elif 21 <= a <= 22:
        return mod(mod(mod(sig_1(seventeen_1(a - 2)), w_n(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_3(a):
    if a <= 22:
        return seventeen_2(a)
    elif a == 23:
        return mod(mod(mod(sig_1(seventeen_2(a - 2)), w_n(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))
    elif a == 24:
        return mod(mod(mod(sig_1(seventeen_2(a - 2)), seventeen_2(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_4(a):
    if a <= 24:
        return seventeen_3(a)
    elif 25 <= a <= 26:
        return mod(mod(mod(sig_1(seventeen_3(a - 2)), seventeen_3(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_5(a):
    if a <= 26:
        return seventeen_4(a)
    elif 27 <= a <= 28:
        return mod(mod(mod(sig_1(seventeen_4(a - 2)), seventeen_4(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_6(a):
    if a <= 28:
        return seventeen_5(a)
    elif 29 <= a <= 30:
        return mod(mod(mod(sig_1(seventeen_5(a - 2)), seventeen_5(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))


def seventeen_7(a):
    if a <= 30:
        return seventeen_6(a)
    elif a == 31:
        return mod(mod(mod(sig_1(seventeen_6(a - 2)), seventeen_6(a - 7)), sig_0(w_n(a - 15))), w_n(a - 16))
    elif a == 32:
        return mod(mod(mod(sig_1(seventeen_6(a - 2)), seventeen_6(a - 7)), sig_0(seventeen_6(a - 15))), w_n(a - 16))


def s_v_8(a):
    s_v_7 = seventeen_7
    if a <= 32:
        return s_v_7(a)
    elif 33 <= a <= 34:
        return mod(mod(mod(sig_1(s_v_7(a - 2)), s_v_7(a - 7)), sig_0(s_v_7(a - 15))), s_v_7(a - 16))


def s_v_9(a):
    if a <= 34:
        return s_v_8(a)
    elif 35 <= a <= 36:
        return mod(mod(mod(sig_1(s_v_8(a - 2)), s_v_8(a - 7)), sig_0(s_v_8(a - 15))), s_v_8(a - 16))


def s_v_10(a):
    if a <= 36:
        return s_v_9(a)
    elif 37 <= a <= 38:
        return mod(mod(mod(sig_1(s_v_9(a - 2)), s_v_9(a - 7)), sig_0(s_v_9(a - 15))), s_v_9(a - 16))


def s_v_11(a):
    if a <= 38:
        return s_v_10(a)
    elif 39 <= a <= 40:
        return mod(mod(mod(sig_1(s_v_10(a - 2)), s_v_10(a - 7)), sig_0(s_v_10(a - 15))), s_v_10(a - 16))


def s_v_12(a):
    if a <= 40:
        return s_v_11(a)
    elif 41 <= a <= 42:
        return mod(mod(mod(sig_1(s_v_11(a - 2)), s_v_11(a - 7)), sig_0(s_v_11(a - 15))), s_v_11(a - 16))


def s_v_13(a):
    if a <= 42:
        return s_v_12(a)
    elif 43 <= a <= 44:
        return mod(mod(mod(sig_1(s_v_12(a - 2)), s_v_12(a - 7)), sig_0(s_v_12(a - 15))), s_v_12(a - 16))


def s_v_14(a):
    if a <= 44:
        return s_v_13(a)
    elif 45 <= a <= 46:
        return mod(mod(mod(sig_1(s_v_13(a - 2)), s_v_13(a - 7)), sig_0(s_v_13(a - 15))), s_v_13(a - 16))


def s_v_15(a):
    if a <= 46:
        return s_v_14(a)
    elif 47 <= a <= 48:
        return mod(mod(mod(sig_1(s_v_14(a - 2)), s_v_14(a - 7)), sig_0(s_v_14(a - 15))), s_v_14(a - 16))


def s_v_16(a):
    if a <= 48:
        return s_v_15(a)
    elif 49 <= a <= 50:
        return mod(mod(mod(sig_1(s_v_15(a - 2)), s_v_15(a - 7)), sig_0(s_v_15(a - 15))), s_v_15(a - 16))


def s_v_17(a):
    if a <= 50:
        return s_v_16(a)
    elif 51 <= a <= 52:
        return mod(mod(mod(sig_1(s_v_16(a - 2)), s_v_16(a - 7)), sig_0(s_v_16(a - 15))), s_v_16(a - 16))


def s_v_18(a):
    if a <= 52:
        return s_v_17(a)
    elif 53 <= a <= 54:
        return mod(mod(mod(sig_1(s_v_17(a - 2)), s_v_17(a - 7)), sig_0(s_v_17(a - 15))), s_v_17(a - 16))


def s_v_19(a):
    if a <= 54:
        return s_v_18(a)
    elif 55 <= a <= 56:
        return mod(mod(mod(sig_1(s_v_18(a - 2)), s_v_18(a - 7)), sig_0(s_v_18(a - 15))), s_v_18(a - 16))


def s_v_20(a):
    if a <= 56:
        return s_v_19(a)
    elif 57 <= a <= 58:
        return mod(mod(mod(sig_1(s_v_19(a - 2)), s_v_19(a - 7)), sig_0(s_v_19(a - 15))), s_v_19(a - 16))


def s_v_21(a):
    if a <= 58:
        return s_v_20(a)
    elif 59 <= a <= 60:
        return mod(mod(mod(sig_1(s_v_20(a - 2)), s_v_20(a - 7)), sig_0(s_v_20(a - 15))), s_v_20(a - 16))


def s_v_22(a):
    if a <= 60:
        return s_v_21(a)
    elif 61 <= a <= 62:
        return mod(mod(mod(sig_1(s_v_21(a - 2)), s_v_21(a - 7)), sig_0(s_v_21(a - 15))), s_v_21(a - 16))


def s_v_23(a):
    if a <= 62:
        return s_v_22(a)
    elif 63 <= a <= 64:
        return mod(mod(mod(sig_1(s_v_22(a - 2)), s_v_22(a - 7)), sig_0(s_v_22(a - 15))), s_v_22(a - 16))


ini_0008 = mod(ini_8_064, initiate_hash_two(8))
ini_0007 = mod(ini_7_064, initiate_hash_two(7))
ini_0006 = mod(ini_6_064, initiate_hash_two(6))
ini_0005 = mod(ini_5_064, initiate_hash_two(5))
ini_0004 = mod(ini_4_064, initiate_hash_two(4))
ini_0003 = mod(ini_3_064, initiate_hash_two(3))
ini_0002 = mod(ini_2_064, initiate_hash_two(2))
ini_0001 = mod(ini_1_064, initiate_hash_two(1))


# 001


def t__1(a):
    t_1 = ini_0008
    t_2 = sum_1(ini_0005)
    t_3 = ch(ini_0005, ini_0006, ini_0007)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_0001)
    t_2 = maj(ini_0001, ini_0002, ini_0003)
    return mod(t_1, t_2)


ini_8 = ini_0007
ini_7 = ini_0006
ini_6 = ini_0005
ini_5 = mod(ini_0004, t__1(1))
ini_4 = ini_0003
ini_3 = ini_0002
ini_2 = ini_0001
ini_1 = mod(t__1(1), t__2())


# 002


def t__1(a):
    t_1 = ini_8
    t_2 = sum_1(ini_5)
    t_3 = ch(ini_5, ini_6, ini_7)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1)
    t_2 = maj(ini_1, ini_2, ini_3)
    return mod(t_1, t_2)


ini_8_02 = ini_7
ini_7_02 = ini_6
ini_6_02 = ini_5
ini_5_02 = mod(ini_4, t__1(2))
ini_4_02 = ini_3
ini_3_02 = ini_2
ini_2_02 = ini_1
ini_1_02 = mod(t__1(2), t__2())


# 003


def t__1(a):
    t_1 = ini_8_02
    t_2 = sum_1(ini_5_02)
    t_3 = ch(ini_5_02, ini_6_02, ini_7_02)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_02)
    t_2 = maj(ini_1_02, ini_2_02, ini_3_02)
    return mod(t_1, t_2)


ini_8_03 = ini_7_02
ini_7_03 = ini_6_02
ini_6_03 = ini_5_02
ini_5_03 = mod(ini_4_02, t__1(3))
ini_4_03 = ini_3_02
ini_3_03 = ini_2_02
ini_2_03 = ini_1_02
ini_1_03 = mod(t__1(3), t__2())


# 004


def t__1(a):
    t_1 = ini_8_03
    t_2 = sum_1(ini_5_03)
    t_3 = ch(ini_5_03, ini_6_03, ini_7_03)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_03)
    t_2 = maj(ini_1_03, ini_2_03, ini_3_03)
    return mod(t_1, t_2)


ini_8_04 = ini_7_03
ini_7_04 = ini_6_03
ini_6_04 = ini_5_03
ini_5_04 = mod(ini_4_03, t__1(4))
ini_4_04 = ini_3_03
ini_3_04 = ini_2_03
ini_2_04 = ini_1_03
ini_1_04 = mod(t__1(4), t__2())


# 005


def t__1(a):
    t_1 = ini_8_04
    t_2 = sum_1(ini_5_04)
    t_3 = ch(ini_5_04, ini_6_04, ini_7_04)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_04)
    t_2 = maj(ini_1_04, ini_2_04, ini_3_04)
    return mod(t_1, t_2)


ini_8_05 = ini_7_04
ini_7_05 = ini_6_04
ini_6_05 = ini_5_04
ini_5_05 = mod(ini_4_04, t__1(5))
ini_4_05 = ini_3_04
ini_3_05 = ini_2_04
ini_2_05 = ini_1_04
ini_1_05 = mod(t__1(5), t__2())


# 006


def t__1(a):
    t_1 = ini_8_05
    t_2 = sum_1(ini_5_05)
    t_3 = ch(ini_5_05, ini_6_05, ini_7_05)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_05)
    t_2 = maj(ini_1_05, ini_2_05, ini_3_05)
    return mod(t_1, t_2)


ini_8_06 = ini_7_05
ini_7_06 = ini_6_05
ini_6_06 = ini_5_05
ini_5_06 = mod(ini_4_05, t__1(6))
ini_4_06 = ini_3_05
ini_3_06 = ini_2_05
ini_2_06 = ini_1_05
ini_1_06 = mod(t__1(6), t__2())


# 007


def t__1(a):
    t_1 = ini_8_06
    t_2 = sum_1(ini_5_06)
    t_3 = ch(ini_5_06, ini_6_06, ini_7_06)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_06)
    t_2 = maj(ini_1_06, ini_2_06, ini_3_06)
    return mod(t_1, t_2)


ini_8_07 = ini_7_06
ini_7_07 = ini_6_06
ini_6_07 = ini_5_06
ini_5_07 = mod(ini_4_06, t__1(7))
ini_4_07 = ini_3_06
ini_3_07 = ini_2_06
ini_2_07 = ini_1_06
ini_1_07 = mod(t__1(7), t__2())


# 008


def t__1(a):
    t_1 = ini_8_07
    t_2 = sum_1(ini_5_07)
    t_3 = ch(ini_5_07, ini_6_07, ini_7_07)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_07)
    t_2 = maj(ini_1_07, ini_2_07, ini_3_07)
    return mod(t_1, t_2)


ini_8_08 = ini_7_07
ini_7_08 = ini_6_07
ini_6_08 = ini_5_07
ini_5_08 = mod(ini_4_07, t__1(8))
ini_4_08 = ini_3_07
ini_3_08 = ini_2_07
ini_2_08 = ini_1_07
ini_1_08 = mod(t__1(8), t__2())


# 009


def t__1(a):
    t_1 = ini_8_08
    t_2 = sum_1(ini_5_08)
    t_3 = ch(ini_5_08, ini_6_08, ini_7_08)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_08)
    t_2 = maj(ini_1_08, ini_2_08, ini_3_08)
    return mod(t_1, t_2)


ini_8_09 = ini_7_08
ini_7_09 = ini_6_08
ini_6_09 = ini_5_08
ini_5_09 = mod(ini_4_08, t__1(9))
ini_4_09 = ini_3_08
ini_3_09 = ini_2_08
ini_2_09 = ini_1_08
ini_1_09 = mod(t__1(9), t__2())


# 0010


def t__1(a):
    t_1 = ini_8_09
    t_2 = sum_1(ini_5_09)
    t_3 = ch(ini_5_09, ini_6_09, ini_7_09)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_09)
    t_2 = maj(ini_1_09, ini_2_09, ini_3_09)
    return mod(t_1, t_2)


ini_8_010 = ini_7_09
ini_7_010 = ini_6_09
ini_6_010 = ini_5_09
ini_5_010 = mod(ini_4_09, t__1(10))
ini_4_010 = ini_3_09
ini_3_010 = ini_2_09
ini_2_010 = ini_1_09
ini_1_010 = mod(t__1(10), t__2())


# 0011


def t__1(a):
    t_1 = ini_8_010
    t_2 = sum_1(ini_5_010)
    t_3 = ch(ini_5_010, ini_6_010, ini_7_010)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_010)
    t_2 = maj(ini_1_010, ini_2_010, ini_3_010)
    return mod(t_1, t_2)


ini_8_011 = ini_7_010
ini_7_011 = ini_6_010
ini_6_011 = ini_5_010
ini_5_011 = mod(ini_4_010, t__1(11))
ini_4_011 = ini_3_010
ini_3_011 = ini_2_010
ini_2_011 = ini_1_010
ini_1_011 = mod(t__1(11), t__2())


# 0012


def t__1(a):
    t_1 = ini_8_011
    t_2 = sum_1(ini_5_011)
    t_3 = ch(ini_5_011, ini_6_011, ini_7_011)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_011)
    t_2 = maj(ini_1_011, ini_2_011, ini_3_011)
    return mod(t_1, t_2)


ini_8_012 = ini_7_011
ini_7_012 = ini_6_011
ini_6_012 = ini_5_011
ini_5_012 = mod(ini_4_011, t__1(12))
ini_4_012 = ini_3_011
ini_3_012 = ini_2_011
ini_2_012 = ini_1_011
ini_1_012 = mod(t__1(12), t__2())


# 0013


def t__1(a):
    t_1 = ini_8_012
    t_2 = sum_1(ini_5_012)
    t_3 = ch(ini_5_012, ini_6_012, ini_7_012)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_012)
    t_2 = maj(ini_1_012, ini_2_012, ini_3_012)
    return mod(t_1, t_2)


ini_8_013 = ini_7_012
ini_7_013 = ini_6_012
ini_6_013 = ini_5_012
ini_5_013 = mod(ini_4_012, t__1(13))
ini_4_013 = ini_3_012
ini_3_013 = ini_2_012
ini_2_013 = ini_1_012
ini_1_013 = mod(t__1(13), t__2())


# 0014


def t__1(a):
    t_1 = ini_8_013
    t_2 = sum_1(ini_5_013)
    t_3 = ch(ini_5_013, ini_6_013, ini_7_013)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_013)
    t_2 = maj(ini_1_013, ini_2_013, ini_3_013)
    return mod(t_1, t_2)


ini_8_014 = ini_7_013
ini_7_014 = ini_6_013
ini_6_014 = ini_5_013
ini_5_014 = mod(ini_4_013, t__1(14))
ini_4_014 = ini_3_013
ini_3_014 = ini_2_013
ini_2_014 = ini_1_013
ini_1_014 = mod(t__1(14), t__2())


# 0015


def t__1(a):
    t_1 = ini_8_014
    t_2 = sum_1(ini_5_014)
    t_3 = ch(ini_5_014, ini_6_014, ini_7_014)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_014)
    t_2 = maj(ini_1_014, ini_2_014, ini_3_014)
    return mod(t_1, t_2)


ini_8_015 = ini_7_014
ini_7_015 = ini_6_014
ini_6_015 = ini_5_014
ini_5_015 = mod(ini_4_014, t__1(15))
ini_4_015 = ini_3_014
ini_3_015 = ini_2_014
ini_2_015 = ini_1_014
ini_1_015 = mod(t__1(15), t__2())


# 0016


def t__1(a):
    t_1 = ini_8_015
    t_2 = sum_1(ini_5_015)
    t_3 = ch(ini_5_015, ini_6_015, ini_7_015)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_015)
    t_2 = maj(ini_1_015, ini_2_015, ini_3_015)
    return mod(t_1, t_2)


ini_8_016 = ini_7_015
ini_7_016 = ini_6_015
ini_6_016 = ini_5_015
ini_5_016 = mod(ini_4_015, t__1(16))
ini_4_016 = ini_3_015
ini_3_016 = ini_2_015
ini_2_016 = ini_1_015
ini_1_016 = mod(t__1(16), t__2())


# 0017


def t__1(a):
    t_1 = ini_8_016
    t_2 = sum_1(ini_5_016)
    t_3 = ch(ini_5_016, ini_6_016, ini_7_016)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_016)
    t_2 = maj(ini_1_016, ini_2_016, ini_3_016)
    return mod(t_1, t_2)


ini_8_017 = ini_7_016
ini_7_017 = ini_6_016
ini_6_017 = ini_5_016
ini_5_017 = mod(ini_4_016, t__1(17))
ini_4_017 = ini_3_016
ini_3_017 = ini_2_016
ini_2_017 = ini_1_016
ini_1_017 = mod(t__1(17), t__2())


# 0018


def t__1(a):
    t_1 = ini_8_017
    t_2 = sum_1(ini_5_017)
    t_3 = ch(ini_5_017, ini_6_017, ini_7_017)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_017)
    t_2 = maj(ini_1_017, ini_2_017, ini_3_017)
    return mod(t_1, t_2)


ini_8_018 = ini_7_017
ini_7_018 = ini_6_017
ini_6_018 = ini_5_017
ini_5_018 = mod(ini_4_017, t__1(18))
ini_4_018 = ini_3_017
ini_3_018 = ini_2_017
ini_2_018 = ini_1_017
ini_1_018 = mod(t__1(18), t__2())


# 0019


def t__1(a):
    t_1 = ini_8_018
    t_2 = sum_1(ini_5_018)
    t_3 = ch(ini_5_018, ini_6_018, ini_7_018)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_018)
    t_2 = maj(ini_1_018, ini_2_018, ini_3_018)
    return mod(t_1, t_2)


ini_8_019 = ini_7_018
ini_7_019 = ini_6_018
ini_6_019 = ini_5_018
ini_5_019 = mod(ini_4_018, t__1(19))
ini_4_019 = ini_3_018
ini_3_019 = ini_2_018
ini_2_019 = ini_1_018
ini_1_019 = mod(t__1(19), t__2())


# 0020


def t__1(a):
    t_1 = ini_8_019
    t_2 = sum_1(ini_5_019)
    t_3 = ch(ini_5_019, ini_6_019, ini_7_019)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_019)
    t_2 = maj(ini_1_019, ini_2_019, ini_3_019)
    return mod(t_1, t_2)


ini_8_020 = ini_7_019
ini_7_020 = ini_6_019
ini_6_020 = ini_5_019
ini_5_020 = mod(ini_4_019, t__1(20))
ini_4_020 = ini_3_019
ini_3_020 = ini_2_019
ini_2_020 = ini_1_019
ini_1_020 = mod(t__1(20), t__2())


# 0021


def t__1(a):
    t_1 = ini_8_020
    t_2 = sum_1(ini_5_020)
    t_3 = ch(ini_5_020, ini_6_020, ini_7_020)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_020)
    t_2 = maj(ini_1_020, ini_2_020, ini_3_020)
    return mod(t_1, t_2)


ini_8_021 = ini_7_020
ini_7_021 = ini_6_020
ini_6_021 = ini_5_020
ini_5_021 = mod(ini_4_020, t__1(21))
ini_4_021 = ini_3_020
ini_3_021 = ini_2_020
ini_2_021 = ini_1_020
ini_1_021 = mod(t__1(21), t__2())


# 0022


def t__1(a):
    t_1 = ini_8_021
    t_2 = sum_1(ini_5_021)
    t_3 = ch(ini_5_021, ini_6_021, ini_7_021)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_021)
    t_2 = maj(ini_1_021, ini_2_021, ini_3_021)
    return mod(t_1, t_2)


ini_8_022 = ini_7_021
ini_7_022 = ini_6_021
ini_6_022 = ini_5_021
ini_5_022 = mod(ini_4_021, t__1(22))
ini_4_022 = ini_3_021
ini_3_022 = ini_2_021
ini_2_022 = ini_1_021
ini_1_022 = mod(t__1(22), t__2())


# 0023


def t__1(a):
    t_1 = ini_8_022
    t_2 = sum_1(ini_5_022)
    t_3 = ch(ini_5_022, ini_6_022, ini_7_022)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_022)
    t_2 = maj(ini_1_022, ini_2_022, ini_3_022)
    return mod(t_1, t_2)


ini_8_023 = ini_7_022
ini_7_023 = ini_6_022
ini_6_023 = ini_5_022
ini_5_023 = mod(ini_4_022, t__1(23))
ini_4_023 = ini_3_022
ini_3_023 = ini_2_022
ini_2_023 = ini_1_022
ini_1_023 = mod(t__1(23), t__2())


# 0024


def t__1(a):
    t_1 = ini_8_023
    t_2 = sum_1(ini_5_023)
    t_3 = ch(ini_5_023, ini_6_023, ini_7_023)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_023)
    t_2 = maj(ini_1_023, ini_2_023, ini_3_023)
    return mod(t_1, t_2)


ini_8_024 = ini_7_023
ini_7_024 = ini_6_023
ini_6_024 = ini_5_023
ini_5_024 = mod(ini_4_023, t__1(24))
ini_4_024 = ini_3_023
ini_3_024 = ini_2_023
ini_2_024 = ini_1_023
ini_1_024 = mod(t__1(24), t__2())


# 0025


def t__1(a):
    t_1 = ini_8_024
    t_2 = sum_1(ini_5_024)
    t_3 = ch(ini_5_024, ini_6_024, ini_7_024)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_024)
    t_2 = maj(ini_1_024, ini_2_024, ini_3_024)
    return mod(t_1, t_2)


ini_8_025 = ini_7_024
ini_7_025 = ini_6_024
ini_6_025 = ini_5_024
ini_5_025 = mod(ini_4_024, t__1(25))
ini_4_025 = ini_3_024
ini_3_025 = ini_2_024
ini_2_025 = ini_1_024
ini_1_025 = mod(t__1(25), t__2())


# 0026


def t__1(a):
    t_1 = ini_8_025
    t_2 = sum_1(ini_5_025)
    t_3 = ch(ini_5_025, ini_6_025, ini_7_025)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_025)
    t_2 = maj(ini_1_025, ini_2_025, ini_3_025)
    return mod(t_1, t_2)


ini_8_026 = ini_7_025
ini_7_026 = ini_6_025
ini_6_026 = ini_5_025
ini_5_026 = mod(ini_4_025, t__1(26))
ini_4_026 = ini_3_025
ini_3_026 = ini_2_025
ini_2_026 = ini_1_025
ini_1_026 = mod(t__1(26), t__2())


# 0027


def t__1(a):
    t_1 = ini_8_026
    t_2 = sum_1(ini_5_026)
    t_3 = ch(ini_5_026, ini_6_026, ini_7_026)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_026)
    t_2 = maj(ini_1_026, ini_2_026, ini_3_026)
    return mod(t_1, t_2)


ini_8_027 = ini_7_026
ini_7_027 = ini_6_026
ini_6_027 = ini_5_026
ini_5_027 = mod(ini_4_026, t__1(27))
ini_4_027 = ini_3_026
ini_3_027 = ini_2_026
ini_2_027 = ini_1_026
ini_1_027 = mod(t__1(27), t__2())


# 0028


def t__1(a):
    t_1 = ini_8_027
    t_2 = sum_1(ini_5_027)
    t_3 = ch(ini_5_027, ini_6_027, ini_7_027)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_027)
    t_2 = maj(ini_1_027, ini_2_027, ini_3_027)
    return mod(t_1, t_2)


ini_8_028 = ini_7_027
ini_7_028 = ini_6_027
ini_6_028 = ini_5_027
ini_5_028 = mod(ini_4_027, t__1(28))
ini_4_028 = ini_3_027
ini_3_028 = ini_2_027
ini_2_028 = ini_1_027
ini_1_028 = mod(t__1(28), t__2())


# 0029


def t__1(a):
    t_1 = ini_8_028
    t_2 = sum_1(ini_5_028)
    t_3 = ch(ini_5_028, ini_6_028, ini_7_028)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_028)
    t_2 = maj(ini_1_028, ini_2_028, ini_3_028)
    return mod(t_1, t_2)


ini_8_029 = ini_7_028
ini_7_029 = ini_6_028
ini_6_029 = ini_5_028
ini_5_029 = mod(ini_4_028, t__1(29))
ini_4_029 = ini_3_028
ini_3_029 = ini_2_028
ini_2_029 = ini_1_028
ini_1_029 = mod(t__1(29), t__2())


# 0030


def t__1(a):
    t_1 = ini_8_029
    t_2 = sum_1(ini_5_029)
    t_3 = ch(ini_5_029, ini_6_029, ini_7_029)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_029)
    t_2 = maj(ini_1_029, ini_2_029, ini_3_029)
    return mod(t_1, t_2)


ini_8_030 = ini_7_029
ini_7_030 = ini_6_029
ini_6_030 = ini_5_029
ini_5_030 = mod(ini_4_029, t__1(30))
ini_4_030 = ini_3_029
ini_3_030 = ini_2_029
ini_2_030 = ini_1_029
ini_1_030 = mod(t__1(30), t__2())


# 0031


def t__1(a):
    t_1 = ini_8_030
    t_2 = sum_1(ini_5_030)
    t_3 = ch(ini_5_030, ini_6_030, ini_7_030)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_030)
    t_2 = maj(ini_1_030, ini_2_030, ini_3_030)
    return mod(t_1, t_2)


ini_8_031 = ini_7_030
ini_7_031 = ini_6_030
ini_6_031 = ini_5_030
ini_5_031 = mod(ini_4_030, t__1(31))
ini_4_031 = ini_3_030
ini_3_031 = ini_2_030
ini_2_031 = ini_1_030
ini_1_031 = mod(t__1(31), t__2())


# 0032


def t__1(a):
    t_1 = ini_8_031
    t_2 = sum_1(ini_5_031)
    t_3 = ch(ini_5_031, ini_6_031, ini_7_031)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_031)
    t_2 = maj(ini_1_031, ini_2_031, ini_3_031)
    return mod(t_1, t_2)


ini_8_032 = ini_7_031
ini_7_032 = ini_6_031
ini_6_032 = ini_5_031
ini_5_032 = mod(ini_4_031, t__1(32))
ini_4_032 = ini_3_031
ini_3_032 = ini_2_031
ini_2_032 = ini_1_031
ini_1_032 = mod(t__1(32), t__2())


# 0033


def t__1(a):
    t_1 = ini_8_032
    t_2 = sum_1(ini_5_032)
    t_3 = ch(ini_5_032, ini_6_032, ini_7_032)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_032)
    t_2 = maj(ini_1_032, ini_2_032, ini_3_032)
    return mod(t_1, t_2)


ini_8_033 = ini_7_032
ini_7_033 = ini_6_032
ini_6_033 = ini_5_032
ini_5_033 = mod(ini_4_032, t__1(33))
ini_4_033 = ini_3_032
ini_3_033 = ini_2_032
ini_2_033 = ini_1_032
ini_1_033 = mod(t__1(33), t__2())


# 0034


def t__1(a):
    t_1 = ini_8_033
    t_2 = sum_1(ini_5_033)
    t_3 = ch(ini_5_033, ini_6_033, ini_7_033)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_033)
    t_2 = maj(ini_1_033, ini_2_033, ini_3_033)
    return mod(t_1, t_2)


ini_8_034 = ini_7_033
ini_7_034 = ini_6_033
ini_6_034 = ini_5_033
ini_5_034 = mod(ini_4_033, t__1(34))
ini_4_034 = ini_3_033
ini_3_034 = ini_2_033
ini_2_034 = ini_1_033
ini_1_034 = mod(t__1(34), t__2())


# 0035


def t__1(a):
    t_1 = ini_8_034
    t_2 = sum_1(ini_5_034)
    t_3 = ch(ini_5_034, ini_6_034, ini_7_034)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_034)
    t_2 = maj(ini_1_034, ini_2_034, ini_3_034)
    return mod(t_1, t_2)


ini_8_035 = ini_7_034
ini_7_035 = ini_6_034
ini_6_035 = ini_5_034
ini_5_035 = mod(ini_4_034, t__1(35))
ini_4_035 = ini_3_034
ini_3_035 = ini_2_034
ini_2_035 = ini_1_034
ini_1_035 = mod(t__1(35), t__2())


# 0036


def t__1(a):
    t_1 = ini_8_035
    t_2 = sum_1(ini_5_035)
    t_3 = ch(ini_5_035, ini_6_035, ini_7_035)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_035)
    t_2 = maj(ini_1_035, ini_2_035, ini_3_035)
    return mod(t_1, t_2)


ini_8_036 = ini_7_035
ini_7_036 = ini_6_035
ini_6_036 = ini_5_035
ini_5_036 = mod(ini_4_035, t__1(36))
ini_4_036 = ini_3_035
ini_3_036 = ini_2_035
ini_2_036 = ini_1_035
ini_1_036 = mod(t__1(36), t__2())


# 0037


def t__1(a):
    t_1 = ini_8_036
    t_2 = sum_1(ini_5_036)
    t_3 = ch(ini_5_036, ini_6_036, ini_7_036)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_036)
    t_2 = maj(ini_1_036, ini_2_036, ini_3_036)
    return mod(t_1, t_2)


ini_8_037 = ini_7_036
ini_7_037 = ini_6_036
ini_6_037 = ini_5_036
ini_5_037 = mod(ini_4_036, t__1(37))
ini_4_037 = ini_3_036
ini_3_037 = ini_2_036
ini_2_037 = ini_1_036
ini_1_037 = mod(t__1(37), t__2())


# 0038


def t__1(a):
    t_1 = ini_8_037
    t_2 = sum_1(ini_5_037)
    t_3 = ch(ini_5_037, ini_6_037, ini_7_037)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_037)
    t_2 = maj(ini_1_037, ini_2_037, ini_3_037)
    return mod(t_1, t_2)


ini_8_038 = ini_7_037
ini_7_038 = ini_6_037
ini_6_038 = ini_5_037
ini_5_038 = mod(ini_4_037, t__1(38))
ini_4_038 = ini_3_037
ini_3_038 = ini_2_037
ini_2_038 = ini_1_037
ini_1_038 = mod(t__1(38), t__2())


# 0039


def t__1(a):
    t_1 = ini_8_038
    t_2 = sum_1(ini_5_038)
    t_3 = ch(ini_5_038, ini_6_038, ini_7_038)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_038)
    t_2 = maj(ini_1_038, ini_2_038, ini_3_038)
    return mod(t_1, t_2)


ini_8_039 = ini_7_038
ini_7_039 = ini_6_038
ini_6_039 = ini_5_038
ini_5_039 = mod(ini_4_038, t__1(39))
ini_4_039 = ini_3_038
ini_3_039 = ini_2_038
ini_2_039 = ini_1_038
ini_1_039 = mod(t__1(39), t__2())


# 0040


def t__1(a):
    t_1 = ini_8_039
    t_2 = sum_1(ini_5_039)
    t_3 = ch(ini_5_039, ini_6_039, ini_7_039)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_039)
    t_2 = maj(ini_1_039, ini_2_039, ini_3_039)
    return mod(t_1, t_2)


ini_8_040 = ini_7_039
ini_7_040 = ini_6_039
ini_6_040 = ini_5_039
ini_5_040 = mod(ini_4_039, t__1(40))
ini_4_040 = ini_3_039
ini_3_040 = ini_2_039
ini_2_040 = ini_1_039
ini_1_040 = mod(t__1(40), t__2())


# 0041


def t__1(a):
    t_1 = ini_8_040
    t_2 = sum_1(ini_5_040)
    t_3 = ch(ini_5_040, ini_6_040, ini_7_040)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_040)
    t_2 = maj(ini_1_040, ini_2_040, ini_3_040)
    return mod(t_1, t_2)


ini_8_041 = ini_7_040
ini_7_041 = ini_6_040
ini_6_041 = ini_5_040
ini_5_041 = mod(ini_4_040, t__1(41))
ini_4_041 = ini_3_040
ini_3_041 = ini_2_040
ini_2_041 = ini_1_040
ini_1_041 = mod(t__1(41), t__2())


# 0042


def t__1(a):
    t_1 = ini_8_041
    t_2 = sum_1(ini_5_041)
    t_3 = ch(ini_5_041, ini_6_041, ini_7_041)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_041)
    t_2 = maj(ini_1_041, ini_2_041, ini_3_041)
    return mod(t_1, t_2)


ini_8_042 = ini_7_041
ini_7_042 = ini_6_041
ini_6_042 = ini_5_041
ini_5_042 = mod(ini_4_041, t__1(42))
ini_4_042 = ini_3_041
ini_3_042 = ini_2_041
ini_2_042 = ini_1_041
ini_1_042 = mod(t__1(42), t__2())


# 0043


def t__1(a):
    t_1 = ini_8_042
    t_2 = sum_1(ini_5_042)
    t_3 = ch(ini_5_042, ini_6_042, ini_7_042)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_042)
    t_2 = maj(ini_1_042, ini_2_042, ini_3_042)
    return mod(t_1, t_2)


ini_8_043 = ini_7_042
ini_7_043 = ini_6_042
ini_6_043 = ini_5_042
ini_5_043 = mod(ini_4_042, t__1(43))
ini_4_043 = ini_3_042
ini_3_043 = ini_2_042
ini_2_043 = ini_1_042
ini_1_043 = mod(t__1(43), t__2())


# 0044


def t__1(a):
    t_1 = ini_8_043
    t_2 = sum_1(ini_5_043)
    t_3 = ch(ini_5_043, ini_6_043, ini_7_043)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_043)
    t_2 = maj(ini_1_043, ini_2_043, ini_3_043)
    return mod(t_1, t_2)


ini_8_044 = ini_7_043
ini_7_044 = ini_6_043
ini_6_044 = ini_5_043
ini_5_044 = mod(ini_4_043, t__1(44))
ini_4_044 = ini_3_043
ini_3_044 = ini_2_043
ini_2_044 = ini_1_043
ini_1_044 = mod(t__1(44), t__2())


# 0045


def t__1(a):
    t_1 = ini_8_044
    t_2 = sum_1(ini_5_044)
    t_3 = ch(ini_5_044, ini_6_044, ini_7_044)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_044)
    t_2 = maj(ini_1_044, ini_2_044, ini_3_044)
    return mod(t_1, t_2)


ini_8_045 = ini_7_044
ini_7_045 = ini_6_044
ini_6_045 = ini_5_044
ini_5_045 = mod(ini_4_044, t__1(45))
ini_4_045 = ini_3_044
ini_3_045 = ini_2_044
ini_2_045 = ini_1_044
ini_1_045 = mod(t__1(45), t__2())


# 0046


def t__1(a):
    t_1 = ini_8_045
    t_2 = sum_1(ini_5_045)
    t_3 = ch(ini_5_045, ini_6_045, ini_7_045)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_045)
    t_2 = maj(ini_1_045, ini_2_045, ini_3_045)
    return mod(t_1, t_2)


ini_8_046 = ini_7_045
ini_7_046 = ini_6_045
ini_6_046 = ini_5_045
ini_5_046 = mod(ini_4_045, t__1(46))
ini_4_046 = ini_3_045
ini_3_046 = ini_2_045
ini_2_046 = ini_1_045
ini_1_046 = mod(t__1(46), t__2())


# 0047


def t__1(a):
    t_1 = ini_8_046
    t_2 = sum_1(ini_5_046)
    t_3 = ch(ini_5_046, ini_6_046, ini_7_046)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_046)
    t_2 = maj(ini_1_046, ini_2_046, ini_3_046)
    return mod(t_1, t_2)


ini_8_047 = ini_7_046
ini_7_047 = ini_6_046
ini_6_047 = ini_5_046
ini_5_047 = mod(ini_4_046, t__1(47))
ini_4_047 = ini_3_046
ini_3_047 = ini_2_046
ini_2_047 = ini_1_046
ini_1_047 = mod(t__1(47), t__2())


# 0048


def t__1(a):
    t_1 = ini_8_047
    t_2 = sum_1(ini_5_047)
    t_3 = ch(ini_5_047, ini_6_047, ini_7_047)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_047)
    t_2 = maj(ini_1_047, ini_2_047, ini_3_047)
    return mod(t_1, t_2)


ini_8_048 = ini_7_047
ini_7_048 = ini_6_047
ini_6_048 = ini_5_047
ini_5_048 = mod(ini_4_047, t__1(48))
ini_4_048 = ini_3_047
ini_3_048 = ini_2_047
ini_2_048 = ini_1_047
ini_1_048 = mod(t__1(48), t__2())


# 0049


def t__1(a):
    t_1 = ini_8_048
    t_2 = sum_1(ini_5_048)
    t_3 = ch(ini_5_048, ini_6_048, ini_7_048)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_048)
    t_2 = maj(ini_1_048, ini_2_048, ini_3_048)
    return mod(t_1, t_2)


ini_8_049 = ini_7_048
ini_7_049 = ini_6_048
ini_6_049 = ini_5_048
ini_5_049 = mod(ini_4_048, t__1(49))
ini_4_049 = ini_3_048
ini_3_049 = ini_2_048
ini_2_049 = ini_1_048
ini_1_049 = mod(t__1(49), t__2())


# 0050


def t__1(a):
    t_1 = ini_8_049
    t_2 = sum_1(ini_5_049)
    t_3 = ch(ini_5_049, ini_6_049, ini_7_049)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_049)
    t_2 = maj(ini_1_049, ini_2_049, ini_3_049)
    return mod(t_1, t_2)


ini_8_050 = ini_7_049
ini_7_050 = ini_6_049
ini_6_050 = ini_5_049
ini_5_050 = mod(ini_4_049, t__1(50))
ini_4_050 = ini_3_049
ini_3_050 = ini_2_049
ini_2_050 = ini_1_049
ini_1_050 = mod(t__1(50), t__2())


# 0051


def t__1(a):
    t_1 = ini_8_050
    t_2 = sum_1(ini_5_050)
    t_3 = ch(ini_5_050, ini_6_050, ini_7_050)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_050)
    t_2 = maj(ini_1_050, ini_2_050, ini_3_050)
    return mod(t_1, t_2)


ini_8_051 = ini_7_050
ini_7_051 = ini_6_050
ini_6_051 = ini_5_050
ini_5_051 = mod(ini_4_050, t__1(51))
ini_4_051 = ini_3_050
ini_3_051 = ini_2_050
ini_2_051 = ini_1_050
ini_1_051 = mod(t__1(51), t__2())


# 0052


def t__1(a):
    t_1 = ini_8_051
    t_2 = sum_1(ini_5_051)
    t_3 = ch(ini_5_051, ini_6_051, ini_7_051)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_051)
    t_2 = maj(ini_1_051, ini_2_051, ini_3_051)
    return mod(t_1, t_2)


ini_8_052 = ini_7_051
ini_7_052 = ini_6_051
ini_6_052 = ini_5_051
ini_5_052 = mod(ini_4_051, t__1(52))
ini_4_052 = ini_3_051
ini_3_052 = ini_2_051
ini_2_052 = ini_1_051
ini_1_052 = mod(t__1(52), t__2())


# 0053


def t__1(a):
    t_1 = ini_8_052
    t_2 = sum_1(ini_5_052)
    t_3 = ch(ini_5_052, ini_6_052, ini_7_052)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_052)
    t_2 = maj(ini_1_052, ini_2_052, ini_3_052)
    return mod(t_1, t_2)


ini_8_053 = ini_7_052
ini_7_053 = ini_6_052
ini_6_053 = ini_5_052
ini_5_053 = mod(ini_4_052, t__1(53))
ini_4_053 = ini_3_052
ini_3_053 = ini_2_052
ini_2_053 = ini_1_052
ini_1_053 = mod(t__1(53), t__2())


# 0054


def t__1(a):
    t_1 = ini_8_053
    t_2 = sum_1(ini_5_053)
    t_3 = ch(ini_5_053, ini_6_053, ini_7_053)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_053)
    t_2 = maj(ini_1_053, ini_2_053, ini_3_053)
    return mod(t_1, t_2)


ini_8_054 = ini_7_053
ini_7_054 = ini_6_053
ini_6_054 = ini_5_053
ini_5_054 = mod(ini_4_053, t__1(54))
ini_4_054 = ini_3_053
ini_3_054 = ini_2_053
ini_2_054 = ini_1_053
ini_1_054 = mod(t__1(54), t__2())


# 0055


def t__1(a):
    t_1 = ini_8_054
    t_2 = sum_1(ini_5_054)
    t_3 = ch(ini_5_054, ini_6_054, ini_7_054)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_054)
    t_2 = maj(ini_1_054, ini_2_054, ini_3_054)
    return mod(t_1, t_2)


ini_8_055 = ini_7_054
ini_7_055 = ini_6_054
ini_6_055 = ini_5_054
ini_5_055 = mod(ini_4_054, t__1(55))
ini_4_055 = ini_3_054
ini_3_055 = ini_2_054
ini_2_055 = ini_1_054
ini_1_055 = mod(t__1(55), t__2())


# 0056


def t__1(a):
    t_1 = ini_8_055
    t_2 = sum_1(ini_5_055)
    t_3 = ch(ini_5_055, ini_6_055, ini_7_055)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_055)
    t_2 = maj(ini_1_055, ini_2_055, ini_3_055)
    return mod(t_1, t_2)


ini_8_056 = ini_7_055
ini_7_056 = ini_6_055
ini_6_056 = ini_5_055
ini_5_056 = mod(ini_4_055, t__1(56))
ini_4_056 = ini_3_055
ini_3_056 = ini_2_055
ini_2_056 = ini_1_055
ini_1_056 = mod(t__1(56), t__2())


# 0057


def t__1(a):
    t_1 = ini_8_056
    t_2 = sum_1(ini_5_056)
    t_3 = ch(ini_5_056, ini_6_056, ini_7_056)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_056)
    t_2 = maj(ini_1_056, ini_2_056, ini_3_056)
    return mod(t_1, t_2)


ini_8_057 = ini_7_056
ini_7_057 = ini_6_056
ini_6_057 = ini_5_056
ini_5_057 = mod(ini_4_056, t__1(57))
ini_4_057 = ini_3_056
ini_3_057 = ini_2_056
ini_2_057 = ini_1_056
ini_1_057 = mod(t__1(57), t__2())


# 0058


def t__1(a):
    t_1 = ini_8_057
    t_2 = sum_1(ini_5_057)
    t_3 = ch(ini_5_057, ini_6_057, ini_7_057)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_057)
    t_2 = maj(ini_1_057, ini_2_057, ini_3_057)
    return mod(t_1, t_2)


ini_8_058 = ini_7_057
ini_7_058 = ini_6_057
ini_6_058 = ini_5_057
ini_5_058 = mod(ini_4_057, t__1(58))
ini_4_058 = ini_3_057
ini_3_058 = ini_2_057
ini_2_058 = ini_1_057
ini_1_058 = mod(t__1(58), t__2())


# 0059


def t__1(a):
    t_1 = ini_8_058
    t_2 = sum_1(ini_5_058)
    t_3 = ch(ini_5_058, ini_6_058, ini_7_058)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_058)
    t_2 = maj(ini_1_058, ini_2_058, ini_3_058)
    return mod(t_1, t_2)


ini_8_059 = ini_7_058
ini_7_059 = ini_6_058
ini_6_059 = ini_5_058
ini_5_059 = mod(ini_4_058, t__1(59))
ini_4_059 = ini_3_058
ini_3_059 = ini_2_058
ini_2_059 = ini_1_058
ini_1_059 = mod(t__1(59), t__2())


# 0060


def t__1(a):
    t_1 = ini_8_059
    t_2 = sum_1(ini_5_059)
    t_3 = ch(ini_5_059, ini_6_059, ini_7_059)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_059)
    t_2 = maj(ini_1_059, ini_2_059, ini_3_059)
    return mod(t_1, t_2)


ini_8_060 = ini_7_059
ini_7_060 = ini_6_059
ini_6_060 = ini_5_059
ini_5_060 = mod(ini_4_059, t__1(60))
ini_4_060 = ini_3_059
ini_3_060 = ini_2_059
ini_2_060 = ini_1_059
ini_1_060 = mod(t__1(60), t__2())


# 0061


def t__1(a):
    t_1 = ini_8_060
    t_2 = sum_1(ini_5_060)
    t_3 = ch(ini_5_060, ini_6_060, ini_7_060)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_060)
    t_2 = maj(ini_1_060, ini_2_060, ini_3_060)
    return mod(t_1, t_2)


ini_8_061 = ini_7_060
ini_7_061 = ini_6_060
ini_6_061 = ini_5_060
ini_5_061 = mod(ini_4_060, t__1(61))
ini_4_061 = ini_3_060
ini_3_061 = ini_2_060
ini_2_061 = ini_1_060
ini_1_061 = mod(t__1(61), t__2())


# 0062


def t__1(a):
    t_1 = ini_8_061
    t_2 = sum_1(ini_5_061)
    t_3 = ch(ini_5_061, ini_6_061, ini_7_061)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_061)
    t_2 = maj(ini_1_061, ini_2_061, ini_3_061)
    return mod(t_1, t_2)


ini_8_062 = ini_7_061
ini_7_062 = ini_6_061
ini_6_062 = ini_5_061
ini_5_062 = mod(ini_4_061, t__1(62))
ini_4_062 = ini_3_061
ini_3_062 = ini_2_061
ini_2_062 = ini_1_061
ini_1_062 = mod(t__1(62), t__2())


# 0063


def t__1(a):
    t_1 = ini_8_062
    t_2 = sum_1(ini_5_062)
    t_3 = ch(ini_5_062, ini_6_062, ini_7_062)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_062)
    t_2 = maj(ini_1_062, ini_2_062, ini_3_062)
    return mod(t_1, t_2)


ini_8_063 = ini_7_062
ini_7_063 = ini_6_062
ini_6_063 = ini_5_062
ini_5_063 = mod(ini_4_062, t__1(63))
ini_4_063 = ini_3_062
ini_3_063 = ini_2_062
ini_2_063 = ini_1_062
ini_1_063 = mod(t__1(63), t__2())


# 0064


def t__1(a):
    t_1 = ini_8_063
    t_2 = sum_1(ini_5_063)
    t_3 = ch(ini_5_063, ini_6_063, ini_7_063)
    return mod(mod(mod(mod(t_1, t_2), t_3), initiate_hash_three(a)), s_v_23(a))


def t__2():
    t_1 = sum_0(ini_1_063)
    t_2 = maj(ini_1_063, ini_2_063, ini_3_063)
    return mod(t_1, t_2)


ini_8_064 = ini_7_063
ini_7_064 = ini_6_063
ini_6_064 = ini_5_063
ini_5_064 = mod(ini_4_063, t__1(64))
ini_4_064 = ini_3_063
ini_3_064 = ini_2_063
ini_2_064 = ini_1_063
ini_1_064 = mod(t__1(64), t__2())


ale_8 = str(mod(ini_8_064, ini_0008))
ale_7 = str(mod(ini_7_064, ini_0007))
ale_6 = str(mod(ini_6_064, ini_0006))
ale_5 = str(mod(ini_5_064, ini_0005))
ale_4 = str(mod(ini_4_064, ini_0004))
ale_3 = str(mod(ini_3_064, ini_0003))
ale_2 = str(mod(ini_2_064, ini_0002))
ale_1 = str(mod(ini_1_064, ini_0001))


ale_8_1 = hex(int(ale_8, 2))[2:]
ale_7_1 = hex(int(ale_7, 2))[2:]
ale_6_1 = hex(int(ale_6, 2))[2:]
ale_5_1 = hex(int(ale_5, 2))[2:]
ale_4_1 = hex(int(ale_4, 2))[2:]
ale_3_1 = hex(int(ale_3, 2))[2:]
ale_2_1 = hex(int(ale_2, 2))[2:]
ale_1_1 = hex(int(ale_1, 2))[2:]

print(str(ale_1_1)+str(ale_2_1)+str(ale_3_1)+str(ale_4_1)+str(ale_5_1)+str(ale_6_1)+str(ale_7_1)+str(ale_8_1))
