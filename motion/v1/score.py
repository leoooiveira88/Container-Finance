# Synthesized score + SFX on the beat grid (120 BPM, offset 0.3s). Seeded noise only.
import numpy as np, json, wave
SR=48000; DUR=60.0; N=int(SR*DUR)
rng=np.random.default_rng(13)
b=lambda n:0.3+0.5*n
out=np.zeros((N,2))
def add(sig,t,gain=1.0,pan=0.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if i>=N: return
    s=sig[:j-i]*gain; out[i:j,0]+=s*(1-pan)/1; out[i:j,1]+=s*(1+pan)/1
def env(n,a,d):
    e=np.ones(n); A=int(a*SR); e[:A]=np.linspace(0,1,A) if A>0 else 1
    e*=np.exp(-np.arange(n)/(d*SR)); return e
def kick(g=1.0):
    n=int(.35*SR); t=np.arange(n)/SR; f=50+90*np.exp(-t*30)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.001,.12)*g
def thump(): # big impact
    n=int(.9*SR); t=np.arange(n)/SR; f=42+120*np.exp(-t*18)
    body=np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.001,.28)
    nz=rng.standard_normal(n)*env(n,.001,.03)*.35
    return body+nz
def tick(f=2400,g=.25):
    n=int(.04*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*env(n,.0005,.008)*g
def hat(g=.08):
    n=int(.06*SR); x=rng.standard_normal(n); x=np.diff(np.concatenate([[0],x])); return x*env(n,.0005,.012)*g
def whoosh(len_s=.5,g=.35):
    n=int(len_s*SR); x=rng.standard_normal(n)
    # sweep lowpass via moving average with shrinking window
    y=np.zeros(n); acc=0; 
    for k in range(0,n,256):
        w=int(40-36*(k/n)); seg=x[k:k+256]; y[k:k+256]=np.convolve(seg,np.ones(w)/w,'same')
    e=np.sin(np.linspace(0,np.pi,n))**2
    return y*e*g*3
def pad_chord(freqs,len_s,g=.06):
    n=int(len_s*SR); t=np.arange(n)/SR; s=np.zeros(n)
    for f in freqs:
        for h,a in [(1,1),(2,.35),(3,.15),(4,.08)]:
            s+=a*np.sin(2*np.pi*f*h*t+rng.uniform(0,6.28))*(1+.003*np.sin(2*np.pi*.3*t))
    e=np.minimum(1,t/.4)*np.minimum(1,(len_s-t)/.3)
    return s*e*g/len(freqs)
def bass(f,len_s=.45,g=.22):
    n=int(len_s*SR); t=np.arange(n)/SR
    return (np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*2*f*t))*env(n,.004,.18)*g

CH=[(130.81,164.81,196.0),(110.0,130.81,164.81),(87.31,110.0,130.81),(98.0,123.47,146.83)]
ROOT=[65.41,55.0,43.65,49.0]
bar=2.0; t=b(0); k=0
while t<DUR-0.5:
    c=k%4; add(pad_chord(CH[c],bar+.3),t)
    for q in range(4):
        tb=t+q*.5
        if tb>=58.5: break
        quiet = b(47)<=tb<b(54)          # breathe before the key message
        if tb>=b(6) and not quiet: add(kick(.55),tb)
        if not quiet and q in (0,2): add(bass(ROOT[c]),tb)
        if tb>=b(18) and not quiet:
            add(hat(),tb+.25,pan=.3)
    t+=bar; k+=1

hits=[0.2+9*0.085, b(10), b(11)+1.0, b(30), b(34), b(72), b(73), b(97), b(98), b(99), b(109), b(114)]
hits+= [b(48+i) for i in range(4)] + [b(54+i) for i in range(6)]
for h in hits: add(thump(),h,.55)
for i,ch in enumerate('33.469.244'):
    if ch!='.': add(tick(2600,.22),0.2+i*0.085)
for x in np.arange(b(11),b(11)+1.0,.05): add(tick(3200,.12),x)
for i in range(22): add(tick(1800,.12),b(19)+i*.035)
for i in range(0,335,6): add(tick(2200,.06),b(22)+i*.0075,pan=(i%2-.5)*.6)
scenes=[b(6),b(18),b(33),b(47),b(71),b(95)]
for s in scenes: add(whoosh(),s-.3)
# fade out last 1.5s
fo=int(1.5*SR); out[-fo:]*=np.linspace(1,0,fo)[:,None]
out/=np.max(np.abs(out))*1.05
w=wave.open('score_raw.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
json.dump({"bpm":120,"offset":0.3,"beats":[round(b(n),3) for n in range(119)],
  "scenes":{"s1":0,"s2":b(6),"s3":b(18),"s4":b(33),"s5":b(47),"s6":b(71),"s7":b(95)},
  "hits":sorted(round(h,3) for h in hits),
  "vo_slots":{"vo1":[0.0,3.3],"vo2":[3.4,9.3],"vo3":[9.4,16.8],"vo4":[16.9,23.8],"vo5":[24.0,35.8],"vo6":[36.0,47.8],"vo7":[48.2,53.0]}},open('beats.json','w'),indent=1)
print('ok')
