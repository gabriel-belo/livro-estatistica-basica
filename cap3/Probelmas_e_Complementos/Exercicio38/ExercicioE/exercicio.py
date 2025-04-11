import numpy as np

estatistica= np.array([9, 9, 8, 8, 9, 10, 8, 8, 9, 8, 10, 7, 7, 9, 9, 7, 8, 9, 4, 7, 7, 8, 10, 9, 9])
media_estatistica= np.mean(estatistica)

dp_estatistica= round(np.std(estatistica),2)

Z_estatistica= np.array([(estatistica - media_estatistica)/ dp_estatistica])

direito=np.array([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])
media_direito= 9

dp_direito= 0

Z_direito= 0

politica= np.array([9.0, 6.5, 9.0, 6.0, 6.5, 6.5, 9.0, 6.0, 10.0, 9.0, 10.0, 6.5, 6.0, 10.0, 10.0, 9.0,
                    10.0, 6.0, 6.0, 6.0, 6.5, 6.0, 9.0, 6.5, 9.0])

media_politica= np.mean(politica)

dp_politica= np.std(politica)

Z_politica= np.array([(politica - media_politica)/ dp_politica])


print(Z_estatistica, Z_direito, Z_direito)
