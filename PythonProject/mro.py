class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class E(B):
    def show(self):
        print("E")


class D(B):  # Multiple Inheritance
    pass

class F(C):
    pass

class G(C):
    pass


class I:
    pass
class H(I):
    pass
class J(I):
    pass

class K(D,E,F,G,I,H,J):
    pass
k = K()
print(K.mro())
