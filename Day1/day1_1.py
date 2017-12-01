f = open("./day1.txt", "r") # Open the puzzle file
puzzle = list(f.read())     # Convert the puzzle number into a list of numbers
puzzle.pop()                # removes the newline character at the end
puzzle.append(puzzle[0])    # adds the first element in the list to the end,
                            #  because the list is circular according to the rules
                            #  of the puzzle
puzzle = [ int(el) for el in puzzle]  # convert all the string elements into ints

matches = []                          # declare an empty array for the matching numbers

for i, el in enumerate(puzzle):       # loop through each element in puzzle
  if(i+1 == len(puzzle)):             # check that the next index does not exceed the length of puzzle
    break                             # if it does, break the loop
  else:                               # otherwise
    if puzzle[i] == puzzle[i+1]:      # if the next digit matches the previous
      matches.append(puzzle[i])       # add it to the matches array

print(sum(matches))                   # print the sum of the matches array and be done :)