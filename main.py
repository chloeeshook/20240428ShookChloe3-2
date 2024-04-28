#Function: This program determines if a student will be admitted or rejected.
#Input:  Interactive
testScoreString = int(input("Enter a test score: "))
classRankString = int(input("Enter a class rank: "))
#Output: Accept or Reject

# Get input and convert to correct data type for testScore and classRank

# Test using admission requirements and print Accept or Reject
if testScoreString >= 90:
  if classRankString >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScoreString >= 80:
    if classRankString >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScoreString >= 70:
      if classRankString >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")