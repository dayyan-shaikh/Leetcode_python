paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

strt_city=[]
end_city=[]

for i in paths:
    strt_city.append(i[0])
    end_city.append(i[1])

strt_set=set(strt_city)
end_set=set(end_city)

final=end_set.difference(strt_city)

final_1=list(final)

print(final_1[0])