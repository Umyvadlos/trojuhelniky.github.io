from math import sqrt, fabs, isclose

print("Zadej první trojuhelnik")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

print("Zadej druhy trojuhelnik")
x4 = float(input("x1: "))
y4 = float(input("y1: "))
x5 = float(input("x2: "))
y5 = float(input("y2: "))
x6 = float(input("x3: "))
y6 = float(input("y3: "))

print("Souradnice prvniho trojuhelniku jsou:", x1, y1, x2, y2, x3, y3)
print("Souradnice druheho trojuhelniku jsou:", x4, y4, x5, y5, x6, y6)



a = fabs(x1 - x2) # absolutní hodnota = fabs
b = fabs(y1 - y2)
a1 = fabs(x2 - x3)
b1 = fabs(y2 - y3)
a2 = fabs(x3 - x1)
b2 = fabs(y3 - y1)

a3 = fabs(x4 - x5)
b3 = fabs(y4 - y5)
a4 = fabs(x5 - x6)
b4 = fabs(y5 - y6)
a5 = fabs(x6 - x4)
b5 = fabs(y6 - y4)


s = sqrt(a*a + b*b)

s1 = sqrt(a1*a1 + b1*b1)

s2 = sqrt(a2*a2 + b2*b2)

print(s, s1, s2)

t = sqrt(a3*a3 + b3*b3)

t1 = sqrt(a4*a4 + b4*b4)

t2 = sqrt(a5*a5 + b5*b5)

print(t, t1, t2)

ot1 = s + s1 + s2

ot2 = t + t1 + t2

print(ot1, ot2)
 




#isclose(s, t) and isclose(s1, t1) and isclose(s2, t2):
    #print("trojuhelniky mají stejny obvod a jsou shodny")

#rovnostranny
if isclose(s, s1) and isclose(s1, s2) and isclose(t, t1) and isclose(t1, t2) and isclose(ot1, ot2):
    print(" trojuhelniky jsou shodne(rovnostranny).")

#rovnoramenny
#if isclose(s, s1) and s1 != s2 or isclose(s, s1) and s2 != s or isclose(s, s1) and s2 != s1 or isclose(t, t1) and t1 != t2 or isclose(t1, t2) and t2!= t or isclose(t, t2) and t2 != t1 and isclose(ot1, ot2):
    #print("trojuhelniky jsou shodne(rovnoramenny).")


if isclose(s, s1) and s1 != s2 and isclose(ot1, ot2) or isclose(s1, s2) and s2 != s and isclose(ot1, ot2) or isclose(s, s2) and s2 != s1 and isclose(t, t1) and t1 != t2 and isclose(ot1, ot2) or isclose(t1, t2) and t2 != t and isclose(ot1, ot2) or isclose(t, t2) and t2 != t1 and isclose(ot1, ot2):
    print("trojuhelniky jsou shodne(rovnoramenny).")


#obecny a obvody
if s != s1 != s2 and t != t1 != t2 and isclose(ot1, ot2):
    print("trojuhelniky nejsou shodne ale maji stejny obvod")
elif s + s1 > s2 and s2 < s1 + s and ot1 < ot2 and t + t1 > t2 and t2 < t1 + t and ot1 < ot2:
    print("trojuhelnik 2 ma vetsi obvod")
elif s + s1 > s2 and s2 < s1 + s and ot1 > ot2 and t + t1 > t2 and t2 < t1 + t and ot1 > ot2:
    print("trojuhelnik 1 ma vetsi obvod")


#if s + s1 > s2 and s2 < s1 + s and ot1 < ot2 and t + t1 > t2 and t2 < t1 + t and ot1 < ot2:
  #  print("trojuhelnik 2 ma vetsi obvod")

#if s + s1 > s2 and s2 < s1 + s and ot1 > ot2 and t + t1 > t2 and t2 < t1 + t and ot1 > ot2:
#    print("trojuhelnik 1 ma vetsi obvod")

#je toto trojuhelnik ?
if s + s1 > s2 and s2 + s1 > s and s2 + s > s1 and t + t1 > t2 and t2 + t1 > t and t2 + t > t1:
    print("ano, toto je trojuhelnik")
else:
    print("toto neni trojuhelnik")


#s + s2 == s1 and s + s1 == s2 and s1 + s2 == s:











#else: print("toto neni trojuhelnik")

#jsou shodne   hotovo
#nejsou shodne ale maji stejny obvod   ¨Hotovo
# Trojuhelnik 2 ma vesti obvod Hotovo
# trojuhelnik 1 ma vetsi obvod Hotovo
# netvori trojuhelnik Hotovo






