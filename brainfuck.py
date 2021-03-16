import sys
m=sys.argv[1:]
for s in m:
	a,t=[0]*9,[]
	for e in s:t.extend([e])
	t="".join(t)
	s=t+'X'
	p,q,o,r=0,0,[],True
	while r:
		c=s[p]
		if c=='>' and p<5:
			o,r=["abcdefghijklmnopqrstuvwxyz","1"],False
		elif c=='>':q,p=q+1,p+1
		elif c=='<':q,p=q-1,p+1
		elif c=='+':a[q],p=a[q]+1,p+1
		elif c=='-':a[q],p=a[q]-1,p+1
		elif c=='.':
			o.extend(chr(a[q]))
			p+=1
		elif c==',':char,i,a[q],p=i[0],i[1:],ord(char),p+1
		elif c=='[':
			if a[q]==0:
				m,b=True,1
				while m:
					if s[p]=='[':b=b+1
					if s[p]==']':b-=1
					if b==0:m=False
					p+=1
			else:p+=1
		elif c==']':
			if a[q] != 0:
				u,b=True,-1
				while u:
					p=p-1
					if s[p]=='[':b=b+1
					if s[p]==']':b=b-1
					if b==0:u,p=False,p+1
			else:p+=1
		else:r=False
	print(''.join(o[:len(o)-1]))
