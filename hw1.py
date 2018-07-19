#!/usr/bin/env python
# coding=utf-8
import numpy as np
from scipy.stats import ortho_group

n=1000
m=100

def get_angle(v1, v2):
    norm1 = np.sqrt(v1.dot(v1))
    norm2 = np.sqrt(v2.dot(v2))
    cos = v1.dot(v2)/(norm1*norm2)
    angle = np.arccos(cos)
    degree = angle*360/2/np.pi
   # print(degree)
    return degree

def reduct():
    vec = ortho_group.rvs(dim=n)
    u = np.random.randn(m, n)
    product = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            #print(vec[i]*u[j])
            product[i,j] = sum(vec[i] * u[j])
    #print(product)
    minangle = 90.0
    allclass = np.zeros(36, dtype = int)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            angle = get_angle(product[i],product[j])
            if angle<minangle:
                minangle = angle
            classangle = int(angle/5)
            allclass[classangle]+=1
    print(allclass)
    print(minangle)

def random_gaussian():
    product = np.random.randn(n, m)
    minangle = 90.0
    allclass = np.zeros(36, dtype = int)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            angle = get_angle(product[i],product[j])
            if angle<minangle:
                minangle = angle
            classangle = int(angle/5)
            allclass[classangle]+=1
    print(allclass)
    print(minangle)

if __name__=='__main__':
    reduct()
    random_gaussian()
