print("dessinons un triangle ensenble")

height = int(input("donne moi la longeur du triangle je rajout toujour 3: "))
i = height*2+10

espace = "  "
bat= "__"

def draw_triangle():
    if height >=1:
        H=height +1
        esp = [""]
        ba = [""]
        
        tr="/\ "
        
        TRIANGLE_D=tr.center(i)
        print(TRIANGLE_D)
        for index in range(0,height):
            
            esp.append (espace)
            es = "".join(esp)
            t="/"+es+"\ "
            TRIANGLE_M = t.center(i)
            print (TRIANGLE_M)
        
        for index in range(0,H):
            ba.append (bat)
            
        b = "".join(ba)
        T=("/"+b+"\ ")
        TRIANGLE_F = T.center(i)
        print(TRIANGLE_F)
        
draw_triangle()