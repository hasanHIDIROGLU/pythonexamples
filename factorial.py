@author hasanHIDIROGLU

fact=lambda x:x and x*fact(x-1) or 1

print(fact(4))
