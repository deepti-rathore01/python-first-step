def count_line(fname):
     num_lines = 0
     with open(fname, 'r') as f:
        for line in f:
         num_lines += 1
     return num_lines

