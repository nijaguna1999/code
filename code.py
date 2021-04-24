#This program is submitted by nijaguna GB.
#This program is written in Python 3
#Note : if the no of employee value exceeds more than the no of goodies then this programs throws error.
#Note : the input must be given in same format as given in sample_input.txt or else ambiguity occurs.

a,d=[],{}

#Reading the file

file=open('C:\\WEB\sample_input.txt','r')   #consider the file path accordingly
for i in file:
    a.append(i)
n=[int(word) for word in a[0].split() if word.isdigit()]
n=n[0]
del a[0:4]
for i in a:
    s, n1 = "", ""
    ans=i
    for j in ans:
        if j=='\n':
            pass
        elif j.isdigit():
            n1+=j
        else:
            s+=j
    d[int(n1)]=s
a=list(d.keys())
a=sorted(a)
ans=a[-1]
x,y=0,0
for i in range(len(a)-n+1):
    if (a[i+n-1]-a[i])<ans:
        ans=a[i+n-1]-a[i]
        x,y=i,i+n-1

#Writing to the file

file = open("C:\\WEB\sample_output.txt", "w")   #consider the file path accordingly
file.write("The goodies selected for distribution are:\n\n")
for i in range(x,y+1):
    file.write(d[a[i]]+str(a[i])+"\n")
file.write('\n')
file.write('And the difference between the chosen goodie with highest price and the lowest price is '+str(ans))
file.close()

file=open("C:\\WEB\sample_output.txt",'r')  #This code block is to see output in console
for i in file:
    print(i)