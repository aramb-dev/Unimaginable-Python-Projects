def raise_to_power_of_a_number(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power_of_a_number(2, 3))
