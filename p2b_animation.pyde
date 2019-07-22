# Animation (Tie fighter) by Vernon Buck

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    if frameCount > 300:
        exit()
    global time
    time += 0.01

    camera (frameCount, frameCount, 500 - frameCount, 0, 30, 0, 0,  1, 0)  # position the virtual camera

    background (25, 25, 25)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    
    # Object that will be a source of light  directional! golden light
    #Star
    fill (255, 255, 0)
    pushMatrix()
    rotateY(-time)
    translate (0, -200, 250)
    #directional lighting made by star
    spotLight(255,255,0, 0 ,-100, 200,0, 0, -1, PI/4, 2)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(100)
    popMatrix()
    
    #instantiation of tiefighter
    tiefighter(time * 100)
    
    #object that will be instancing
    lx = 60
    ly = 0
    lz = 45
    
    pushMatrix()
    for x in range(0,5):    
        rotateZ (time)
        meteor(lx, ly, lz)
        lx = lx + 20
        ly = ly
        lz = lz + 20
    popMatrix()

def tiefighter(zmove):
    # Tie Fighter wing A
    fill (0,0,0)
    #rotateY(-time) #keep
    pushMatrix()
    translate (30, 0, zmove)
    scale(1,3,1)
    rotate(PI/8)
    rotateY(3)
    box(20)
    popMatrix()
    
    # Tie Fighter wing B
    fill (0,0,0)
    pushMatrix()
    translate (-30, 0, zmove)
    scale(1,3,1)
    rotate(PI/8)
    box(20)
    popMatrix()
    
    # Tie fighter cockpit
    fill (128, 128, 128)
    pushMatrix()
    translate (0, 0, zmove)
    #translate (0, 8 * sin(4 * time), 0)  # move up and down
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(15)
    popMatrix()
    
    # Tie fighter screen
    fill (0, 0, 0)
    pushMatrix()
    #translate (0, 8 * sin(4 * time), 0)  # move up and down
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    translate (3.5, 3.5, zmove + 10)
    sphere(6)
    popMatrix()
    
    # Tie fighter cannon Laser A
    fill (255, 126, 0)
    pushMatrix()
    translate (-5, 10, zmove + 10)
    rotateZ (8)
    rotateX (10)
    scale (.8, .8, .8)
    rotate(PI/3)
    cylinder()
    popMatrix()
    
    # Tie fighter cannon Laser B
    fill (255, 126, 0)
    pushMatrix()
    translate (7, 10, zmove + 10)
    rotateZ (8)
    rotateX (10)
    scale (.8, .8, .8)
    rotate(PI/3)
    cylinder()
    popMatrix()
    
    # Tie fighter Wing connector A
    fill (128, 126, 128)
    pushMatrix()
    translate (20, -3, zmove)
    rotateY (30)
    rotateZ (-10)
    scale (6, 7, 8)
    cylinder()
    popMatrix()
    
    # Tie fighter Wing connector B
    fill (128, 126, 128)
    pushMatrix()
    translate (-20, -3, zmove)
    rotateY (30)
    rotateZ (-10)
    scale (6, 7, 8)
    cylinder()
    popMatrix()

def meteor(la,lb,lc):
    # Object that will be instanced!
    # Random space object partA
    fill (255, 128, 128)
    pushMatrix()
    translate (la, lb, lc)
    #rotateZ (time)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()
    
    # Random space object partB
    fill (255, 128, 128)
    #rotateY(-time)
    pushMatrix()
    translate (la, lb + 15, lc)
    #rotateZ (time)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()
    
    # Random space object partC
    fill (255, 128, 128)
    #rotateY(-time)
    pushMatrix()
    translate (la, (lb + 15)/2, lc - 10)
    #rotateZ (time)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()
    
    # Random space object partD
    fill (255, 128, 128)
    #rotateY(-time)
    pushMatrix()
    translate (la, (lb + 15)/2, lc + 10)
    #rotateZ (time)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2