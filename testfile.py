n():
    import towers
    def whatdisk(num1,num2):
    	hanoi.moveDisk(num1,num2)
    print("Welcome to the Towers of Hanoi Game!")
	n=input("Enter how many disks you would like to play with?")
	n=int(n)
	print("Type end at any time to stop the game")
	hanoi=towers.ThreeTowers(n)
	num1=input("What tower would you like to move a disk from? 1  2  3?")
	num2=input("What tower would like to move the disk to?")
					        
	while num1 !='end'and num2 !='end':
		num1=int(num1)
		num2=int(num2)
		num1=num1-1
		num2=num2-1
		whatdisk(num1,num2)
		num1=input("What tower would you like to move a disk from? 1  2  3?")
		num2=input("What tower would like to move the disk to?)
main()
