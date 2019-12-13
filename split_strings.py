def solution(s):
  result = []
  a = [letter for letter in str(s)]
  if len(a)%2 == 1:
    a.append('_')
  [result.append(a[i] + a[i+1]) for i in range(0,len(a),2)]
  return result
