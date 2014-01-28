def LSubSum(AR):

  ''' This is a O(n) Implementation of 
      the Algorithm
  '''
  if max(AR) > 0:
    return min(AR)
  else:
    maxpast = 0 
    maxpresent= 0 
    for x in AR:
      maxpast = max(0 , maxpast + x)
      maxpresent = max(maxpast , maxpresent)
    return maxpresent 
  
if __name__ == '__main__':
  AR = []
  LSubSum(AR)
