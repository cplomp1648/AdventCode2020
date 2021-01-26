

f = open("inputs\\Day_2_input.txt", "r")
old_invalid_pw = 0
invalid_pw = 0
# for line in f:
#     # Input format: #-# C: abcd
#     test = line
#     line = line.split(":")
#     password = line[1].strip()
#     line = line[0].split()
#     req_char = line[1]
#     line = line[0].split("-")
#     min_occ = line[0]
#     max_occ = line[1]
#     a = password.count(req_char)
#     if int(min_occ) <= password.count(req_char) <= int(max_occ):
#         pass
#     else:
#         old_invalid_pw += 1
for line in f:
    # Input format: #-# C: abcd
    test = line
    line = line.split(":")
    password = line[1].strip()
    line = line[0].split()
    req_char = line[1]
    line = line[0].split("-")
    pos_1 = line[0]
    pos_2 = line[1]
    if (password[int(pos_1)-1] == req_char) ^ (password[int(pos_2)-1] == req_char):
        pass
    else:
        invalid_pw += 1
print(1000-invalid_pw)
