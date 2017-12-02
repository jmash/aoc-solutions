f = open('./day2.txt', 'r')        # open the file with the values for the puzzle

vals = f.read().split('\n')        # set a variable called vals to read in and split
                                   #   the input by the newline characters
puzzle = []                        # initialize the puzzle array

for el in vals:                    # for every element in the vals array,
  puzzle.append(el.split('\t'))    # split it by the tab character and append it to
                                   #   the puzzle array

puzzle.pop()                       # remove the last element (it's empty)

checksum = 0                       # initialize the checksum

for el in puzzle:                  # for every element in the puzzle array,
  el = [ int(x) for x in el ]      # turn every element into an integer
  for x in el:                     # for every element in the line,
    for y in el:                   # check that element against every other element
      if (x != y and x % y == 0):  # x % y would give a false positive
        checksum += x / y          # add the divisible values to the checksum on each pass

print(checksum)                    # print the checksum and be done :)
