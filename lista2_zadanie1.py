#wbudowana funkcja
wynik1=sum(1/(n**2) for n in range(1, 10**6+1))
print(wynik1)

#sumowanie od najmniejszej do największej
wynik2=0
for n in range(1, 10**6+1):
    wynik2+=1/(n**2)
print(wynik2)
#sumowanie od największej do najmniejszej
wynik3=0
for n in range(10**6, 0, -1):
    wynik3+=1/(n**2)
print(wynik3)

#kopiec z heapq
import heapq
kopiec=[1/(n**2) for n in range(1, 10**6+1)]
heapq.heapify(kopiec)
while len(kopiec)>1:
  a=heapq.heappop(kopiec)
  b=heapq.heappop(kopiec)
  heapq.heappush(kopiec, a+b)

wynik4=kopiec[0]
print(wynik4)

#bez heapq
#lista=[1/(n**2) for n in range(1, 10**6+1)]
#lista.sort()
#while len(lista)>1:
#    a=lista.pop(0)
#    b=lista.pop(0)
#    lista.append(a+b)
#
#wynik5=lista[0]
#print(wynik5)

