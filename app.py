name = input("nama monsternya siapa? ")
monster = {'name': name, 'power':100 }

def startGame():
    choice = input("Input perintah: \n1.Makan \n2.Lihat Status \n3.Keluar \nInput anda: ")
    if choice == '1':
        goEat()
    elif choice == '2':
        showStatus()
    elif choice == '3':
        goExit()
    else:
        startGame()
        print("Input yang anda masukan salah! ")

def goEat():
    print("\nNyam.. Nyam..\n")
    monster["power"] += 50
    startGame()

def showStatus():
    print("Cheking Status..")
    print("\nnama monster  : ", monster['name'])
    print(f"lemak         :  {monster['power']}\n")
    startGame()

def goExit():
    print("program berakhir")

startGame()