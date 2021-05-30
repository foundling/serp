# work done in session w/ brad over replit.com multiuser session

fpath = "constitution_files/article1.txt"
file_handle = open(fpath, "r")
file_lines = file_handle.readlines()
count = dict()

for each_line in file_lines:
  words = each_line.split()
  for each_word in words:
    # text processing goes here 
    count[each_word] = count.get(each_word, 0) + 1
print(count)
