#This is another variation of mylstar.py as it checks each string's presence from the file of acceptable strings
#and groups similar transitions with comma "," while making DFA

#INPUTS

# sys.argv[0]  is   this file name
# sys.argv[1]  is   acceptable stringset file which enlists all the acceptable strings
#sys.argv[2]   is   name to generate dot files




import copy
import sys

def stringlist():		#To read the acceptable list of strings from file
	pnfile = open(sys.argv[1], "r")		#open in reading mode
	data = pnfile.readlines()
	word =[]
	#print(type(data))		#it is list type

	for x in data:
		#print(x)		
		#print(type(x))		#string type
		word.extend(x.split())	#removes spaces and newline characters
	return word
	
def prefix(prelist):
	#prelist.remove('')		#to avoid string prefixes of ''
	newS=copy.deepcopy(prelist)
	for x in prelist:
		y=str(x)
		newS.append(y)		#to have a list of S in strings
		num=len(y)		#length of each string ( of S) 
		for i in range(num):	#to have all prefixes of each value in S
			prefx=""
			for j in range(i):	#to build each prefix
				if y[j] != '':			#looks like this can be removed
					prefx=prefx+y[j]
			newS.append(prefx)		#append the built prefix to list S
	#newS.remove("")				#removes only first occurence of ""
	#newS = list(filter(lambda x: x != "", newS))	#removes all occurrences of ""	
	#newS.append('')				#'' was there but was removed in this function
	newS_set=set(newS)
	return list(newS_set)

def get_cols(Dict):
	return list(Dict[''].keys())		#returns list for column names

def sufix(elist):
	newE=copy.deepcopy(elist)
	for x in elist:
		y=str(x)
		newE.append(y)			#to have a list of S in strings
		num=len(y)			#length of each string ( of S)	 
		for i in range(num,0,-1):	#to have all prefixes of each value in S
			sfx=''
			for j in range(0,i):			#to build each prefix
				sfx=sfx+y[j]
			newE.append(sfx)		#append the built prefix to list S
	#newE.remove("")				#removes only first occurence of ""
	#newE = list(filter(lambda x: x != "", newS))	#removes all occurrences of ""	
	newE.append('')					#'' was there but was removed in this function
	newE_set=set(newE)
	return list(newE_set)

def confirm(yn,Dict2):
	for x in Dict2:
		for y in Dict2[x]:
			if(str(x)+str(y)==str(yn)):
				return str(Dict2[x][y])	#return str type to avoid 0==False which evaluates to true
	return False

def present(tocheck):
	global word
	if tocheck not in strings:
		return str(0)
	else:
		return str(1)

def fillsaub(Dict):
	Dict2 = copy.deepcopy(Dict)
	this_elist=list(Dict[''].keys())		#maintains list for column names
	#this_elist=get_cols(Dict)			#This line is more efficient than above line
	print("Printing this_elist")
	print(this_elist)
	for i in S:
		for x in alp:
			for t in this_elist:		
				m=str(i)+str(x)		#suffix of member of S (i) with each alphabet (x)
				j=str(i)+str(t)+str(x)
				if( m not in list(Dict2.keys())):
					#To add the entry for suffix member m in table Dict for current column t
					cell=confirm(j,Dict2) #to check if the combination is present in record table
					if(cell==False):
						cell=present(j)
						#cell=input("Is \""+j+"\" in your language(0 or 1) ")
					#Dict2[j]={"Flag":"L",'':cell}
					Dict2[j]={t:cell}
				else:
					#To ensure entries for all columns in each row of Dict
					if(t not in list(Dict2[m].keys())):
						cell=confirm(j,Dict2)
						if(cell==False):
							cell=present(j)
							#cell=input("Is \""+j+"\" in your language(0 or 1) ")
						Dict2[m][t]=cell									
	return Dict2

#def complete(fillit):
	#for f in fillit:
		#if f not in Dict:
	
def consistency(Dict):
	S2=copy.deepcopy(S)			#Changes in S2 are not copied to original S. 
						#S and S2 are lists and have Upper table's keys
	for x in S:
		S2.remove(x)			#To remove the selected row while comparing
		for y in S2:
			#print("Dict[x].values and Dict[y].values()")
			#print(str(Dict[x].values()))
			#print(str(Dict[y].values()))
			if(str(Dict[x].values())==str(Dict[y].values())):  #Dict[x] is inner dictionary at x position
							#and its .values() are values inside inner dictionary
				for t in alp:		#to append with each alphabet for each alphabet
					#if(x==''):		#looks like can be commented
					#	element1=t	#looks like can be commented
					#	element2=str(y)+str(t)
					#else:			#looks like can be commented
						#if(y==''):	#looks like can be commented
						#	element1=str(x)+str(t)	#looks like can be commented
						#	element2=t	#looks like can be commented
						#else:
						#	element1=str(x)+str(t)
						#	element2=str(y)+str(t)
					#print(element1+" "+element2)
					#print("Dict[x].values and Dict[y].values()")
					#print(str(Dict[x].values()))
					#print(str(Dict[y].values()))
					element1=str(x)+str(t)
					element2=str(y)+str(t)
					if(str(Dict[element1].values()) != str(Dict[element2].values())):
							#This is consistency cond. check
							
						for z in list(Dict[x].keys()):
							if(str(Dict[element1][z]) != str(Dict[element2][z])):
								ret=str(t)+str(z)
								p={ret:False}
								return p    #Returns failure point i.e. t
							
						
						#return p    #Returns failure point i.e. t					
		S2 = copy.deepcopy(S)		#different element will be removed in next iteration 
						#because same element is not compared everytime 
						#so we need fresh copy of S
	return {"xyz":True}

def closed(Dict):
	Dict2=copy.deepcopy(Dict)		#Changes in Dict2 are not copied to original Dict.
	L = list(Dict2.keys())			#Object type <Dict_keys> converted into list
	state=False				#say it is not closed. Just a counter
	for x in S:
		L.remove(x)			#to have list of lower table's keys
	for x in L:
		for y in S:
			if(Dict2[x]==Dict2[y]):		#closed condition check 
							#(All lower table keys in upper table's keys
				state=True		#This lower tabloe key found in upper table key
		if(state==False):
			return {x:False}
		state=False			#Next iteration key.....therefore, just counter reset
	return {"xyz":True}

def lev1dic2str(dic):			#Returns all the entries from a row as a single comncatenated string
	lval=list(dic.values())
	name=""
	for x in lval:
		name=name+str(x)
	return name
	
def lev1dic2str4keys(dic):		#Returns all the keys of dictinoary as a single concatenated string
	lval=list(dic.keys())
	name=""
	for x in lval:
		name=name+str(x)
	return name


def simplify(tran):
	tran2=copy.deepcopy(tran)
	tran3=copy.deepcopy(tran)
	donemark=[]				#To mark if already included with comma
	for i in tran3:				
		tran2.remove(i)
		for x in tran2:			#For comparision with all remaining 
			if((str(i[0])==str(x[0])) and (str(i[2])==str(x[2])) and (x not in donemark)):	
			#If transitions start from same state and end on same state and are not included yet
				i[1]=str(i[1])+","+str(x[1])		#append with comma in single transition
				donemark.append(x)			#Kind of flag to mark that it is visited
				tran3.remove(x)				#To avoid duplicacy as next i
#Can not be achieved like removing x from tran2 at the same time as it skips iterations (as we would be iterating over changing list)(can be considered aspython's flaw).. Therefore, donemark[] named flag is used
	return tran3


def publish(start,tran,final):
	
	#statedata1 = """digraph M{\nrankdir=LR;\nnode [shape=doublecircle];"""+str(final)+""" ;\nx [shape=none, label=""];\nnode [shape=circle];\n"""
	#this above statement is when there is only 1 final state
	
	
	# Template for creating States	
	statedata1 = """digraph M{\nrankdir=LR;\nnode [shape=doublecircle];"""
	statedata2=""
	flag=0
	for i in final:
		statedata2=statedata2+i+" "
		flag=flag+1
	if(flag):
		statedata3=""";\nx [shape=none, label=""];\nnode [shape=circle];\n"""
	else:
		statedata3="""\nx [shape=none, label=""];\nnode [shape=circle];\n"""
	global fcount
	fcount=fcount+1
	pnfile = open(sys.argv[2]+str(fcount)+".dot", "w")		#To create a dot file for printing
	pnfile.write(statedata1+statedata2+statedata3)
	pnfile.write("x->"+str(start)+";\n")
	tran_print=simplify(tran)
	for i in tran_print:
		pnfile.write(str(i[0])+"->"+str(i[2])+""" [label=" """+str(i[1])+""" "];\n""")
	
	pnfile.write("}")
	pnfile.close()

def makeDfa():
	print("making DFA")
	state=[]
	for x in (Dict.values()):				#each x is also dictionary
		state.append(list(x.values()))			#<Dict_values> objects are created
								#by values() function
								#append appends list as an item
								#rather than all list items as list items
	name=" "
	for x in state:					#these are value rows like [1,0] for {ep:{ep:1,0:0}}
		for y in x:				#for each value in value rows
			name=name+str(y)		#Making rows as string i.e. " 10" for above
		name=name+" "
	state=name.split()			#splits string into list across space " "
	stateset=set(state)					
	
	name=lev1dic2str(Dict[''])
	if(name not in stateset):
		print("No such state found error")
	else:
		start_state=name		#start state is Dict[ep] but as string
			
	tran_list=[]				#Transitions in form (from_state, move, to_state)
	final_state=[]
	for i in S:
		curr_state=lev1dic2str(Dict[i])
		for a in alp:
			if(i != ''):			#looks like can be commented
				ele=str(i+a)	
			else:				#looks like can be commented
				ele=str(a)		#looks like can be commented
			next_state=lev1dic2str(Dict[ele])
								#Building final state
			if((curr_state[0]=='1') and (curr_state not in final_state)):
				final_state.append(curr_state)
			if((next_state[0]=='1') and (next_state not in final_state)):
				final_state.append(next_state)
			if [curr_state,a,next_state] not in tran_list:
				tran_list.append([curr_state,a,next_state])
	#final_state=name
	#tran_len=len(tran_list)
	#for i in range tran_len:
	
	print("Start state/s: "+start_state)	### DONT REMOVE
	print("DFA: ")
	print(tran_list)			### DONT REMOVE
	print("Final state/s: ")
	print(final_state)	### DONT REMOVE	
	publish(start_state,tran_list,final_state)
	
def addcolumn(col_str):
	#global elist
	#elist.append=col_str
	dlen=len(Dict)
	for x in Dict:					#inserts values for all the existing members in Dict
		if x=='':				#looks like can be commented
			askfor=col_str			#looks like can be commented
		else:					#looks like can be commented
			askfor=str(x)+str(col_str)
		cell=confirm(askfor,Dict)
		if(cell==False):
			cell = present(askfor)
			#cell=input("Is \""+askfor+"\" in your language(0 or 1) ")
		Dict[x][col_str]=cell
	return Dict	

def algo(Dict,S):
	listOfGlobals = globals()   #To refer global variables via list as listOfGlobals[]
	Dict=fillsaub(Dict)      #complete lower part of table i.e. S.A i.e. 
				#upper half elemets, each followed with each alphabe
	listOfGlobals["Dict"] = Dict		#To update global Dict also
	
	global count			#count will always refer to global count
	count=count+1		#to keep record of algo() calls. 
	
	print("Printing Dict and S at start of algo")
	print(Dict)
	print(S)
	consistency_result = consistency(Dict)    #Check consistency
	
	if True in consistency_result.values():		#It was consistent
		print("consistent")
		closed_result=closed(Dict)		# Check if table is closed
		
		if True in closed_result.values():			#Closed
			print("Closed")
			makeDfa()
			res=input("Is this correct DFA representation (1 or 0) ")
			print(res)
			if res=="0" or res==0:
				counter_example=input("Give counter example string ")
				cell=present(counter_example)
				#cell=input("Is \""+counter_example+"\" in your language(0 or 1) ")
				Dict[counter_example]={'':cell}
				S.append(counter_example)
				S=prefix(S)
				listOfGlobals["Dict"] = Dict		#To update global Dict also
				listOfGlobals["S"] = S
				
				print("PASS"+str(count))
				algo(Dict,S)
		else:
			print("not closed")
			S.extend(list(closed_result.keys()))     #extend appends all list items as list items
								#rather than list being appended as an item
			#print(S)
			S=prefix(S)
			listOfGlobals["S"] = S		#To update global S also
			#print(S)
			
			print("PASS"+str(count))
			algo(Dict,S)
	else:
		print("not consistent")
		kval=lev1dic2str4keys(consistency_result)	#dictionary in form {t:False} is returned
		
		Dict=addcolumn(kval)			#send column to be added in string
		elst=get_cols(Dict)			#get all current column names as list
		elst=sufix(elst)		
		listOfGlobals["Dict"] = Dict
		listOfGlobals["elist"] = elst
		
		print("PASS"+str(count))
		algo(Dict,S)

#BEGINS HERE
strings = stringlist()
fcount=0		#fcount is file count and scount is statecount in DFA
#To input alphabets as list type.
alp = input("Enter the alphabets ").split()
epin = input("Is epsilon accepted in your language (0 or 1) ")
Dict = { '': {'':epin}}
S=['']     #S is the upper half of the table i.e. prefix complete
elist=['']

count=1
algo(Dict,S)		#Starts recursive call to algorithm

print(Dict)
print(S)
