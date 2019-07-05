from django.shortcuts import render
from django.http import HttpResponse
from heapq import *
import re
from django.views.decorators.csrf import csrf_exempt
import json


def api_doc_view(request,*args,**kwargs):
	return render(request,"djikstra/api_doc.html")


def api_view(request):

	inp_path=request.GET['path']
	startp=request.GET['start']
	endp=request.GET['end']
	
	if inp_path==None or endp==None or startp==None:
		response = json.dumps([{'Error':True}])
		return HttpResponse(response, content_type='text/json')

	
	inp_path=inp_path.split( )
	len_inp=len(inp_path)


	if len_inp%3 != 0 :
		response = json.dumps([{'Error':True}])
		return HttpResponse(response, content_type='text/json')

	for i in range(len_inp):
		inp_path[i]=inp_path[i].upper()

	startp=startp.upper().strip()
	endp=endp.upper().strip()
	

	#--------------------Convert graph to integer vertices--------

	place_id = dict()
	id_place = dict()
	new_inp = []

	id=0
	i=0

	for x in inp_path:
		i=i+1
		if i%3==0:
			if x.isdigit():
				new_inp.append(int(x))
			else:
				response = json.dumps([{'Error':True}])
				return HttpResponse(response, content_type='text/json')
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
		response = json.dumps([{'Error': False, 'Found': False }])
		return HttpResponse(response, content_type='text/json')
		

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

	

	if d[place_id[endp]] == I:
		response = json.dumps([{'Error':False , 'Found':False }])
		return HttpResponse(response, content_type='text/json')

	else:
		x, y = place_id[endp], []
		while x != -1:
			y += [id_place[x] ]
			x = p[x]
		y.reverse()
		
	response = json.dumps([{
		'Error'		: False , 
		'Found'		: True  ,
		'Length'	: d[place_id[endp]],
		'Start'		: startp,
		'End'		: endp,
		'Path'		: y,
		}
	])
	return HttpResponse(response, content_type='text/json')