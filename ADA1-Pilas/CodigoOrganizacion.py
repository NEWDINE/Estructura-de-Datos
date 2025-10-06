class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

PREC = {'neg':4, '√':4, '^':3, '*':2, '/':2, '+':1, '-':1}
ASOC = {'neg':'R', '√':'R', '^':'R', '*':'L', '/':'L', '+':'L', '-':'L'}

def preprocess(expr: str) -> str:
    return expr.replace(" ", "").replace("sqrt", "√")

def tokenizar(expr: str):
    s = preprocess(expr)
    tokens, i = [], 0
    while i < len(s):
        c = s[i]
        if c.isdigit() or c=='.':
            j = i+1
            while j < len(s) and (s[j].isdigit() or s[j]=='.'):
                j += 1
            tokens.append(s[i:j])
            i = j
        elif c in "+-*/^()√":
            tokens.append(c)
            i += 1
        else:
            if c.isalpha():
                j = i+1
                while j < len(s) and s[j].isalnum():
                    j += 1
                tokens.append(s[i:j])
                i = j
            else:
                raise ValueError(f"Carácter no válido: {c}")
    return tokens

def construir_arbol(expr: str) -> Nodo:
    toks = tokenizar(expr)
    valores, ops = [], []

    def aplicar():
        op = ops.pop()
        if op in ('neg', '√'):
            a = valores.pop()
            valores.append(Nodo(op, a, None))
        else:
            b = valores.pop()
            a = valores.pop()
            valores.append(Nodo(op, a, b))

    prev = None 
    for t in toks:
        if t not in PREC and t not in ('(', ')', '√'):
            valores.append(Nodo(t))
            prev = 'num'
        elif t == '(':
            ops.append(t)
            prev = '('
        elif t == ')':
            while ops and ops[-1] != '(':
                aplicar()
            ops.pop()
            prev = 'num'
        else:
            # manejar '-' unario
            if t == '-' and (prev in (None, 'op', '(')):
                t = 'neg'
            # manejar √ como unario
            if t == '√':
                ops.append(t)
                prev = 'op'
                continue
            while ops and ops[-1] in PREC:
                top = ops[-1]
                if (ASOC[t] == 'L' and PREC[t] <= PREC[top]) or \
                   (ASOC[t] == 'R' and PREC[t] <  PREC[top]):
                    aplicar()
                else:
                    break
            ops.append(t)
            prev = 'op'

    while ops:
        aplicar()
    return valores[-1]

def prec_nodo(n: Nodo) -> int:
    return PREC.get(n.valor, -1)

def a_postfija(n: Nodo) -> str:
    if n is None:
        return ""
    if n.valor in ('neg', '√'):
        return f"{a_postfija(n.izq)} {n.valor}"
    if n.valor in PREC:
        if n.valor in ('+', '*'):
            L, R = n.izq, n.der
            if prec_nodo(R) > prec_nodo(L):
                return f"{a_postfija(R)} {a_postfija(L)} {n.valor}"
        return f"{a_postfija(n.izq)} {a_postfija(n.der)} {n.valor}"
    return n.valor

expr = input("Ingrese una expresión en notación infija: ")
arbol = construir_arbol(expr)
print("Postfija:", a_postfija(arbol).strip())
