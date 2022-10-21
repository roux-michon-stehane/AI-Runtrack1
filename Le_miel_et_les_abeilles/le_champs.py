import random ,csv

class bee :

    def __init__(self, name):
        self.name = name
        self.distance = self.the_Darwinian_score()
        self.score = self.the_score(self.distance)
             
    def the_Darwinian_score(self):
        
        flower_list=[]
        f =open("Champd_de_pissenlits_et_de_sauge_des_pres___Feuille_1.csv","r")
        flower = csv.reader(f)
        
        for ligne in flower:
            if ligne == ["x","y"]:
                continue
            else :
                flower_list.append([0,0])
                flower_list[-1][0] = int(ligne[0])
                flower_list[-1][-1] = int(ligne[1])
                
        
        journey_of_the_bee = random.sample(flower_list,50)
        return journey_of_the_bee
    
    def the_score(self,flower_list):

        general_distance = []
        total_Distance = []
        for a in range(49):
            for i in range (1):
                b= a + 1
                distance = flower_list[a][i] - flower_list[b][i]
                print(distance)
                distance_2 = distance * distance
            general_distance.append(distance_2)
        total = sum(total_Distance)
        return total 
    
    def check_score(self):
        return self.score
            
    def crossing(self, bee_generator,bees) :
        bees.score.sort()
        for q in range (99):
            d= q +1
            if bees.score[q] >= bees.score[d] :
                bees.distance[d] = bees.distance[q]
            else :
                bees.distance[q] = bees.distance[d]
        
    def score_hive (self):
        total_hive = []
        for index in bee:
            total_hive.append(bee.score)
            score_hive = sum(total_hive)
            return score_hive

hive = []
for index in range (100):
    bees = bee(index)
    hive.append(bees)
# print(hive.score_hive())
