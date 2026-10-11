import numpy as np
from scipy.stats import poisson
L=np.arange(0.05,4.5,0.025); N=len(L); K=12; RHO=-0.05
pm=poisson.pmf(np.arange(K)[None,:],L[:,None])
J=pm[:,None,:,None]*pm[None,:,None,:]
lh=L[:,None]; la=L[None,:]
J[:,:,0,0]*=1-lh*la*RHO; J[:,:,0,1]*=1+lh*RHO; J[:,:,1,0]*=1+la*RHO; J[:,:,1,1]*=1-RHO
J/=J.sum(axis=(2,3),keepdims=True)
i=np.arange(K)[:,None]; j=np.arange(K)[None,:]
H=(J*(i>j)).sum((2,3)); D=(J*(i==j)).sum((2,3)); A=(J*(i<j)).sum((2,3)); O25=(J*((i+j)>2)).sum((2,3))
def fit(pH,pD,pA,pO=None):
    e=(H-pH)**2+(A-pA)**2+0.5*(D-pD)**2
    if pO is not None: e=e+2*(O25-pO)**2
    a,b=np.unravel_index(np.argmin(e),e.shape); return a,b
def grid(a,b): return J[a,b]
def devig(*o):
    v=[1/x for x in o]; s=sum(v); return [x/s for x in v]
