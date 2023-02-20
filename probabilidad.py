from modelo import modelo

def imp (var, prob):
    print(f"Para el caso en que la lluvia sea {var[0]}, haya mantenimiento? {var[1]}, el estado del bus sea {var[2]} y la cita sea {var[3]}.")
    print(f"La probabilidad es {prob}")

# Calculemos la probabilidad para una observacion dada
var0 = ["ninguna", "no", "a tiempo", "atendida"]
probabilidad = modelo.probability([var0])

var1 = ["suave", "no", "retrasado", "atendida"]
prob1 = modelo.probability([var1])

var2 = ["fuerte", "si", "retrasado", "atendida"]
prob2 = modelo.probability([var2])

var3 = ["ninguna", "no", "a tiempo", "atendida"]
prob3 = modelo.probability([var3])

imp (var1, prob1)
imp (var2, prob2)
imp (var3, prob3)