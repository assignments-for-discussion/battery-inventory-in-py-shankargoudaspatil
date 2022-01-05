def test_bucketing_by_number_of_cycles(cycles):
  print("Counting batteries by usage cycles...\n");
  lowCount = 0
  highCount = 0
  mediumCount = 0
  for i in cycles:
      if i < 400:
        lowCount += 1
      elif i > 920:
        highCount += 1
      else:
        mediumCount += 1
  "return lowCount, highCount, mediumCount"
  print(lowCount, highCount, mediumCount)

cycles = [100, 200, 300, 550, 520, 600, 800, 1000,1120]
if _name_ == '_main_':
  test_bucketing_by_number_of_cycles(cycles)
  
