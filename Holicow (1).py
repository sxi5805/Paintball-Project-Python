__author__ = 'swetha kannan'

from math import sqrt
from Graph import Graph
from vertex import Vertex

class Holicow:
 __slots__ ='cownames','paintball','graph'

 def __init__(self, filename):
     self.cownames={}
     self.paintball={}
     self.graph = Graph()
     #self.vertex=Vertex()
     with open(filename) as f:
            for line in f:
                if len(line) > 0 and line[0] != '#':
                    fields = line.split()
                    if fields[0]=='cow':
                      id = (fields[1])
                      self.cownames[fields[1]]=[fields[2],fields[3]]

                    else:
                        id = (fields[1])
                        self.paintball[fields[1]]=[fields[2],fields[3],fields[4]]

            for name in self.paintball:

                 list=self.paintball[name]


                 x1=list[0]
                 y1=list[1]
                 radius=list[2]

                 for key in self.cownames:

                     cowlist=self.cownames[key]

                     x2=cowlist[0]
                     y2=cowlist[1]

                     if int(radius)>= sqrt(abs(pow(abs(int(x1)-int(x2)),2)+(pow(abs(int(y1)-int(y2)),2)))):

                          self.graph.addEdge(name,key)

            for name in self.paintball:
                 list=self.paintball[name]
                 x1=list[0]
                 y1=list[1]
                 radius=list[2]
                 for key in self.paintball:
                     if name!=key:
                         list1=self.paintball[key]
                         x2=list1[0]
                         y2=list1[1]
                         if int(radius)>= sqrt(abs(pow(abs(int(x1)-int(x2)),2)+(pow(abs(int(y1)-int(y2)),2)))):
                             self.graph.addEdge(name,key)

     for key in self.graph:
         print(key)

     self.simulation()
     self.results()

 def results(self):
     max=0
     dictionary={'Milka':[],'Daisy':[],'Babe':[],'Fauntleroy':[]}
     #colourlist=[]

     optimalball=self.graph
     for key in self.graph:
         if key.counter>max:
             max=key.counter
             optimalball=key
     print('Triggering',optimalball.keyfinder(), 'paint ball is the best choice with 4 total paint on the cows:')
     redlist=optimalball.connections()
     for element in redlist:
         if element in self.cownames:

             #dictionary[element]=[optimalball.keyfinder]
             print(type(dictionary[element]), 'dict ele')
             print(optimalball.keyfinder(),'optimalkeyfinder')
             dictionary[element].append(optimalball.keyfinder())
             print(dictionary,'dictionary in results')
         else:
             self.another(element,dictionary)

     for k, v in dictionary.items():

        print(k,'s colors: {', v,'}')



 def another(self,element,dictionary):
     for key in self.graph:
         if(key.id==element):
             anotherlist=key.connections()
     for a in anotherlist:
         if a in self.cownames:
                print(type(a),'a')
                print(type(dictionary[a]),'type')
                dictionary[a].append(element)
                print(dictionary,'dictionary in another ')

         else:
             self.another(a,dictionary)


 def simulation(self):
    dict1={}

    for key in self.graph:

        if (key.keyfinder()) in self.paintball:
            print('Triggering',key.keyfinder(),'paint ball. . .')
            #print(key.connections())
            connlist=key.connections()

            for x in range(len(connlist)):
                storelist=[]
                if connlist[x] in self.cownames:

                    print('      ',connlist[x],'is painted',key.keyfinder(),'!')
                    key.counter=key.counter+1
                    #print(key.counter,'counter in simulation')


                    '''storelist.append(key.keyfinder())
                    dict1[connlist[x]]=storelist
                    print(dict1,'dict1')
                    #print(storelist,'store')'''

                    '''key.storelist.append(key.keyfinder())
                    dict1[connlist[x]]=key.storelist
                    print(dict1,'  dict1')
                    print(key.storelist,'  store list')'''
                    #  print(type(dict1[connlist[x]]),'typeeeeeeeeee')
                    #dict1[connlist[x]].append(key.keyfinder())
                    #print(dict1,'  dict1')

                else:
                    print('      ',connlist[x],'paint ball is triggered by',key.keyfinder(),'paint ball')

                    self.test(connlist[x],dict1,key)

 def test(self,value,dict1,key):
    for x in self.graph:


        if (x.id==value):

            newlist=x.connections()

            for i in range(len(newlist)):
                if newlist[i] in self.cownames:
                    print('      ',newlist[i],'is painted',x.keyfinder(),'!')
                    key.counter=key.counter+1
                    #print(key.counter,'counter in test')


                    '''storelist.append(x.keyfinder())
                    dict1[newlist[i]]=storelist
                    print(dict1,'dict1')
                    print(storelist,'store')'''

                    '''storelist.append(x.keyfinder())
                    dict1[newlist[i]]=storelist
                    print(dict1,'  dict1')
                    print(storelist,'  store list') '''

                    #dict1[newlist[i]].append(x.keyfinder())
                    #print(dict1,'  dict1')



                else:
                    print('      ',newlist[i],'paint ball is triggered by',x.keyfinder(),'paint ball')
                    self.test(newlist[i],dict1,key)
                    #print(connlist[x],'type',type(connlist[x]))
                    









 #def __str__(self):


def main():
    """
    The main function prompts for the file name and enters the
    main loop.
    :return: None
    """
    try:
        holicow = Holicow(input('Enter filename: '))

        #subway.mainLoop()
    except IOError as err:  # if error with file name
        print(err)

if __name__ == '__main__':
    main()