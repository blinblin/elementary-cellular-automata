import sys

def init_list(x):
  """Returns a list that represents the first row of the image. x is the number of 0's before the 1"""
  list = []
  for i in xrange(2*x):
    list.append(0)
  list.insert(x,1)
  return list

def conv_bin(x):
  """Takes an int and converts it into a binary number and places each bit into a list"""
  out = []
  for i in xrange(7,-1,-1):
      out.append((x & 2**i) >> i)
  return out

def conv_deci(x):
  """Takes a list that represents a binary number and converts it into an int"""
  sum = 0
  for i in xrange(3):
    sum += x[i]*(2**(2-i))
  return sum

def update(x,rule):
  """Applies a rule to an input and returns 1 or 0"""
  return rule[7-conv_deci(x)]

def update_list(list,rule):
  """Takes a list as a row and applies a rule to that row and returns a new row"""
  newlist = []
  length = len(list)
  newlist.append(update([0,list[0],list[1]],rule))
  for i in range(1,length-1):
    newlist.append(update(list[i-1:i+2],rule))
  if len(sys.argv) == 4:
    if sys.argv[3] == 'Wolfram':
      newlist.append(update([list[length-2],list[length-1],list[length-1]],rule))
  else:
    newlist.append(update([list[length-2],list[length-1],0],rule))
  return newlist

def print_list(list):
  """Prints out a list"""
  out = ''
  for x in list:
    out = out + str(x)
  print out

def main():
  rule = conv_bin(int(sys.argv[1]))
  num_steps = int(sys.argv[2])
  list = init_list(num_steps)
  print 'P1 '+str(num_steps*2+1)+' '+str(num_steps+1)
  print_list(list)
  for x in range(num_steps):
    list = update_list(list,rule)
    print_list(list)

if len(sys.argv) == 2 or len(sys.argv) == 1:
  print "Incorrect number of inputs." 
  print "Inputs are Rule Number, Number of rows, and an optional 'Wolfram'"
  print "Wolfram parameter will determine if grid is infinite or finite"
  print "Add 'Wolfram' for an infinite grid"
elif len(sys.argv) == 3:
  main()
elif len(sys.argv) == 4 and sys.argv[3] == 'Wolfram':
  main()
elif len(sys.argv) == 4:
  print "Third input has to be 'Wolfram' or nothing"
else:
  print "Too many inputs"