#created by me 


from django.http import HttpResponse ;
from django.shortcuts import render;


def index(request):
    return render( request , 'index.html'  )

def about(request):
    return render(request , 'about.html')
    
def process(request):
    data = request.POST.get('text' , "default")
    rmvpuncs = request.POST.get('rmvpunc','off')
    capitlz = request.POST.get('capitalize' , 'off')
    newlinermv=request.POST.get("newlinermv","off")
    extraspacermv=request.POST.get("extraspacermv","off")
    chcounter = request.POST.get("chcounter" , "off")


    adata=data
    purpose=""

    if rmvpuncs == 'on':
        puncs='''.,-_?!''"";:(){,}[]'/'''
        temp=""
        for ch in data :
            if ch not in puncs :
                temp = temp+ch
        purpose+="Remove Punctuations "
        params={'output': temp , 'purpose' : purpose }
        adata=temp
        
    if  capitlz == "on":
        temp=""
        for ch in adata :
            temp = temp + ch.upper()
        purpose +="  Capitallized All "
        params={'output' : temp , 'purpose' : purpose}
        adata=temp
    if  newlinermv == "on":
        temp=""
        for ch in adata :
            if ch !="\n" :
                temp = temp + ch
        purpose+=" New Lines Removed "
        params={'output' : temp , 'purpose' : purpose }
        adata=temp

    if  extraspacermv == "on":
        temp=""
        for index,ch in  enumerate(adata):
            if not(adata[index] == " " and adata[index+1] == " " ):
                temp = temp + ch
        purpose+="  Extra Spaces Removed "
        params={'output' : temp , 'purpose' : purpose}
        adata=temp
    if  chcounter == "on":
        count=0
        for ch in adata :
            count+=1
        purpose+="  Character counter"
        params={'output' : adata, 'purpose' : purpose , 'count': count }
    if  (rmvpuncs=="on" or capitlz=="on" or newlinermv=="on" or  extraspacermv=="on" or chcounter=="on" or  chcounter=="on") :
        return render(request , 'analyze.html', params)
    else :
        params={'purpose':"Error : No operation selected"}
        return HttpResponse('<center  >Error ! Please select a operation </center>')

