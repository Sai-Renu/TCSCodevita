def min_num(arr,max_weight):
  arr.sort(reverse=True)
  
  vehicles_needed=0
  i=0
  while i <len(arr):
    current_weight=arr[i]
    vehicles_needed+=1
    while i<len(arr) and current_weight+ arr[i]<=max_weight:
      current_weight+=arr[i]
      i+=1
  return vehicles_needed

arr=list(map(int,input().split()))
max_weight=int(input())

print(min_num(arr,max_weight))
