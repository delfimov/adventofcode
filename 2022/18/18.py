lava = []
g = {}
adj = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
max_coord = 0
min_coord = -4

for nnn in [[int(s) for s in x.split(',')] for x in open('input.txt').readlines()]:
    t = tuple(nnn)
    max_coord = max(max_coord, *t)
    if t not in g:
        g[t] = 1
    g[t] = 1
    lava.append(t)

r = 0
for nx,ny,nz in lava:
    for dx,dy,dz in adj:
        tx = nx + dx
        ty = ny + dy
        tz = nz + dz
        if (tx,ty,tz) not in g or g[tx,ty,tz] == 0:
            r += 1
print(r)


# min_coord to max_coord for all coords

def dfs(x,y,z,c):
    stack = [(x,y,z)]
    while len(stack) > 0:
        x,y,z = stack.pop(-1)
        if x<min_coord or x>max_coord+1 or y<min_coord or y>max_coord+1 or z<min_coord or z>max_coord+1 or (x,y,z) in g:
            continue
        g[x,y,z] = c
        for dx,dy,dz in adj:
            stack.append((x+dx,y+dy,z+dz))

nc = 2
for i in range(0,max_coord):
    for j in range(0,max_coord):
        for k in range(0,max_coord):
            dfs(i,j,k,nc)
            if g[i,j,k] == nc:
                nc += 1
r2 = 0
for nx,ny,nz in lava:
    for dx,dy,dz in adj:
        tx = nx + dx
        ty = ny + dy
        tz = nz + dz
        if g[tx,ty,tz] == g[min_coord,min_coord,min_coord]:
            r2 += 1
print(r2)
