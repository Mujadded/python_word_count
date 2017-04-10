def count_words(s,n):
  temp=s.split()
  t_n={}
  for word in temp:
    if word not in t_n:
      t_n[word]=1
    else:
      t_n[word]+=1
    top_n=[]
  
  for key, value in sorted(t_n.iteritems(), key=lambda (k,v): (-v,k)):
    top_n.append((key,value))
  # print top_n
  # top_n=list(reversed(top_n))
  return top_n[:n]
  
  
def test_run():
  print count_words("cat bat mat cat bat cat",3)
  print count_words("betty bought a bit of butter but the butter was bitter",3)
  
test_run()
