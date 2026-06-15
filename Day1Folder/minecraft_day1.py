# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def t():
    agent.teleport_to_player()


    
player.on_chat("t", t)

def f(step):
    agent.move(FORWARD, step)

player.on_chat("f", f)

def b(step):
    agent.move(BACK, step)

player.on_chat("b", b)

def l(step):
    agent.move(LEFT, step)
    
player.on_chat("l", l)

def r(step):
    agent.move(RIGHT, step)
    
player.on_chat("r", r)

def u(step):
    agent.move(UP, step)

player.on_chat("u", u)

def d(step):
    agent.move(DOWN, step)

player.on_chat("d", d)

def tl():
    agent.turn(TurnDirection.LEFT)

player.on_chat("tl", tl)

def tr():
    agent.turn(TurnDirection.RIGHT)

player.on_chat("tr", tr)

def mazestair():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 3)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("mast", mazestair)

def mazestair2():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    for i in range(2):
        agent.move(FORWARD, 1)
        agent.move(UP, 1)
    agent.move(FORWARD, 3)
    agent.move(DOWN, 1)
    for k in range(2):
        agent.move(FORWARD, 1)
        agent.move(DOWN, 1)


player.on_chat("mast2", mazestair2)
