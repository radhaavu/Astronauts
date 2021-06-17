'''
Class Astronaut
---------------
+name
+year
+group
+status
+birthdate
+birthplace
+gender
+Alma mater
+undergraduate degree
+graduate degree
+military branch
+space flight numbers
+flight hours
+number of space walks
+space walk hours
+missions
+death date
+death missions
'''
import csv
import json


def upload(decorated_fn):
    def inner_fn(*args,**kwargs):
        with open('astronauts.json', "w") as outfile: 
            json.dump(decorated_fn(*args,**kwargs), outfile)
        outfile.close()
    return inner_fn
class Astronaut:
    def __init__(self,astro_list):
        self._name=astro_list[0]
        self._flighthr=astro_list[14]
        self._status=astro_list[3]
        self._year=astro_list[2]
        self._birthPlace=astro_list[5]
        self._gender=astro_list[6]
        self._undAlm=astro_list[7]
        self._undMaj=astro_list[9]
        self._gradAlm=astro_list[8]
        self._gradMaj=astro_list[10]
    def __str__(self):
        return (self._name+", "+self._status)
    def __gt__(self,other):
        print('__gt__ called -self: %s, other: %s'%(self,other))
        return self._flighthr>other._flighthr
        
    def __ge__(self,other):
        print('__ge__ called -self: %s, other: %s'%(self,other))
        return self._flighthr>=other._flighthr
    def __eq__(self,other):
        print('__eq__ called -self: %s, other: %s'%(self,other))
        if self._flighthr==other._flighthr:
            return True
        else:
            return False
    @upload
    def getAll(self):
        ast_dict={'Name':self._name,'Year':self._year,'Status':self._status,'Birth Place':self._birthPlace,'Gender':self._gender,'Alma Mater-Undergraduate':self._undAlm,
        'Undergraduate Major':self._undMaj,'Alma Mater-Graduate':self._gradAlm,'Graduate Major':self._gradMaj}
        return ast_dict

astronaut_data=[]
with open("astronauts.csv","r") as f:
    csv_reader=csv.reader(f,delimiter=",")
    astro=list(csv_reader)

for a in astro[1:]:
    astronaut_data.append(Astronaut(a))

a1=astronaut_data[4]
a1.getAll()


class Mission:
    def __init__(self,astro_list):
        #search to see which astronauts are in the group
        #set year to one of the astronauts in the group
        self._list_b=astro_list
        self.position=0

    def __iter__(self):
            return self._list_b[self.position]
    def __next_(self):
        if self.position==len(self._list_b):
            raise StopIteration
        self.position+=1
        return self._list_b[self.position]
'''
def mission(astro_list):
    max_it=len(astro_list)
    for i in range(max_it-1,-1,-1):
        yield astro_list[i]
'''
m=Mission(astronaut_data[4:7])
for i in m:
    print(i)


