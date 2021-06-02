from django.shortcuts import render
import pandas as pd
import re
# Create your views here.
def main(request):
    if request.method == "POST":
        person=request.POST['name']
        data=pd.read_csv("./main/phone-numbers.csv")
        detail={}
        name=data["Name"].to_list()
        number=data["Number"].to_list()
        for i in range(len(name)):
            detail[number[i]]=name[i].lower()
        reObj = re.compile(person)
        z=[]
        y=[]
        c=[]
        i=0
        for number, name in detail.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            if reObj.match(name):
                z.append(name)
                y.append(number)
                i+=1
                c.append(i)
        html=pd.DataFrame({'name':z,'number':y})
        htmlf = html.to_html()
        text_file = open("./tamplates/table.html", "w")
        text_file.write(htmlf)
        text_file.close()
        return render(request,'main.html',{"name":z,"number":y,"len":c})


    else:
        return render(request,'main.html')
