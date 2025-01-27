filenames = ["input.txt"]
f =open("output.txt","w")
f.close()
with open(filenames[0],"r") as file:
    T = int(file.readline().strip())
    for t in range(T):
        target_start = []
        coordinates ={}
        N,M = map(int,file.readline().split())
        grid = N*N
        for i in range(M):
            x, y,n_visite= map(int,file.readline().split())
            coordinates.update({(x,y):n_visite})
            target_start.append(abs(x)+ abs(y))
        print(coordinates,target_start,min(target_start))
        index = target_start.index(min(target_start))
        keys = list(coordinates.keys())
        key = keys[min(target_start)]  # Ottieni la seconda chiave (indice 1)
        print(coordinates[key])
        coordinates[key] = coordinates[key] -1
        print(coordinates)




