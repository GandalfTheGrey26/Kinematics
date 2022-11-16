import pygame, math

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = [1440, 910]
    
    clockSpeed = 60
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    mainSurface = pygame.display.set_mode((surfaceSize[0], surfaceSize[1]))

   
   
    #--------------------------------   
    ballStartX = 100    #the starting (x) position of the ball
    ballStartY = surfaceSize[1] - surfaceSize[1]/10 #the starting (y) position of the ball
    theta = 0 #initialize theta
    gravity = 1.2 #gravity positive, because decreasing height increases y-coordinate
    
    runCount = 0 #a counter to loop through the motion of the function
    running = False #whether the ball is moving
    
    divisor = 10 #a variable for to use to make the velocity smaller
    #--------------------------------
    
    

    #-----------------------------Main Program Loop---------------------------------------------#
    while True:       
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        mouseX, mouseY = pygame.mouse.get_pos()
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_EQUALS: 
                divisor += 0.5
            if ev.key == pygame.K_MINUS:
                divisor -= 0.5
        
        if ev.type == pygame.MOUSEBUTTONDOWN: #mouse button is pressed
            running = True #set the ball to moving
            runCount = 0   #reset the move counter
            
            #use pythagorean theorem to get the distance between the mouse and the ball, then divide it by the divisor to get the speed in seconds, then divide by clock speed to get the speed in runs (frames)
            velocity = (math.sqrt(math.pow((mouseX - ballStartX), 2) + math.pow((mouseY - ballStartY), 2))/divisor) / clockSpeed
            
            theta = math.atan((mouseY - ballStartY) / (mouseX - ballStartX)) #use trig ratio: tan(theta) = (opposite / adjacent); to get the launch angle
            velocityX = velocity * math.degrees(math.cos(theta))             #use trig ratio: cos(theta) = (opposite / hypotenuse); to get the (constant) x velocity
            velocityOneY = velocity * math.degrees(math.sin(theta))          #use trig ratio: sin(theta) = (adjacent / hypotenuse); to get the y velocity
            

        
        mainSurface.fill((25, 25, 25))


          
        if running:
            height = (velocityOneY * runCount) + (0.5 * gravity * (math.pow(runCount, 2))) + ballStartY #use kinematic equation: height (delta Dy) = (VelocityY * t) + (half * gravity * (t squared)) + initial height; 't' is the runCount
            distance = (velocityX * runCount) + ballStartX                                              #use kinematic equation: distance (delta Dx) = (VelocityX * t) + initial distance; 't' is the runCount
            if height > ballStartY: #the ball is below it's starting position:
                running = False        #...stop running
            else:
                pygame.draw.circle(mainSurface, (255, 0, 0), (distance, height), 10) #draw the circle
                runCount += 1 #increase the runCount by one

               
        pygame.draw.circle(mainSurface, (0, 0, 255), (ballStartX, ballStartY), 10)
        
        pygame.display.flip()
        
        clock.tick(clockSpeed) #


    pygame.quit()     # Once we leave the loop, close the window.

main()