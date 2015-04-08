
m stack import Stack
from turtleDisk import *
from turtle import Turtle
class ThreeTowers:  
    def __init__(self,numDisks):
            self.numDisks = numDisks
	            self.t = Turtle()
		            self.screen = self.t.getscreen()
			            self.height = self.screen.window_height()
				            self.width = self.screen.window_width()
					            self.threePoles = [-self.width/4, 0, self.width/4]
						            self.towers = [Stack(),Stack(), Stack()]
							            self.largestDisk = self.width/3
								            self.diskHeight = self.height/100
									            for i in range(numDisks):
										                disk = Disk(self.largestDisk/(i+2),self.diskHeight   ,self.threePoles[0],0 + self.diskHeight*i)
												            disk.drawDisk('blue')
													                self.towers[0].push(disk)    
															    def moveDisk(self, fromPole,toPole):
															            if self.towers[fromPole].size() > 0:
																                disk1=self.towers[fromPole].peek()
																		            d1width=disk1.getWidth()
																			                #print("disk1 width",d1width)
																					            if self.towers[toPole].size()==0:
																						                    disk = self.towers[fromPole].pop()
																								                    disk.drawDisk('white')
																										                    numInStack = self.towers[toPole].size()
																												                    disk.moveTo(self.threePoles[toPole],0+ self.diskHeight*numInStack)
																														                    self.towers[toPole].push(disk)
																																                    disk.drawDisk('red')
																																		                else:
																																				                disk2=self.towers[toPole].peek()
																																						                d2width=disk2.getWidth()
																																								                #print("disk2 width", d2width)
																																										                if d2width < d1width:
																																												                    print("You cannot place a larger disk on top of a smaller disk, TRY AGAIN!")
																																														                    else:
																																																                        disk = self.towers[fromPole].pop()
																																																			                    disk.drawDisk('white')
																																																					                        numInStack = self.towers[toPole].size()
																																																								                    disk.moveTo(self.threePoles[toPole],0+ self.diskHeight*numInStack)
																																																										                        self.towers[toPole].push(disk)
																																																													                    disk.drawDisk('red')
																																																															                
																																																																	 

																																																																	     def moveTower(self, height, fromPole, toPole, withPole):
																																																																	             if height >= 1:
																																																																		                 self.moveTower(height - 1, fromPole, withPole,toPole)
																																																																				             self.moveDisk(fromPole, toPole)
																																																																					                 self.moveTower(height - 1, withPole, toPole, fromPole)
