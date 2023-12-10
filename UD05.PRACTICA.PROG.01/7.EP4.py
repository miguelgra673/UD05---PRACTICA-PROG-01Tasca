# Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, 
# y sabiendo que:

total_preguntas = int(input("Ingrese la cantidad total de preguntas: "))
correctas = int(input("Ingrese la cantidad de preguntas contestadas correctamente: "))

porcentaje_correctas = (correctas / total_preguntas) * 100

if porcentaje_correctas >= 90:
    nivel = "Excelente"
elif 75 <= porcentaje_correctas < 90:
    nivel = "Bueno"
elif 50 <= porcentaje_correctas < 75:
    nivel = "Regular"
else:
    nivel = "Insuficiente"

print(f"\nPorcentaje de respuestas correctas: {porcentaje_correctas:.2f}%")
print(f"Nivel del postulante: {nivel}")
