def longest_common_substring(str1, str2):
    matrix = []
    for i in range(len(str1)):
        matrix.append([0] * len(str2))
    max_value = 0
    max_value_row = 0
    max_value_col = 0
    for row in range(len(str1)):
        for col in range(len(str2)):
            if str1[row] == str[col]:
                up_left = 0
                if row > 0 and col > 0:
                    up_left = matrix[row - 1][col - 1]
                matrix[row][col] = 1 + up_left
                if matrix[row][col] > max_value:
                    max_value = matrix[row][col]
                    max_value_row = row
                    max_value_col = col
            else:
                matrix[row][col] = 0
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_row + 1]

def longest_common_substring_optimized(str1, str2):
    matrix_row = [0] * len(str2)
    max_value = 0
    max_value_row = 0
    for row in range(len(str1)):
        up_left = 0
        for col in range(len(str2)):
            saved_current = matrix_row[col]
            if str1[row] == str[col]:
                matrix_row[col] = 1 + up_left
                if matrix_row[col] > max_value:
                    max_value = matrix_row[col]
                    max_value_row = row
            else:
                matrix_row[col] = 0
            up_left = saved_current
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_row + 1]