from django.shortcuts import render
from django.http import HttpResponse
from heapq import *
import re

def sp_input_view(request,*args,**kwargs):
	return render(request,"sp_input.html")



def sp_output_view(request,*args,**kwargs):

	context={
		"error" : 	0,
		"valid" :	1,
		"found"	: 	0,
		"length":	100000,
		"path"	:	[],
		"start" : 	"Delhi",
		"endp"	:	"Mumbai"
	}
	


	system	=	request.POST.get('input',None)
	startp	=	request.POST.get('startp',None)
	endp	=	request.POST.get('endp',None)

	

	if system==None or endp==None or startp==None:
		context['error']=1
		context['valid']=0
		return render(request,"sp_output.html",context)		


	context['path']=system.split( )	
	system=system.split( )
	len_inp=len(system)


	if len_inp%3 != 0 :
		context['valid']=1
		context['error']=1
		return render(request,"sp_output.html",context)		

	for i in range(len_inp):
		system[i]=system[i].upper()

	startp=startp.upper()
	endp=endp.upper()

	context['startp']=startp
	context['endp']=endp

	#--------------------Convert graph to integer vertices--------

	place_id = dict()
	id_place = dict()
	new_inp = []

	id=0
	i=0

	for x in system:
		i=i+1
		if i%3==0:
			if x.isdigit():
				new_inp.append(int(x))
			else:
				context['valid']=0
				return render(request,"sp_output.html",context)			
		else:
			if x in place_id :
				new_inp.append(place_id[x])
				continue
			else:
				place_id[x]=id
				id_place[id]=x
				new_inp.append(id)
				id=id+1

	if startp not in place_id or endp not in place_id:
		context['found']=0
		return render(request,"sp_output.html",context)			
		

	
		

	print(place_id)
	print(startp)
	print(place_id[startp])

	#-------------------------------------------------------------






	#---------------------------Algorithm starts--------------

	I = 1 << 60
 
	n=id
	g = [[] for _ in range(n)]
	d = [0] + [I] * n
	p = [-1] * n
	q = [(0, place_id[startp])]
	d[place_id[startp]]=0
	i=0
	print(q)
	while i<len_inp :
		a, b, w = new_inp[i],new_inp[i+1],new_inp[i+2]
		g[a] += [(w, b)]
		g[b] += [(w, a)]
		i+=3

	while q:
		a = heappop(q)[1]
		print("Heap" + str(a))
		
		for e in g[a]:
			w, b = d[a] + e[0], e[1]
			if w < d[b]:
				d[b], p[b] = w, a
				heappush(q, (d[b], b))

	print(d)
	print(p)

	if d[place_id[endp]] == I:
		return render(request,"sp_output.html",context)

	else:
		x, y = place_id[endp], []
		while x != -1:
			y += [id_place[x] ]
			x = p[x]
		y.reverse()
		context["found"]=1
		context["path"]=y
		context["length"]=d[place_id[endp]]


	# #---------------------Algorithm Ends-----------------------


	return render(request,"sp_output.html",context)