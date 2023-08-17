def count(n):
    n = n + 1
    print(n)

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    
    TowerOfHanoi(n-1, source, auxiliary, destination)
    count(n)
    
    print ("Move disk",n,"from source",source,"to destination",destination)
    
    TowerOfHanoi(n-1, auxiliary, destination, source)
    count(n)
    

n = int(input('Enter the no of disks: '))
TowerOfHanoi(n,'A','B','C')