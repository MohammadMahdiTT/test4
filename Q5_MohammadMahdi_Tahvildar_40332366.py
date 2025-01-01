# 40332366
# MohammadMahdi Tahvildar

martabe=input().split()
n=martabe[0]
m=martabe[1]

mat=[]
for i in range(len(n)+1):
    a=input()
    mat=mat+[a]

newMat=[]
for j in mat:
    for k in range(len(mat)):
        newMat+= [element[::-1] for element in mat[k]]

print(newMat)