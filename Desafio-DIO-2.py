#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo (soma de todos os lados) e apresente a mensagem:
#Perimetro = XX.X
#Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:
#Area = XX.X
#Fórmula da área de um trapézio: AREA = ((A + B) x C) / 2
#Entrada
#A entrada contém três valores reais.
#Saída
#O resultado deve ser apresentado com uma casa decimal.

lados = [float(x) for x in input().split()]

a = lados[0];
b = lados[1];
c = lados[2];

if a + b > c and a + c > b and b + c > a:
  per = a + b + c 
  print(f"Perimetro = {per:.1f}")
else:
  area = ((a + b) *c)/2
  print(f"Area = {area:.1f}")