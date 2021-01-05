import json,os,pickle
filename=input("enter file name in .txt format")
n=input("enter the operation such as r-read,w-write,d-delete:").lower()
print("enter once again")
d={}
while n!="exit":
    if n =="r":
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                print(f.read())
        else:
            with open(filename, 'w') as f:
                json.dump(d,f)
        n=input("enter the operation such as r-read,w-write,d-delete:").lower()
    elif n=="w":
        with open(filename, 'r') as f:
            per=f.read()
            print(per)
        person_dict=json.loads(per)
        k,v=input("enter key and value pair:").split()
        keys=person_dict.keys()
        if k not in keys:
            person_dict[k]=v
        else:
            print("value already found")
        with open(filename, 'w') as f:
            
            json.dump(person_dict,f)
        with open(filename, 'r') as f:
            print(f.read())
        n=input("enter the operation such as r-read,w-write,d-delete:").lower()
    elif n=="d":
        f=open(filename,'r')
        print(f.read())  
        k=input("enter key to be deleted:")
        person_dict.pop(k)
        with open(filename, 'w') as f:
            json.dump(person_dict, f)
            print(k,"key is deleted")
        with open(filename, 'r') as f:
            print(f.read())   
        n=input("enter the operation such as r-read,w-write,d-delete:").lower()
            



