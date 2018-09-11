#Exercicio 1

import numpy as np
M = np.arange(1,16).reshape((3,5)).T
print(M)

import numpy as np
D = np.array([[2,7,12],[4,9,14]]).reshape((2,3)).T
print(D)

import numpy as np
A = np.arange(10,49)
print(A)

import numpy as np
B = np.arange(0,39)
print(B)

import numpy as np
C = np.arange(0,20)
print(C)

import numpy as np
M2 = np.arange(0,9).reshape((3,3)).T
print(M2)

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0.0, 2.0, 0.01)
y = np.sin(2*np.pi*x)

plt.plot(x,y)
plt.title('Gráfico do Seno (Senoidal)',fontsize=20)

         
plt.xlabel('x')
plt.ylabel('y')
plt.show()
