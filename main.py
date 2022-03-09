N = int(input())
nList = list(map(int, input().split()))
nList.sort()
M = int(input())
MList = list(map(int, input().split()))


def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) //2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid+1, end)
    
for check in MList:
  result = binary_search(nList, check, 0, N-1)
  if(result == None):
    print("no", end=' ')
  else:
    print("yes", end=' ')
  
  
