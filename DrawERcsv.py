#Draw Escape routes using nodecoords.csv and connectivity.csv for KFX
import csv
Ns = {}
with open('nodecords_jal.csv', 'r') as file:
# with open('n.csv', 'r') as file:
    reader = csv.reader(file)
    for n in reader:
        Ns[n[0]] = [float(x) for x in n[1:]]
        # print(Ns[n[0]])
Cs = []
with open('connectivity_jal.csv', 'r') as file:
# with open('c.csv', 'r') as file:
    reader = csv.reader(file)
    for c in reader:
        Cs.append([c[0],c[1],True])
        

er_box = open("er_box.kfx","w")
#For each connection
for c in Cs:
    x1,y1,z1 = Ns[c[0]]
    x2,y2,z2 = Ns[c[1]]
    dx,dy,dz = x2-x1,y2-y1,z2-z1
    if z1 != z2:
        color = "0 0 1"    
    elif z1 > 51.9:
        color = "0 1 0.3"    
    elif z1 == 44:
        color = "0 1 0.6"    
    elif z1 == 35:
        color = "0 1 0.9"
    z1 += 1.5        
    z2 += 1.5        

    er_box.write("COLOR: "+color+"\nPART: "+c[0]+"_"+c[1]+"\n")                                
    er_box.write("TEXT: {:8.1f} {:8.1f} {:8.1f} {:s}\n".format(x1,y1,z1+1.,c[0]))                                
    er_box.write("SBOX: {:10.1f} {:10.1f} {:10.1f} {:10.1f} {:10.1f} {:10.1f} 400 400\n".format(x1*1000,y1*1000,z1*1000,x2*1000,y2*1000,z2*1000))

er_box.close()
