I=99999
V=[0,100,320,330,500,900,0]
P="AIAIASi{i{h9R'Q5EOU_EMAMPkA[9g9UEb1;I>AIAI?g150i*!IS8OI|UL1<UvU32RYfH9MmUM0oIgH]!K15(e9?9?1_AIAG9hIRA!EOI?9AISI):1ISHaE:AJ8w9?9=AIAIAJISISE'AIAH=XAIA5AIAI=EAIAH=XAIA6AJE:@Y9S9=9gAIA!A]EM9TENE9AJENA4ENEM9AE:AG1]=C8u))!I13(a)-0k!#)S))!I1[0k17A!9?9mXuIWYiQ5RM"
D=[0,0,[-21,-19,-12,-8,8,12,19,21],[-11,-9,9,11],[-1,1,-10,10],[-11,-9,9,11,-1,1,-10,10],[-11,-10,-9,-1,1,9,10,11]]
RM=[15]*128
for a,b in((92,13),(99,14),(96,12),(22,7),(29,11),(26,3)):RM[a]=b
PB=0
bd=[15]*128;sd=0;rg=15;ep=0;ks=[96,26]
for i in range(8):t='.pnbrqk'.index('rnbqkbnr'[i]);bd[22+i]=8+t;bd[32+i]=9;bd[82+i]=1;bd[92+i]=t
for i in range(4,8):bd[i*10:i*10+12]=[15,15]+[0]*8+[15,15]
T=[[0]*128 for _ in range(7)]
for j in range(384):
 k=2*(j//3);n=(ord(P[k])-33)*94+ord(P[k+1])-33
 i=j%64;T[1+j//64][i+2*(i//8)+22]=5*((n//361,n//19%19,n%19)[j%3]-8)
def att(b,s):
 f=20*b-10;g=b*8
 if bd[s-f+1]==g+1 or bd[s-f-1]==g+1:return 1
 for p in(2,6):
  for d in D[p]:
   if bd[s+d]==g+p:return 1
 for p in(3,4):
  for d in D[p]:
   t=s+d
   while(v:=bd[t])<15:
    if v in(g+p,g+5):return 1
    if v:break
    t+=d
 return 0
def make(m):
 global sd,rg,ep
 fr=m&127;to=m>>7&127;f=m>>14;o=sd;pc=bd[fr];cap=bd[to];e=ep;R=rg
 bd[fr]=0;sd^=1;rg=R&RM[fr]&RM[to];ep=0
 if pc&7==6:ks[o]=to
 if pc&7==1 and not cap and to==e:bd[to+10-20*o]=0
 if f==1:ep=(fr+to)//2
 if f>5:
  a,b=(1,1)if f==6 else(-2,-1)
  bd[to+a]=0;bd[fr+b]=o*8+4;bd[to]=o*8+6
 elif 1<f<6:bd[to]=o*8+f
 else:bd[to]=pc
 return R,e,cap,pc
def unmake(m,h):
 global sd,rg,ep
 R,e,cap,pc=h;fr=m&127;to=m>>7&127;f=m>>14;bd[fr]=pc;bd[to]=cap;sd^=1;o=sd;rg=R;ep=e
 if pc&7==6:ks[o]=fr
 if f>5:
  a,b=(1,1)if f==6 else(-2,-1)
  bd[to+a]=o*8+4;bd[fr+b]=0
 if pc&7==1 and not cap and to==e:bd[to+10-20*o]=(o^1)*8+1
def gen():
 op=sd^1;f=20*sd-10;st=3+5*(sd==0);pr=2+7*sd;ms=[];k=ks[sd]
 for fr in range(20,100):
  pc=bd[fr]
  if not pc or pc==15 or pc>>3!=sd:continue
  p=pc&7
  if p==1:
   to=fr+f
   if not bd[to]:
    if fr//10==pr:ms+=[fr|to<<7|x<<14 for x in(5,4,3,2)]
    else:
     if fr//10==st and not bd[fr+2*f]:ms.append(fr|fr+2*f<<7|1<<14)
     ms.append(fr|to<<7)
   for d in(f-1,f+1):
    to=fr+d;v=bd[to]
    if v==15:continue
    if v:
     if v>>3==op:ms+=([fr|to<<7|x<<14 for x in(5,4,3,2)]if fr//10==pr else[fr|to<<7])
    elif to==ep:ms.append(fr|to<<7)
  else:
   for d in D[p]:
    to=fr+d;v=bd[to]
    if v==15 or(v and v>>3==sd):continue
    ms.append(fr|to<<7)
    if not v and 2<p<6:
     while 1:
      to+=d;v=bd[to]
      if v==15:break
      if not v:ms.append(fr|to<<7)
      else:
       if v>>3==op:ms.append(fr|to<<7)
       break
 if rg&1<<2*sd and not any(bd[k+x]for x in(1,2))and not any(att(sd,k+x)for x in(0,1,2)):ms.append(k|k+2<<7|6<<14)
 if rg&2<<2*sd and not any(bd[k+x]for x in(-1,-2,-3))and not any(att(sd,k+x)for x in(0,-1,-2)):ms.append(k|k-2<<7|7<<14)
 if len(ms)>1:
  def sc(m):
   v=bd[m>>7&127];ff=m>>14
   return V[v&7]*100-V[bd[m&127]&7]+V[ff]*10*(1<ff<6)+2e6*(m==PB)
  ms.sort(key=sc,reverse=1)
 return ms
def ev():
 s=sum(V[v&7]+T[v&7][(11-i//10)*10+i%10 if v>>3 else i]for i,v in enumerate(bd)if v!=15)
 return s if sd==0 else-s
def ab(d,al,be):
 if not d:return ev()
 ic=att(sd^1,ks[sd]);best=-99999
 for m in gen():
  o=sd;h=make(m)
  if att(o^1,ks[o]):unmake(m,h);continue
  v=-ab(d-1,-be,-al);unmake(m,h)
  if v>best:best=v
  if v>al:al=v
  if al>=be:break
 if best==-99999:return-(30000-d)if ic else 0
 return best
def search(dep):
 global PB
 PB=0
 for d in range(1,dep+1):
  bv=-I;bm=0
  for m in gen():
   o=sd;h=make(m)
   if att(o^1,ks[o]):unmake(m,h);continue
   v=-ab(d-1,-I,I);unmake(m,h)
   if v>bv:bv=v;bm=m
  if bm:PB=bm
 return PB
def uci(m):
 fr=m&127;to=m>>7&127;f=m>>14
 s=chr(fr%10+95)+str(10-fr//10)+chr(to%10+95)+str(10-to//10)
 if 1<f<6:s+='nbrq'[f-2]
 return s
print('bestmove '+uci(search(4)))
