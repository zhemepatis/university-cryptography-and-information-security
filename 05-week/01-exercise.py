# 1. Decipher Feistel cipher (ECB) with three iterations when key is [55, 101, 183]
# Iteration function: (m^k)&((k//16)|m)
# Cipher: [[75, 77], [92, 87], [81, 69], [93, 83], [79, 70], [69, 83], [66, 81], [92, 85], [65, 95], [86, 83], [94, 67], [92, 87], [91, 85], [73, 71], [73, 74], [67, 91], [91, 85], [88, 80], [79, 70], [75, 71], [71, 79], [66, 81], [92, 85], [83, 65], [92, 87], [75, 77], [75, 71], [83, 85], [75, 77], [78, 73], [75, 71], [89, 68], [77, 79], [71, 85], [73, 74], [69, 88], [77, 66], [85, 67], [67, 79], [69, 94], [65, 95], [67, 77], [71, 69], [82, 85], [75, 75], [67, 82], [83, 74], [75, 79], [82, 64], [79, 67], [91, 85], [68, 77], [75, 71], [83, 68], [82, 81], [83, 64], [67, 46]]

import utils.feistel_scheme as fs

keys = [55, 101, 183]
byte_pairs = [[75, 77], [92, 87], [81, 69], [93, 83], [79, 70], [69, 83], [66, 81], [92, 85], [65, 95], [86, 83], [94, 67], [92, 87], [91, 85], [73, 71], [73, 74], [67, 91], [91, 85], [88, 80], [79, 70], [75, 71], [71, 79], [66, 81], [92, 85], [83, 65], [92, 87], [75, 77], [75, 71], [83, 85], [75, 77], [78, 73], [75, 71], [89, 68], [77, 79], [71, 85], [73, 74], [69, 88], [77, 66], [85, 67], [67, 79], [69, 94], [65, 95], [67, 77], [71, 69], [82, 85], [75, 75], [67, 82], [83, 74], [75, 79], [82, 64], [79, 67], [91, 85], [68, 77], [75, 71], [83, 68], [82, 81], [83, 64], [67, 46]]
func = "(r ^ key) & ((key // 16) | r)"

result_str = ""
for pair in byte_pairs:
    l_result, r_result = fs.decrypt_ebc(pair, func, keys)
    result_str += chr(l_result) + chr(r_result)

print(result_str)
   