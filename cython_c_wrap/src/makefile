# 2.8.3.2. Numpy Support, 2.8.3. Ctypes, http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id6
m.PHONY : clean

libcos_doubles_ctypes.so : cos_doubles_ctypes.o
	gcc -shared -Wl,-soname,libcos_doubles_ctypes.so -o libcos_doubles_ctypes.so cos_doubles_ctypes.o

cos_doubles_ctypes.o : cos_doubles_ctypes.c
	gcc -c -fPIC cos_doubles_ctypes.c -o cos_doubles_ctypes.o

clean :
	-rm -vf libcos_doubles_ctypes.so cos_doubles_ctypes.o cos_doubles_ctypes.pyc
