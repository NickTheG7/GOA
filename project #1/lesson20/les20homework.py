#1
def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))
#2
def make_upper_case(s):
    return s.upper()
#3
def invert(lst):
    return [n * -1 for n in lst] if len(lst) > 0 else []
#4
def make_upper_case(s):
    return s.upper()
#5
def areYouPlayingBanjo(name):
  first = name[0];
  if first == "r" or first == "R":
    return name + " plays banjo";
  else:
    return name + " does not play banjo";
#6
def find_average(array):
    return sum(array) // len(array)
#?
