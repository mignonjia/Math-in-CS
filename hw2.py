import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image
from numpy import linalg

def judge(k):
    if (k==1 or k==2 or k==4 or k==16):
        return 1
    return 0

def restore1(u, sigma, v, k):
    m = len(u)
    n = len(v)
    a = np.zeros((m, n))
    a = np.dot(u[:, :k], np.diag(sigma[:k])).dot(v[:k, :])
    a[a < 0] = 0
    a[a > 255] = 255
    return np.rint(a).astype('uint8')

if __name__ == '__main__':
	#filename = 'panda.jpg'
	#inputimg = Image.open(filename)	
	#npimg = np.array(inputimg,dtype=np.int16)
	
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    A = Image.open('dog.jpg')
    a = np.array(A)	
    u_r, sigma_r, v_r = np.linalg.svd(a[:, :, 0])
    u_g, sigma_g, v_g = np.linalg.svd(a[:, :, 1])
    u_b, sigma_b, v_b = np.linalg.svd(a[:, :, 2])
    plt.figure(facecolor = 'w', figsize = (10, 10))
    K = 4
    cnt = 1
    norm = np.sqrt(np.sum(a**2))
    for i in range(K):
        if i == 3:
            i += 1
        k = pow(2,i)
        if i == 4:
            i -= 1
        R = restore1(u_r, sigma_r, v_r, k)
        G = restore1(u_g, sigma_g, v_g, k)
        B = restore1(u_b, sigma_b, v_b, k)
        I = np.stack((R, G, B), axis = 2)
        u,sigma,v = np.linalg.svd(R)
        #print(normI)
        normI = np.sqrt(np.sum(I**2))
        perc=float(normI)/float(norm)
        print(perc)
        plt.subplot(4, 4, i+5)
        plt.imshow(R)
        plt.subplot(4, 4, i+9)
        plt.imshow(G)
        plt.subplot(4, 4, i+13)
        plt.imshow(B)
        plt.subplot(4, 4, i+1)
        plt.imshow(I)
        plt.axis('off')
        plt.title(u'vec_num:%d' %  k)
        cnt += 1
        
    plt.suptitle(u'SVD', fontsize = 20)
    #plt.tight_layout(0.1, rect = (0, 0, 1, 0.92))
    plt.show()
    





