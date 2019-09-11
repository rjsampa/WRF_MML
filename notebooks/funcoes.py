import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import rasterio as rio

#plota grades do dom 2 e 3 
def plot_t2(imagem, d):                       # d = 2 dominio 3 , 3 dominio 3
    plt.figure(figsize=(14,12))
    plt.imshow(imagem,cmap='jet',)
    if d == 2:
        plt.xticks(np.linspace(0,14,6),(-43.80, -43.66, -43.53, -43.40, -43.26,-43.13),fontsize = 16)
        plt.yticks(np.linspace(0,12,6),(-22.6,-22.7,-22.8,-22.9, -23.0, -23.1), fontsize = 16)
    if d == 3:
        plt.xticks(np.linspace(0,70,6),(-43.80, -43.66, -43.53, -43.40, -43.26,-43.13),fontsize = 16)
        plt.yticks(np.linspace(0,60,6),(-22.6,-22.7,-22.8,-22.9, -23.0, -23.1), fontsize = 16)

    #plt.colorbar(shrink=0.8).set_label(label='Temperatura K',size=15,weight='bold')

    b = plt.colorbar(shrink=0.8)
    b.set_label(label='Temperatura K',size=15,weight='bold')

    for l in b.ax.yaxis.get_ticklabels():
        l.set_family("Times New Roman")
        l.set_size(14)

        
# cria a grade                                 # d = idem func anterior 
def opengrad(arquiv, d=3):
    grid = np.loadtxt(arquiv)
    if d == 2: 
        imagem = grid.reshape(13,15)   # dim 15 x 13
    if d == 3:
        imagem = grid.reshape(61,71)   # 61 x 71
    imagem = np.rot90(imagem,2)
    imagem = np.flip(imagem,1)
    return imagem
 

# redimensiona dominio de array a para d subdivisoes da celula
def dimen(a,d):     
    l = len(a[0])*d
    ar = np.zeros(l)
    for i in range(len(a)):
        L = np.repeat(a[i],d)
        for x in range(d):
            ar = np.vstack((ar,L))#np.concatenate((ar,L))
    return ar[1:]
