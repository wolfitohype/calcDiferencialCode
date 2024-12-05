
#GONZALEZ MAR CESAR JESUS - 1 SEMESTRE GRUPO "G"
import math

totalPpl = int(input("Introduce el numero total de personas: "))

totalFila = totalPpl / 10;
leftSeats = math.trunc(totalFila / 2);
rightSeats = math.trunc(totalFila - leftSeats);
paradosHalf1 = totalFila - (leftSeats+rightSeats);

if paradosHalf1 > math.trunc(totalFila)- (leftSeats+rightSeats):
    paradosHalf1 = math.trunc(paradosHalf1)+1;

#print(totalFila, leftSeats, rightSeats, paradosHalf1);
print(f"Personas por fila: {totalFila}");
print(f"Columna 1: Asientos por fila: {leftSeats}");
print(f"Columna 2: Asientos por fila: {rightSeats}");

costados = totalPpl - (totalFila*5) + paradosHalf1;
leftSide = math.trunc(costados / 3);
rightSide = math.trunc(costados / 3);
backSide = math.trunc(costados - leftSide - rightSide);

print(f"Personas en el costado Izquierdo: {leftSide}");
print(f"Personas en el costado Derecho: {rightSide}");
print(f"Personas en la parte Posterior: {backSide}");
#print(costados, leftSide, rightSide, backSide);

print(f"\tMAÑANERA")
for i in range (5):
    print(f"\t{leftSeats}\t{rightSeats}")
print(f"Costado\t\tParte\t\tCostado")
print(f"Izquierdo\tPosterior\tDerecho")
print(f"{leftSide}\t\t\t{backSide}\t\t\t{rightSide}")
