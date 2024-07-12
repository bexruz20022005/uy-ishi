def ikki_had_mus_man(numbers):
    for i in range(len(numbers) - 1):
        if (numbers[i] > 0 and numbers[i + 1] > 0) or (numbers[i] < 0 and numbers[i + 1] < 0):
            print(numbers[i], numbers[i + 1])
numbers = [int(x) for x in input("Iltimos, sonlarni vergul bilan ajrating: ").split(",")]
ikki_had_mus_man(numbers)
