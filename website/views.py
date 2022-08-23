from django.shortcuts import render

def home(request):
	return render(request, 'home.html',{})

def sumar(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		respuesta = request.POST['respuesta'] 
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Manejo de errores si no se llena la respuesta
		if not respuesta:
			mi_respuesta = "Hola. Has olvidado introducir tu respuesta"
			color ="warning"
			return render(request, 'dividir.html',{
			'respuesta':respuesta,
			'mi_respuesta':mi_respuesta,
			'num_1': num_1,
			'num_2': num_2,
			'color':color,
			})
		
		respuesta_correcta = int(old_num_1) + int(old_num_2)
		if int(respuesta) == respuesta_correcta:
			mi_respuesta ="Correcto: " + old_num_1 + " + " + old_num_2 + " = " + respuesta
			color ="success"
		else:
			mi_respuesta ="Incorrecto: " + old_num_1 + " + " + old_num_2 + " es " + str(respuesta_correcta)+ " ---- NO " + respuesta 
			color ="danger"


		return render(request, 'sumar.html',{
			'respuesta':respuesta,
			'mi_respuesta':mi_respuesta,
			'num_1': num_1,
			'num_2': num_2,
			'color':color,
			})
	return render(request, 'sumar.html',{
		'num_1': num_1,
		'num_2': num_2,
		})


def restar(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		respuesta = request.POST['respuesta'] 
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Manejo de errores si no se llena la respuesta
		if not respuesta:
			mi_respuesta = "Hola. Has olvidado introducir tu respuesta"
			color ="warning"
			return render(request, 'dividir.html',{
			'respuesta':respuesta,
			'mi_respuesta':mi_respuesta,
			'num_1': num_1,
			'num_2': num_2,
			'color':color,
			})

		respuesta_correcta = int(old_num_1) - int(old_num_2)
		if int(respuesta) == respuesta_correcta:
			mi_respuesta ="Correcto: " + old_num_1 + " - " + old_num_2 + " = " + respuesta
			color ="success"
		else:
			mi_respuesta ="Incorrecto: " + old_num_1 + " - " + old_num_2 + " es " + str(respuesta_correcta)+ " ---- NO " + respuesta 
			color ="danger"


		return render(request, 'restar.html',{
			'respuesta':respuesta,
			'mi_respuesta':mi_respuesta,
			'num_1': num_1,
			'num_2': num_2,
			'color':color,
			})
	return render(request, 'restar.html',{
		'num_1': num_1,
		'num_2': num_2,
		})

def multiplicar(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		respuesta = request.POST['respuesta'] 
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Manejo de errores si no se llena la respuesta
		if not respuesta:
			mi_respuesta = "Hola. Has olvidado introducir tu respuesta"
			color ="warning"
			return render(request, 'dividir.html',{
			'respuesta':respuesta,
			'mi_respuesta':mi_respuesta,
			'num_1': num_1,
			'num_2': num_2,
			'color':color,
			})

		respuesta_correcta = int(old_num_1) * int(old_num_2)
		if int(respuesta) == respuesta_correcta:
			mi_respuesta ="Correcto: " + old_num_1 + " x " + old_num_2 + " = " + respuesta
			color ="success"
		else:
			mi_respuesta ="Incorrecto: " + old_num_1 + " x " + old_num_2 + " es " + str(respuesta_correcta)+ " ---- NO " + respuesta 
			color ="danger"


		return render(request, 'multiplicar.html',{
			'respuesta':respuesta,
			'mi_respuesta':mi_respuesta,
			'num_1': num_1,
			'num_2': num_2,
			'color':color,
			})
	return render(request, 'multiplicar.html',{
		'num_1': num_1,
		'num_2': num_2,
		})

def dividir(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(1,10)

	if request.method == "POST":
		respuesta = request.POST['respuesta'] 
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Manejo de errores si no se llena la respuesta
		if not respuesta:
			mi_respuesta = "Hola. Has olvidado introducir tu respuesta"
			color ="warning"
			return render(request, 'dividir.html',{
			'respuesta':respuesta,
			'mi_respuesta':mi_respuesta,
			'num_1': num_1,
			'num_2': num_2,
			'color':color,
			})

		respuesta_correcta = int(old_num_1) / int(old_num_2)
		if float(respuesta) == respuesta_correcta:
			mi_respuesta ="Correcto: " + old_num_1 + " / " + old_num_2 + " = " + respuesta
			color ="success"
		else:
			mi_respuesta ="Incorrecto: " + old_num_1 + " / " + old_num_2 + " es " + str(respuesta_correcta)+ " ---- NO " + respuesta 
			color ="danger"


		return render(request, 'dividir.html',{
			'respuesta':respuesta,
			'mi_respuesta':mi_respuesta,
			'num_1': num_1,
			'num_2': num_2,
			'color':color,
			})
	return render(request, 'dividir.html',{
		'num_1': num_1,
		'num_2': num_2,
		})