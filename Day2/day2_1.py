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
  checksum += max(el) - min(el)    # add the difference of the largest and smallest
                                   # values to the checksum for each line

print(checksum)                    # print the solution and be done :)

