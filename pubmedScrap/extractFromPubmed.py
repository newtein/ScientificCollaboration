
# coding: utf-8

# In[1]:


import re


# In[2]:


def getEmails(text):
   
    match = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return match

def init_data():
    data={}
   
    data['Author']={}
    data['Journal']=''
    return data
    


# In[3]:


f=open("pubmed_result.txt","r")

data={}
tauthor=''
for l in f:
    if (l[0:2]=="TI"):
        title=" ".join(l.split('-')[1:]).strip()
        nextLine=f.readline()
        if nextLine[0:3]=="   ":
            titleContd=nextLine.strip()
            title=title+" "+titleContd
        
        if title not in data:
            data[title]={}
        data[title]=init_data()
    if (l[0:3]=="FAU"):
        author=l.split('-')[1].strip()
        tauthor=author
    

    r=getEmails(l)
    if len(r)!=0:
        email=r[0]
        if email not in data[title]:
            data[title]['Author'][email]=tauthor
      
    if l[0:2]=="JT":
        journal=l.split('-')[1].strip()
        data[title]['Journal']=journal
        


# In[4]:


f=open("details_v3.csv","w")
l=["Email","Author","Title","Jounral"]
f.write("|#|".join(l)+"\n")
for title in data:
    for email in data[title]['Author']:
        author=data[title]['Author'][email]
        author=author.replace(","," ")
        journal=data[title]['Journal']
        
        l=[email,author,title,journal]
        f.write("|#|".join(l)+"\n")
f.close()
        

