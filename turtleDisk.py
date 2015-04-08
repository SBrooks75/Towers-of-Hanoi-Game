
m turtle import Turtle
class Disk:
    def __init__(self,width,height,x,y):
            self.x = x
	            self.y = y
		            self.diskTurtle = Turtle()
			            self.width = width
				            self.height = height
					            self.setCorners()    
						        def setCorners(self):
							        #print(self.x, self.x -  self.width/2,self.x + self.width/2)
								        self.upperleft = [self.x-self.width/2,self.y+self.height]
									        self.lowerleft = [self.x-self.width/2,self.y]
										        self.upperright = [self.x+self.width/2,self.y+self.height]
											        self.lowerright = [self.x + self.width/2,self.y]
												        #print('Setting corners', self.x, self.x - self.width/2, self.x + self.width/2)   
													    def drawDisk(self, color):
													            self.diskTurtle.color(color)
														            self.diskTurtle.fillcolor(color)
															            self.diskTurtle.up()
																            self.diskTurtle.goto(self.x,self.y)
																	            self.diskTurtle.down()        
																		            self.diskTurtle.begin_fill()
																			            self.diskTurtle.goto(self.lowerleft)
																				            self.diskTurtle.goto(self.upperleft)
																					            self.diskTurtle.goto(self.upperright)
																						            self.diskTurtle.goto(self.lowerright)
																							            self.diskTurtle.goto(self.x,self.y)
																								            self.diskTurtle.end_fill()
																									            self.diskTurtle.up()
																										        def getWidth(self):
																											        return self.width
																												    def moveTo(self, x,y):
																												            self.x = x
																													            self.y = y
																														            self.setCorners()
																															            #print('moving to',x,y, self.lowerleft,self.upperleft, self.lowerright,self.upperright,self.height,self.width)   
																																        def moveLeft(self,distance):
																																	        self.x -= distance
																																		        self.setCorners()
																																			    def moveRight(self,distance):
																																			            self.x += distance
																																				            self.setCorners()
																																					        def moveDown(self,distance):
																																						        self.y -= distance
																																							        self.setCorners()
																																								    def moveUp(self,distance):
																																								            self.y += distance
																																									            self.setCorners()
