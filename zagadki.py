import networkx as nx
from random import choice,sample
import matplotlib.pyplot as plt

class animals_semantic_network: #sieć semantyczna zwierząt
    network=nx.DiGraph()
    #możliwe hasła
    answers=["kot","pies","chomik","pająk","ryba","wielbłąd","lew","zebra","owca","krowa","ptak","żółw","ćma","koń","mysz","wąż","pszczoła","mucha"]

    def __init__(self):
        #dodajemy węzły/hasła do sieci
        self.network.add_nodes_from(self.answers)
        
        #budujemy  sieć semantyczną
        #Kot
        self.add_node(self.answers[0],"wąsy","ma")
        self.add_node(self.answers[0],"mruczy","Co robi?")
        self.add_node(self.answers[0],"na myszy","poluje")
        self.add_node(self.answers[0],"futro","ma")
        self.add_node(self.answers[0],"mleko","pije")
        self.add_node(self.answers[0],"miauczy","Co robi?")

        #Pies
        self.add_node(self.answers[1],"4 łapy","ma")
        self.add_node(self.answers[1],"szczeka","Co robi?")
        self.add_node(self.answers[1],"aportuje","Co robi?")
        self.add_node(self.answers[1],"najlepszym przyjacielem człowieka","jest")
        self.add_node(self.answers[1],"kości","je")
        self.add_node(self.answers[1],"w budzie","mieszka")

        #Chomik
        self.add_node(self.answers[2],"krótko","żyje")
        self.add_node(self.answers[2],"futro","ma")
        self.add_node(self.answers[2],"gryzoniem","jest")
        self.add_node(self.answers[2],"ziarenka","je")
        self.add_node(self.answers[2],"biega w kołowrotku","Co robi?")
        self.add_node(self.answers[2],"znany z robienia zapasów","jest")

        #Pająk
        self.add_node(self.answers[3],"8 odnóży","ma")
        self.add_node(self.answers[3],"sieci","wije")
        self.add_node(self.answers[3],"wiele oczu","ma")
        self.add_node(self.answers[3],"muchy","je")
        self.add_node(self.answers[3],"odwłok","ma")
        self.add_node(self.answers[3],"postrachem arachnofobów","jest")

        #Ryba
        self.add_node(self.answers[4],"pływa","Co robi?")
        self.add_node(self.answers[4],"skrzela","ma")
        self.add_node(self.answers[4],"płetwy","ma")
        self.add_node(self.answers[4],"łuski","ma")
        self.add_node(self.answers[4],"głosu","nie ma")
        self.add_node(self.answers[4],"w ławicach","żyje")
        
        #Wielbłąd
        self.add_node(self.answers[5],"garba","ma")
        self.add_node(self.answers[5],"na pustyni","żyje")
        self.add_node(self.answers[5],"kopyta","ma")
        self.add_node(self.answers[5],"toboły","nosi")
        self.add_node(self.answers[5],"długo bez wody","wytrzymuje")
        self.add_node(self.answers[5],"nim dromader","jest")

        #Lew
        self.add_node(self.answers[6],"ryczy","Co robi?")
        self.add_node(self.answers[6],"grzywę","ma")
        self.add_node(self.answers[6],"na sawannie","żyje")
        self.add_node(self.answers[6],"mięsożerny","jest")
        self.add_node(self.answers[6],"królem zwierząt","jest")
        self.add_node(self.answers[6],"znakiem zodiaku","jest")

        #Zebra
        self.add_node(self.answers[7],"paski","ma")
        self.add_node(self.answers[7],"kopyta","ma")
        self.add_node(self.answers[7],"czarno-biała","jest")
        self.add_node(self.answers[7],"na sawannie","żyje")
        self.add_node(self.answers[7],"na ulicy","jest")

        #Owca
        self.add_node(self.answers[8],"wełnę","daje")
        self.add_node(self.answers[8],"żeńską formą barana","jest")
        self.add_node(self.answers[8],"trawę","je")
        self.add_node(self.answers[8],"przed snem","liczy się ją")
        self.add_node(self.answers[8],"niedopasowanie","czarna oznacza")
        self.add_node(self.answers[8],"beczy","Co robi?")

        #Krowa
        self.add_node(self.answers[9],"łatki","ma")
        self.add_node(self.answers[9],"mleko","daje")
        self.add_node(self.answers[9],"muczy","Co robi?")
        self.add_node(self.answers[9],"trawę","je")
        self.add_node(self.answers[9],"żeńską formą byka","jest")
        self.add_node(self.answers[9],"cukierki","zdrobnienie jej nazwy oznacza")

        #Ptak
        self.add_node(self.answers[10],"skrzydła","ma")
        self.add_node(self.answers[10],"dziób","ma")
        self.add_node(self.answers[10],"upierzony","jest")
        self.add_node(self.answers[10],"przedmiotem zainteresowania ornitologów","jest")
        self.add_node(self.answers[10],"nim np. orzeł","jest")
        self.add_node(self.answers[10],"nielotem","czasem jest")

        #Żółw
        self.add_node(self.answers[11],"wolny","jest")
        self.add_node(self.answers[11],"skorupę","ma")
        self.add_node(self.answers[11],"długo","żyje")
        self.add_node(self.answers[11],"gadem","jest")
        self.add_node(self.answers[11],"popularny na Galapagos","jest")
        self.add_node(self.answers[11],"morski lub lądowy","jest")
        #Ćma
        self.add_node(self.answers[12],"stworzeniem nocnym","jest")
        self.add_node(self.answers[12],"szara","jest")
        self.add_node(self.answers[12],"owadem","jest")
        self.add_node(self.answers[12],"do światła","leci")
        self.add_node(self.answers[12],"podobna do motyla","jest")

        #Koń
        self.add_node(self.answers[13],"jaki jest","każdy widzi")
        self.add_node(self.answers[13],"kopyta","ma")
        self.add_node(self.answers[13],"galopuje","Co robi?")
        self.add_node(self.answers[13],"w stajni","żyje")
        self.add_node(self.answers[13],"owies","je")
        self.add_node(self.answers[13],"jednostką mocy","mechaniczny jest")
        #Mysz
        self.add_node(self.answers[14],"ser","je")
        self.add_node(self.answers[14],"mała","jest")
        self.add_node(self.answers[14],"gryzoniem","jest")
        self.add_node(self.answers[14],"w norze","żyje")
        self.add_node(self.answers[14],"do sterowania kursorem","służy")
        self.add_node(self.answers[14],"np. domowa lub polna","jest")

        #Wąż
        self.add_node(self.answers[15],"wije się","Co robi?")
        self.add_node(self.answers[15],"łuski","ma")
        self.add_node(self.answers[15],"kończyn","nie ma")
        self.add_node(self.answers[15],"gadem","jest")
        self.add_node(self.answers[15],"jadowity lub dusicielem","może być")
        self.add_node(self.answers[15],"Pojawia się w motywie Uroboros","Co robi?")
        
        #Pszczoła
        self.add_node(self.answers[16],"owadem","jest")
        self.add_node(self.answers[16],"miód","daje")
        self.add_node(self.answers[16],"paski","ma")
        self.add_node(self.answers[16],"czarno-żółta","jest")
        self.add_node(self.answers[16],"w ulu","żyje")
        self.add_node(self.answers[16],"z osą","jest mylona")

        #Mucha
        self.add_node(self.answers[17],"owadem","jest")
        self.add_node(self.answers[17],"powszechnie spotykana","jest")
        self.add_node(self.answers[17],"bzyczy","Co robi?")
        self.add_node(self.answers[17],"nie siada","Co robi?")
        self.add_node(self.answers[17],"nią np. końśka lub tse-tse","jest")
        self.add_node(self.answers[17],"można mieć ją w nosie","Co robi?")

    def add_node(self,answer,node,activity): #metoda dodająca węzły/hasła do sieci
        self.network.add_edge(answer,node,activity=activity)
    def get_edge_data(self,u,v):#metoda pobierająca dane z krawędzi sieci, opisujące relację między węzłami
        return self.network.get_edge_data(u,v)
    def remove_answer(self,answer): #metoda usuwająca hasło z listy
        if len(self.answers)>1: #zabezpieczenie - zapewnia, że jedno hasło na pewno pozostanie na liście 
            self.answers.remove(answer)   
    def plot_network(self): #metoda wyświetlająca sieć semantyczną na wykresie
        pos = nx.spring_layout(self.network, seed=42)
        nx.draw(self.network, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
        nx.draw(self.network, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
        plt.title("Sieć semantyczna zwierząt")
        plt.show()


class puzzle: #klasa zagadki
    score=0 #wynik 
    count=0 #liczba wygenerowanych zagadek
    difficulty=4 #poziom trudność 4-łatwy 3-średni 2-trudny
    def __init__(self):
        self.semantic_network=animals_semantic_network() # tworzona jest instancja sieci semantycznej zwierząt
    

    def generate_puzzle(self):#metoda tworząca zagadkę
        answer=choice(self.semantic_network.answers) #wybierane jest losowe hasło
        properties=[j  for i,j in list(self.semantic_network.network.edges) if i==answer] #zbieramy wszystkie właściwości powiązane z hasłem
        properties=sample(properties,self.difficulty)#z zebranych właściwości losowo wybieramy 2,3 lub 4, w zależnośći od poziomu trudnośći
        self.print_puzzle(answer,properties) #wyświetlanie zagadki
        
        user_answer=input()
        self.count+=1
        if(user_answer.upper()==answer.upper()): #Poprawna odpowiedź, gracz zdobywa punkt oraz hasło zostaje usunięte z listy(aby gracz nie mógł potem go wylosować ponownie)
            print('Dobrze')
            self.score+=1
            self.semantic_network.remove_answer(answer)
        else:
            print('Źle! To jest {}'.format(answer))

    def greet(self):#Ekran startowy i wybór poziomu trudności
        print("Witaj w grze!")
        c=5
        while c>3 or c<1:
            print("Wybierz poziom trudności")
            print("1)Łatwy\n2)Średni\n3)Trudny")
            c=int(input())
        self.difficulty=5-c

    def print_puzzle(self,answer,properties): #Metoda wyświetlająca zagadkę
        check_activity=lambda a: a if a!='Co robi?' else '' #Gdy activity ma wartość 'Co robi?', to tego nie wyświetlać
        
        #Tworzymy listę z pojęciami opisującymi zwierzaka
        data=["{} {}".format(check_activity(self.semantic_network.get_edge_data(answer,property)['activity']),property) for property in properties]
        
        data[0]=data[0].strip().capitalize() #Zabieg estetyczny - zapewnia, że zdanie zawsze zaczyna się wielką literą  

        riddle="Co to jest? "
    
        if self.difficulty==2: #Najtrudnieszy poziom - 2 podpowiedzi
            riddle+=" i ".join(data)
        elif self.difficulty==3: # Średni - 3
            riddle+="{}, {} i {}".format(*data)
        elif self.difficulty==4: # Łatwy - aż 4
            riddle+="{}, {}, {} i {}".format(*data)

        print(riddle)


    def print_result(self): #Metoda wyświetlająca wyniki
        print("Koniec gry!\nTwój wynik to {}/{}".format(self.score,self.count))
        result=self.score/self.count
        if result < .5:
            print("Słabo. Popraw się!")
        elif result >= .5 and result<.75:
            print("Niby coś wiesz o zwierzętach, ale stać cię na więcej")
        elif result>=.75 and result <.9:
            print("Zdecydowanie znasz się na zwierzętach!")
        else:
            print("Jesteś prawdziwym znawcą zwierząt! Może warto rozważyć napisanie pracy naukowej o nich?")




if __name__=='__main__':
    x=puzzle()
    #x.semantic_network.plot_network() #wyświetlanie struktury sieci semantycznej
    x.greet()
    no_of_puzzles=5  #liczba zagadek
    for _ in range(no_of_puzzles): #generujemy odpowiednią ilość zagadek
        x.generate_puzzle()
    x.print_result() #Wyświetlamy wyniki



