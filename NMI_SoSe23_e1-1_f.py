#https://www.onlinegdb.com/online_python_compiler
#https://www.onlinegdb.com/ryN4rmRKE
from math import log

#Konstanten
a = 10
n_max = 20
N = 27

#untere Schranke
m_n = lambda n: 1/((n+1)*(a+1))

#obere Schranke
M_n = lambda n: 1/((n+1)*a)

#\mathtt{}
mathtt = lambda f: "\\mathtt{}{:+.5e}{}".format("{", f, "}")

#Rekursion
def I_N(n):
  if n < N:
    return (1/(n+1) - I_N(n+1))/a
  else:
    return 1/((N+1)*a)

#Ausgabe Bildschirm
print(" n       m_n     \u2264      I_n     \u2264      M_n")
print("----------------------------------------------")
for i in reversed(range(n_max + 1)):
  print("{:2d}  {: .5e}   {: .5e}   {: .5e}".format(i, m_n(i), I_N(i), M_n(i)))

#Ausgabe LaTeX
print("")
print("\\begin{array}[t]{ c | c c c c c}")
print("n & m_n & \\leq & \\tilde{I}_n & \\leq & M_n\\\\\\hline")
for i in reversed(range(n_max + 1)):
  print("{:2d} & {} &   & {} &   & {} \\\\".format(i, mathtt(m_n(i)), mathtt(I_N(i)), mathtt(M_n(i))))
print("\\end{array}")
