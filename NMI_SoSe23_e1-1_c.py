#https://www.onlinegdb.com/online_python_compiler
#https://onlinegdb.com/SylhlnTFN
from math import log

#Konstanten
a = 10
n_max = 20

#untere Schranke
m_n = lambda n: 1/((n+1)*(a+1))

#obere Schranke
M_n = lambda n: 1/((n+1)*a)

#\mathtt{}
mathtt = lambda f: "\\mathtt{}{:+.5e}{}".format("{", f, "}")

#Rekursion
def I_n(n):
  if n > 0:
    return (1/n) - a * I_n(n-1)
  else:
    return log((a+1)/a)

#Ausgabe Bildschirm
print(" n       m_n     \u2264      I_n     \u2264      M_n")
print("----------------------------------------------")
for i in range(n_max + 1):
  print("{:2d}  {: .5e}   {: .5e}   {: .5e}".format(i, m_n(i), I_n(i), M_n(i)))

#Ausgabe LaTeX
print("")
print("\\begin{array}[t]{ c | c c c c c}")
print("n & m_n & \\leq & I_n & \\leq & M_n\\\\\\hline")
for i in range(n_max + 1):
  print("{:2d} & {} &   & {} &   & {} \\\\".format(i, mathtt(m_n(i)), mathtt(I_n(i)), mathtt(M_n(i))))
print("\\end{array}")
