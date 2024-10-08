# 4. Feistel cipher with three iterations, where the keys are [45, 108, 192]
# Iteration function is (m|k)^((m//16)&k)
# Decipher cipher made using CRT mode:
# [[151, 14], [147, 0], [144, 1], [134, 17], [132, 6], [136, 15], [151, 16], [150, 17], [132, 27], [134, 4], [149, 12], [145, 2], [149, 8], [143, 10], [143, 10], [144, 21], [137, 27], [131, 4], [152, 27], [135, 8], [128, 5], [159, 28], [155, 25], [147, 31], [131, 17], [158, 4], [149, 19], [158, 4], [133, 3], [133, 3], [151, 31], [155, 19], [148, 23], [136, 18], [150, 16], [136, 2], [136, 17], [155, 20], [149, 10], [144, 9], [149, 8], [143, 10], [143, 2], [150, 25], [146, 8], [151, 4], [145, 0], [138, 2], [133, 17], [158, 4], [130, 23], [145, 27], [133, 25], [130, 27], [155, 30], [129, 6], [128, 17], [155, 25], [158, 1], [134, 1], [132, 2], [137, 27], [134, 2], [147, 1], [145, 87], [156, 78], [147, 83], [136, 75], [140, 68], [144, 85], [149, 78], [148, 82], [138, 73], [140, 80], [136, 77], [134, 74], [149, 87], [140, 64], [131, 82], [149, 82]]

import utils.feistel_scheme as fs

keys = [45, 108, 192]
byte_pairs = [[151, 14], [147, 0], [144, 1], [134, 17], [132, 6], [136, 15], [151, 16], [150, 17], [132, 27], [134, 4], [149, 12], [145, 2], [149, 8], [143, 10], [143, 10], [144, 21], [137, 27], [131, 4], [152, 27], [135, 8], [128, 5], [159, 28], [155, 25], [147, 31], [131, 17], [158, 4], [149, 19], [158, 4], [133, 3], [133, 3], [151, 31], [155, 19], [148, 23], [136, 18], [150, 16], [136, 2], [136, 17], [155, 20], [149, 10], [144, 9], [149, 8], [143, 10], [143, 2], [150, 25], [146, 8], [151, 4], [145, 0], [138, 2], [133, 17], [158, 4], [130, 23], [145, 27], [133, 25], [130, 27], [155, 30], [129, 6], [128, 17], [155, 25], [158, 1], [134, 1], [132, 2], [137, 27], [134, 2], [147, 1], [145, 87], [156, 78], [147, 83], [136, 75], [140, 68], [144, 85], [149, 78], [148, 82], [138, 73], [140, 80], [136, 77], [134, 74], [149, 87], [140, 64], [131, 82], [149, 82]]
byte_pair_num = len(byte_pairs)
func = "(r | key) ^ ((r//16) & key)"

result_str = ""
for idx in range(0, byte_pair_num):
    pair = byte_pairs[idx]

    r = idx
    key = keys[0]
    counter = [eval(func), eval(func)]

    l_result, r_result = fs.decrypt_crt(pair, counter, func, keys)
    result_str += chr(l_result) + chr(r_result)

print(result_str)