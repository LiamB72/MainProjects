from random import randint
from time import sleep

vocabulaire = {
    "die Märchen" : {
        "lstG" : ["das Märchen",
                  "die wundersame Geschichte",
                  "die Erzählung (1)",
                  "die Erzählung (2)",
                  "eine Geschichte erzählen",
                  "das Kulturgut",
                  "das Volk",
                  "volkstümlich",
                  "die Volkserzählung",
                  "das Volksmärchen",
                  "der Zeitspiegel",
                  "zeitgemäß",
                  "ein zeitloses Motiv haben",
                  "die Wirklichkeit wider",
                  "der Realität entsprechen",
                  "der Zauber",
                  "die Zauberwelt",
                  "etw. zaubern",
                  "das Vorlesen",
                  "jm vor/lesen",
                  "jm ein Märchen vor/lesen",
                  "der Ursprung", 
                  "ursprünglich",
                  "früher",
                  "heute",
                  "heutzutage",
                  "damals",
                  "der Mund",
                  "der Volksmund",
                  "etw. mündlich überliefern",
                  "überliefert sein",
                  "für Kinder gedacht sein",
                  "für Kinder geeignet sein",
                  "der Erwachsene",
                  "sich an Erwachsene richten",
                  "das Ende",
                  "gut enden",
                  "die Moral",
                  "ein Märchen ist eine moralische Geschichte",
                  "ein Märchen bringt eine ethische Lehre",
                  "es hat einen pädagogischen Zweck",
                  "Grimms Märchen sind Erziehungsbücher",
                  "die Botschaft",
                  "eine Botschaft vermitteln",
                  "die Wahrnehmung etw. wahr/nehmen",
                  "die Persönlichkeitsentwicklung",
                  "die Emanzipation",
                  "das Wert",
                  "die Tugend",
                  "die bestrafen",
                  "die Bestrafung",
                  "jn bestrafen",
                  "die Belohnung",
                  "jn vor einer Gefahr retten",
                  "jm das Leben retten",
                  "die Veröffentlichung",
                  "veröffentlichen",
                  "sammeln",
                  "das Sammeln",
                  "der Sammelband",
                  "die Sammlung"],

        "lstF" : ["le conte",
                  "l'histoire merveilleuse",
                  "le récit",
                  "l'histoire",
                  "raconter une histoire",
                  "un élément du patrimoine culturel",
                  "le peuple",
                  "populaire",
                  "le récit populaire",
                  "le conte populaire",
                  "le reflet de l'époque",
                  "conforme à l'époque",
                  "avoir un thème intemporel",
                  "refléter la réalité",
                  "correspondre à la réalité",
                  "le sort",
                  "le monde enchanté",
                  "faire apparaître qch (comme) par magie",
                  "la lecture",
                  "faire la lecture à qn",
                  "lire un conte à qn",
                  "l'origine", 
                  "au début",
                  "autrefois",
                  "aujourd'hui",
                  "de nos jours",
                  "à l'époque",
                  "la bouche",
                  "le langage populaire",
                  "transmettre qch oralement",
                  "être transmis de génération en génération",
                  "être pensé pour les enfants",
                  "être adapté pour les enfants",
                  "l'adulte",
                  "s'adresser aux adultes",
                  "la fin",
                  "bien finir", 
                  "la morale", 
                  "un conte est une histoire morale", 
                  "un conte apporte un enseignement éthique",
                  "il a un objectif pédagogique", 
                  "les contes de Grimm sont des livres d'éducation", 
                  "le message", 
                  "transmettre un message", 
                  "comprendre qch",
                  "le développement personnel", 
                  "l'émancipation", 
                  "la valeur", 
                  "la vertu", 
                  "la punition", 
                  "sanction",
                  "sanctionner qn", 
                  "la récompense", 
                  "sauver qn d'un danger", 
                  "sauver la vie de qn", 
                  "la publication", 
                  "publier", 
                  "collecter", 
                  "la collecte",
                  "le recueil", 
                  "la collection"]
    },
    "die Angst" : {
        "lstG" : ["die Angst",
				  "etw. aus Angst machen" ,
				  "Angst bekommen",
				  "vor jm/etw. Angst haben",
				  "sich vor jm/etw. ängstigen",
				  "um jn Angst haben",
				  "jm Angst machen",
				  "beängstigend sein",
				  "der Schreck (1)",
				  "der Schreck (2)",
				  "jm einen Schreck ein/jagen" ,
				  "jn erschrecken",
				  "erschrecken",
				  "erschreckend sein",
				  "schrecklich sein",
				  "die Furcht",
				  "Furcht vor jm haben",
				  "sich vor jm/etw. fürchten",
				  "etw. fürchten",
				  "furchtbar sein",
				  "das Gruseln",
				  "sich gruseln",
				  "die Gruselgeschichte",
				  "der Gruselfilm",
				  "gruselig",
				  "schauern",
				  "vor Entsetzen erschauern",
				  "jn erschauern lassen",
				  "der Schauerroman"],

        "lstF" : ["la peur",
				  "faire qch par peur",
				  "prendre peur",
				  "avoir peur de qn",
				  "avoir peur de qch",
				  "avoir peur pour qn",
				  "faire peur à qn",
				  "être effrayant",
				  "la peur",
				  "l'effroi",
				  "faire peur à qn",
				  "faire peur à qn",
				  "avoir peur",
				  "être effrayant",
				  "être affreux",
				  "la crainte",
				  "avoir peur de qn",
				  "avoir peur de qch",
				  "craindre qch",
				  "terrible",
				  "le frisson",
				  "avoir le frisson",
				  "le récit d'épouvante",
				  "le film d'épouvante",
				  "épouvantable",
				  "frissonner",
				  "frissonner d'épouvante",
				  "donner le frisson à qn",
				  "le roman d'épouvante"]
    },
    "HVE" : {
        "lstG": ["der Held",
				 "die Heldin",
				 "das Vorbild",
				 "exemplarisch",
				 "jm als Vorbild dienen",
				 "sich jn zum Vorbild nehmen",
				 "eine Rolle nach/spielen",
				 "die Eigenschaft",
				 "das Wert",
				 "frech sein",
				 "gehorsam",
				 "ungehorsam",
				 "vorsichtig",
				 "unvorsichtig",
				 "die Weisheit",
				 "weise sein",
				 "die Klugheit",
				 "klug sein",
				 "lebensklug sein",
				 "schlau",
				 "die Macht", 
				 "mächtig sein",
				 "die Bosheit",
				 "böse",
				 "die Güte", 
				 "gut sein",
				 "die Menschlichkeit", 
				 "menschlich sein",
				 "die Schönheit",
				 "schön sein",
				 "hübsch sein",
				 "das Abenteuer",
				 "abenteuerlustig sein",
				 "der Mut",
				 "mutig",
				 "der Fleiß",
				 "fleißig sein",
				 "die Treue",
				 "treu sein"],

        "lstF": ["le héros",
				 "la héroïne",
				 "le modèle", 
				 "exemplaire",
				 "servir de modèle à qn",
				 "prendre qn pour modèle",
				 "rejouer un rôle après qn",
				 "le trait de caractère",
				 "la valeur",
				 "être insolent",
				 "obéissant",
				 "désobéissant",
				 "prudent",
				 "imprudent",
				 "la sagesse",
				 "être sage",
				 "le bon sens",
				 "être avisé",
				 "avoir du bon sens",
				 "astucieux",
				 "le pouvoir",
				 "être puissant",
				 "la méchanceté",
				 "méchant",
				 "la bonté",
				 "être bon",
				 "l'humanité",
				 "être humain",
				 "la beauté",
				 "être beau/belle",
				 "être joli/e",
				 "l'aventure",
				 "avoir le goût de l'aventure",
				 "le courage",
				 "courageux",
				 "le zèle",
				 "être travailleur",
				 "la fidélité",
				 "être fidèle"]
    }
}

class revision():

    def __init__(self):

        self.quit = False
        
        self.menu = True
        menu = ""
        
        self.define_lists()
        while not self.quit:
            
            if self.menu:
                
                self.menu = False

                print(f"\n\nAllemand: {self.lenG} mots,\nFrançais: {self.lenF} mots\n## Tu peux quitter à tout moments en entrant \"q\".")
                print("\n\n<<-------------------->>\n")

                if self.userInput == "r" :
                    self.define_variables()
                    self.run_revision()
                    menu = input("Go Back to Menu? (Y/N): ")
                    menu = menu.lower()
                    if menu == "y":
                        self.menu = True  
                    else:
                        self.quit = True
                    
                if self.userInput == "t" :
                    self.run_translate()
                
    def define_lists(self):
        self.userInput = input("\nRevison (R) / Traduire (T) : ")
        self.userInput = self.userInput.lower()
        if self.userInput == 'q':
            self.quit = True  
            return self.quit

        theme = input("\nMärchen Themed (M)\nAngst Themed (A)\nHeld - Vorbild - Eigenschaften Themed (HVE)\nChoice: ")
        theme = theme.lower()

        if theme == "m":
            self.lstG = vocabulaire["die Märchen"]["lstG"]
            self.lstF = vocabulaire["die Märchen"]["lstF"]
        if theme == "a":
            self.lstG = vocabulaire["die Angst"]["lstG"]
            self.lstF = vocabulaire["die Angst"]["lstF"]
        if theme == "hve":
            self.lstG = vocabulaire["HVE"]["lstG"]
            self.lstF = vocabulaire["HVE"]["lstF"]

        self.lenG = len(self.lstG)
        self.lenF = len(self.lstF)

    def define_variables(self):
        self.z = 0
        self.rand = 0

        self.wordG = self.lstG[self.z]
        self.wordF = self.lstF[self.z]

        self.usedWords = []

        self.lenghtTraining = int(input("\nCombien de mots veux tu traduire : "))
        self.lenghtTraining = abs(self.lenghtTraining)

        self.toGerman = input("\nVeux traduire du français à l'allemand? (Y/N) : ")
        self.toGerman = self.toGerman.lower()

        self.toGerman = True if self.toGerman == "y" else False

    def run_revision(self):
        if self.lenghtTraining <= self.lenG:
            a = 0
            while a < self.lenghtTraining:
                
                a += 1
                self.z = randint(0, self.lenG-1)
                if self.toGerman:
                    self.rand = randint(0, 4)
                else:
                    self.rand = 0

                #print(a, self.z)

                if (self.lstG[self.z] in self.usedWords):
                    self.lenghtTraining += 1

                else:
                    if self.rand == 0:
                        userAnswer = input(f"{self.lstG[self.z]} = ")
                        
                        if userAnswer == "q":
                            self.menu = "y"
                            return self.quit
                        else:
                            self.quit = ""
                        
                        if userAnswer == self.lstF[self.z]:
                            print("Oui!\n")
                        else:
                            print(f"Non! C'est \"{self.lstF[self.z]}\"\n")

                    elif self.rand == 1 and self.toGerman:
                        
                        if userAnswer == "q":
                            self.menu = "y"
                            return self.quit
                        else:
                            self.quit = ""
                        
                        userAnswer = input(f"{self.lstF[self.z]} = ")
                        if userAnswer == self.lstG[self.z]:
                            print("Oui!\n")
                        else:
                            print(f"Non! C'est \"{self.lstG[self.z]}\"\n")

                    self.usedWords.append(self.lstG[self.z])

        else:
            for _ in range(self.lenghtTraining):
                self.z = randint(0, self.lenG-1)
                if self.toGerman:
                    self.rand = randint(0, 4)
                else:
                    self.rand = 0

                if self.rand == 0:
                    userAnswer = input(f"{self.lstG[self.z]} = ")
                    
                    if userAnswer == "q":
                        self.menu = "y"
                        return self.quit
                    else:
                        self.quit = ""
                    
                    if userAnswer == self.lstF[self.z]:
                        print("Oui!\n")
                    else:
                        print(f"Not! C'est \"{self.lstF[self.z]}\"\n")

                elif self.rand == 1 and self.toGerman:
                    userAnswer = input(f"{self.lstF[self.z]} = ")
                    
                    if userAnswer == "q":
                        self.menu = "y"
                        return self.quit
                    else:
                        self.quit = ""
                    
                    if userAnswer == self.lstG[self.z]:
                        print("Oui!\n")
                    else:
                        print(f"Non! C'est \"{self.lstG[self.z]}\"\n")

    def run_translate(self):
        userTranslate = ""
        
        while userTranslate != "q":
            
            for i in range(self.lenG):
                print(f"\nMot Allemand numero {i+1:2}: \"{self.lstG[i]}\"", end="")

            userTranslate = input("\n\nMot Allemand : ")
            
            if userTranslate == "q":
                self.menu = "y"
                return self.menu
            
            notFound = 0
            for i in range(self.lenG):

                if userTranslate == self.lstG[i]:
                    notFound -= notFound
                    print(f"\n{userTranslate} = {self.lstF[i]}\n")
                    
                    sleep(1)
                    
                    break

                notFound += 1
            if notFound > 1:
                print("\nMot introuvable")
                
        self.quit = "y"
        return self.quit

revision()
