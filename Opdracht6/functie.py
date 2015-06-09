from lorenz import Lorenz
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = Lorenz([-1,1,0])
u1 = A.solve(50,.01)
B = Lorenz([-1.001,1.001,0.001])
u2 = B.solve(50,.01)


print('---------------------------------------------------------------')
print('',u1,'\n',u2)
print('---------------------------------------------------------------')
print(u1[0][0],u2[0][0])
print(u1[-1][0],u2[-1][0])



fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
plt.plot(u1[:,0],u1[:,1],u1[:,2]) 
plt.plot(u2[:,0],u2[:,1],u2[:,2])
plt.show()