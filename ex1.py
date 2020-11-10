# x=[1,8,3,4,15,6,7,28,9,10,12,53,14,15,76,17,18,19,20]
# u=0
# for n in range (0, 19):
#     for i in range (0, 19):
#         if  x[n] < x[i]:
#             u=x[n]
#             x[n]=x[i]
#             x[i]=u
# print(x)


# import random

# x=[]
# a=0
# max=900
# x=[max]
# while a < max:
#     x.append(random.randint(1,1000))
#     a += 1
# m=0
# u=0
# for n in range (0, max+1):
#     for i in range (0, max+1):
#         if  x[n] < x[i]:
#             u=x[n]
#             x[n]=x[i]
#             x[i]=u
#             m +=1
# print(x)
# print(m)



# Ecrire un algo qui demande une valeur à l'utilisateur et dit a l'utilisateur si elle est présente ou non dans le tableau.
# - Utiliser un booléen
# - Arrter le parcours du tableau si elle est trouvée.



# import random

# b=int(input())
# x=[]
# a=0
# max=20
# x=[max]
# while a < max:
#     x.append(random.randint(1,50))
#     a += 1

#if b != x:
#         print("votre valeur n'est pas compris dans le tableau")
#     else:
#         print("votre valeur est compris dans le tableau")
# print(x)


# import random

# b=int(input())
# x=[]
# a=0
# max=20
# p=0
# x=[max]
# Salut = False
# while a < max:
#     x.append(random.randint(1,50))
#     a += 1
# for i in range (0,20):
#     if b == x[i]:
#         Salut = True

# if Salut == True:
#     print("votre valeur est compris dans le tableau")
# else:
#     print("votre valeur n'est pas compris dans le tableau")
# print(x)


# import random
# list1=[]
# a=0
# max=20
# list1=[max]
# while a < max:
#     list1.append(random.randint(1,50))
#     a += 1

# stockage = 0
# print(list1)
# permute = True
# while permute == True :
#     permute = False    
#     for i in range (0,20) :     
#         if list1[i] > list1[i+1] :
#             stockage = list1[i]
#             list1[i] = list1[i+1]
#             list1[i+1] = stockage
#             permute = True
# print(list1)


# x= []
# l=0

# for j in range (0,13):
#     for i in range(0,6):
#         x[j][i] = l
#         l +=1
# print(x)

x=[]
i=0
j=0
capa=63
x=[capa][capa]
val=1
for i in range (0,capa):
    for j in range (0,capa):
        x[i][j]= val
        val=val*2
for i in range(0,capa):
    for j in range(0,capa):
        print(x[i][j])