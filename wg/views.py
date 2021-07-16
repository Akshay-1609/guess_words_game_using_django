from django.shortcuts import render,redirect
import random
from django.contrib import messages
# Create your views here.
def guess():
        words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
        return random.choice(words)
def home(request):
    global word,wordict,count,name
    word = guess()
    count=len(word)+8
    # print(count)
    wordict=[]
    return render(request,'index.html')

def game(request):
    if request.method=='POST':
        global count
        print(count)
        print(word)
        name=request.POST.get('name')
        ch=request.POST.get('check')
        if ch in list(word):
            wordict.append(ch)
            count=count-1 
            if len(set(wordict))==len(set(list(word))):
                messages.success(request, 'Congratulation You Guess Right word.🙌')
                return render(request,'game.html',{'name':name,'wl':word,'wordict':wordict,'yes':'yes'})
            return render(request,'game.html',{'name':name,'wl':word,'wordict':wordict,'count':count})
        else:
            count=count-1 
            if count==0:
                messages.success(request, 'Your Moves are over')
                return render(request,'game.html',{'name':name,'wl':word,'wordict':wordict,'count':count,'yes':'yes'})
                        
            return render(request,'game.html',{'name':name,'wl':word,'wordict':wordict,'count':count})

        
    else:
        return redirect('/')



