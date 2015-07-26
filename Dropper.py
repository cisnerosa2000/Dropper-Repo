from Tkinter import *
import random
import math

main = Tk()
main.title('Number of Blocks Per Spawn and Spawn Delay')
main.minsize(400,200)



delay = Scale(main,from_=1000,to=100)
delay.pack()
num = Scale(main,from_=1,to=10,orient=HORIZONTAL)
num.pack()



def start():
    
    global numget
    global delayget
    numget = num.get()
    delayget = delay.get()
    
    root = Toplevel()
    root.title('Avoid The Blocks!')

    canvas = Canvas(root)
    canvas.config(width=600,height=600,bg='dark red')
    
    global key
    key = ''
    
    text = Text(root)
    text.config(width=100,height=1)
    text.insert(INSERT,'Score: ')
    text.config(state=DISABLED)
    text.pack()
    
    class Encryption(object):
        def __init__(self,encryptme,decryptme):
            self.encryptme = encryptme
            self.decryptme = decryptme
            
        def encrypt(self):
            global key
            for emptyspace in range(0,10):
               emptyspace = random.randint(0,9)
               key += str(emptyspace)
        
        
            score2 = self.encryptme ** 2
            score3 = str(score2)[::-1]
     
            return str(key) + str(key).join(str(score3))
       
        def decrypt(self):
            tbd = self.decryptme
            oldkey = (tbd[0]+ tbd[1] + tbd[2] + tbd[3] + tbd[4]+ tbd[5]+ tbd[6]+ tbd[7]+ tbd[8]+ tbd[9])
            
            newtbd = tbd.split(oldkey)
            newtbd = "".join(newtbd)
    
            decoded = newtbd.split(oldkey)
            decoded = "".join(decoded)
            
            decoded2 = decoded[::-1]
            return math.sqrt(int(decoded2))

    
    
    
    

    
    squareimg = PhotoImage(file="Goal.gif")
    playerimg = PhotoImage(file="Triangle.gif")

    global thing
    thing = True

    global score
    score = 0
    global lossonce
    lossonce = True

    def loss():
        global lossonce
        global score

        if lossonce == True:
            # stuff here
            lossonce = False
            root.destroy()   
        
            youlost = Tk()
            youlost.title('You Lose!')
            youlost.minsize(300,100)
            
        
        
            with open('HighScore.txt','r') as read_old_score:
                
                decryptsoon = read_old_score.read()
                doody = Encryption(decryptme=decryptsoon,encryptme="Ignore Me!")
                highest_score = doody.decrypt()
                
                
                
                
               
            
            if score > float(highest_score):
                with open('HighScore.txt','w') as new_high_score:
                    poopy = Encryption(encryptme = score,decryptme="Ignore Me!")
                    new_high_score.write(poopy.encrypt())
                    
                    
                
            
            encryptedscore = Encryption(encryptme = score, decryptme = "Ignore please!")
        
        
        
            
            if score > float(highest_score):
                loser = Label(youlost,text="New high score of %s!" % (score)).pack()
            else:
                loser = Label(youlost,text="You got a score of %s! Your high score is %s" % (score,int(highest_score))).pack()
           

            def kill(event):
                youlost.destroy()
                
            youlost.bind("<Down>",kill)
        
        
            youlost.mainloop()
        
         
    
    
    playerpic = canvas.create_image(300,550,image=playerimg)
    def squareloop():
        global square
        global score
    
        canvas.move("squares",0,7)
    
        canvas.addtag_overlapping("out_of_bounds",0,800,600,900)
        canvas.delete("out_of_bounds")
        
        
        text.config(state=NORMAL)
        text.delete(1.0,END)
        text.insert(INSERT,'Score = %s' % score)
        text.config(state=DISABLED)
        
        
        
        
    
        playerbbox = canvas.bbox(playerpic)
        overlap = canvas.find_overlapping(*playerbbox)
    
        if len(overlap) > 1:
            loss()
    
        root.after(3,squareloop)

    def makesquare():
        global thing
        global score
        global square
        
        global delayget
        global numget
        
    
        for num in range(0,numget):
            square = canvas.create_image(random.randint(0,600),0,image=squareimg,tags="squares")
            score += 10   
  
    
    
        if thing == True:
            squareloop()
            thing = False
        
    
        
        
        
        
    
        
        
        root.after(delayget,makesquare)

    makesquare()


    def moveleft(event):
        if canvas.coords(playerpic)[0] > 50:
            canvas.move(playerpic,-30,0)
    def moveright(event):
        if canvas.coords(playerpic)[0] < 550:
            canvas.move(playerpic,30,0)


    root.bind("<Left>",moveleft)
    root.bind("<Right>",moveright)
    root.bind("<a>",moveleft)
    root.bind("<d>",moveright)

    canvas.pack()
    root.mainloop()

startbutton = Button(main,text="Confirm and Start?",command=start).pack()
main.mainloop()