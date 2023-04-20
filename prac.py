# def solution(k, tangerine): 
  # k = 귤의 개수, tangerine = 귤의 크기를 담은 배열
    # k=6, tangerine=[1,3,2,5,4,5,2,3]
    # k가 주어졌을 때, 크기가 서로 다른 종류 수의 최솟값을 반환해야한다. 
    # 크기 종류 수의 최솟값을 반환하려면 종류의 최댓값을 구해서 정렬한 뒤 k개수 만큼 카운트하고 반환하면 될듯?
tangerine=[1,3,2,5,4,5,2,3]
num_list = {}
k = 6 
for num in tangerine: # num = 1 
    if num not in num_list: 
        num_list[num] = 1
    else:
        num_list[num] += 1

    
sorted_num_list = sorted(num_list.items(), key=lambda x: x[1], reverse=True)
print(sorted_num_list)


count = 0
result = 0
for i in sorted_num_list:    
  print(i[1])
  count += i[1]
  result += 1
  if count >= k:
    break
print(result)