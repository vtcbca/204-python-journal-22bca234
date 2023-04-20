#Create a list of 5 value with filename and extension. Replace extension with".c" with ".py" and print new list.
#filenames = ["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]
def replist(l):
    changed_list=[]
    rep=".c"
    for i in l:
        if rep in i: 
            r=i.replace(".c",".py")
            changed_list.append(r)
        else:
            changed_list.append(i)    
    print(changed_list)
filenames=["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]
replist(filenames)
