
from scipy import linalg


#Load world values
with open("world.txt") as f:
    worldFullData = f.readlines()

#Creates worldmap with has rowsxline
worldmap = []
for worldline in worldFullData:
    worldmap.append(worldline.split("  ")[1:])

# #Convert to floatzzzq
# for j in range(3):
#     for i in range(len(worldmap[j])):
#         worldmap[j][i] = float(worldmap[j][i])

#Load image values
with open("image.txt") as f:
    imageFullData = f.readlines()

#Creates imagemap with has rowsxline
imagemap = []
for imageline in imageFullData:
    imagemap.append(imageline.split("  ")[1:])

#Convert to float
# for j2 in range(2):
#     for i2 in range(len(imagemap)):
#         imagemap[j][i] = float(imagemap[j][i])



#[COORD][PT#]

#Build 20x12 Matrix A
#Each correspondance contributes 12
#Ap = 0, p has entries containing the vector P
amat = [[0]*12 for x in xrange(12)]
linear_m = [item for sublist in imagemap for item in sublist]
for j2 in range(12):
    for i2 in range(20):
        amat[i2][j2] = linear_m[i2]
U, eigen, Vh = linalg.svd(amat)

P = eigen.reshape(3,4)


#Verify answer
#Code

#Compute the World Coordinates
#PC=0

#Find null space of P
Up, eigenp, Vhp = linalg.svd(P)
print eigenp
