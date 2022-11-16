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
    ballStartX = 100
    ballStartY = surfaceSize[1] - surfaceSize[1]/10
    theta = 0
    gravity = 1.2 #gravity positive, because decreasing height increases y-coordinate
    
    runCount = 0
    running = False
    
    divisor = 10
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
        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            running = True
            runCount = 0
            
            velocity = (math.sqrt(math.pow((mouseX - ballStartX), 2) + math.pow((mouseY - ballStartY), 2))/divisor) / clockSpeed
            
            theta = math.atan((mouseY - ballStartY) / (mouseX - ballStartX))
            velocityX = velocity * math.degrees(math.cos(theta))
            velocityOneY = velocity * math.degrees(math.sin(theta))
            

        
        mainSurface.fill((25, 25, 25))


          
        if running:
            height = (velocityOneY * runCount) + (0.5 * gravity * (math.pow(runCount, 2))) + ballStartY
            distance = (velocityX * runCount) + ballStartX
            if height > ballStartY:
                running = False
            else:
                pygame.draw.circle(mainSurface, (255, 0, 0), (distance, height), 10)
                runCount += 1

               
        pygame.draw.circle(mainSurface, (0, 0, 255), (ballStartX, ballStartY), 10)
        
        pygame.display.flip()
        
        clock.tick(clockSpeed) #


    pygame.quit()     # Once we leave the loop, close the window.

main()