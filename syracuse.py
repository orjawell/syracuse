
import matplotlib.pyplot as plt

def syracuse(x,iteration):
    iteration_liste = []
    result = []
    i = 0
    val = x
    while i <= iteration:
        i = 0
        if x != val:
            x = val + 1
            val = val + 1
            #print(val)
        while x!=1:
            #iteration = []
            #result = []
            if x%2==0:
                x = x/2
                i = i+1
                #iteration.append(i)
                #result.append(x)
                #print("new val: ",x)
            else:
                x = (3*x)+1
                i = i+1
                #iteration.append(i)
                #result.append(x)
                #print("new val: ",x)

    print(val)
    print(i)
    #plt.plot(iteration, result)
    #plt.ylabel("résultat")
    #plt.xlabel("itération")
    #plt.show()

