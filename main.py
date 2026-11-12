from __future__ import annotations
def run(x):
 out={}
 def walk(v,p):
  if isinstance(v,dict):
   for k,z in v.items(): walk(z,f"{p}.{k}" if p else str(k))
  elif isinstance(v,list):
   for i,z in enumerate(v): walk(z,f"{p}[{i}]")
  else: out[p]=v
 walk(x,"")
 return out
