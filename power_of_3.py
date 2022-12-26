def power_of_3(num):
    if num == 1:
        return True

    return num % 3 == 0 and power_of_3(num / 3)

print(power_of_3(-9))