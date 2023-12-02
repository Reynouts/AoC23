# third try part 1 with chatGPT/3.5 (just replying: "does not work" or "that is not correct"
def calculate_calibration_sum(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            digits = [char for char in line if char.isdigit()]
            if digits:
                calibration_value = int(digits[0] + digits[-1])
                total_sum += calibration_value
    return total_sum

file_path = "day1.txt"
result = calculate_calibration_sum(file_path)
print(result)

# cannot solve part 2 without help. Tried different approaches (without getting into solutions)
# did not work. Nice.
import re

def calculate_calibration_sum(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            words = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d+)', line)
            for word in words:
                if word.isdigit():
                    calibration_value = int(word)
                    total_sum += calibration_value
                else:
                    for char in word:
                        calibration_value = ord(char) - ord('a') + 1
                        total_sum += calibration_value

    return total_sum

file_path = "day1.txt"
result = calculate_calibration_sum(file_path)
print(result)


