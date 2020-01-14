class Jugador():
	def __init__(self):
		self.jugadores = ["Lux", "Batalla", "Fucks", "Nacho", "Ascacibar","Alario", "Driussi", "Benedetto"]
		self.puestos = ["a", "a", "a", "v", "v", "d", "d", "d",]
		self.minJug = [1200, 2700, 1500, 3000, 2000, 2500, 2500, 2400]
		self.penAta = [6, 2, 6, 0, 0, 0, 0, 0]
		self.kimRec = [100, 90, 110, 321, 345, 211, 177, 201]
		self.proGol = [0, 0, 0, 0.1, 0, 0.6, 1.1, 0.9]

	def seleccionArquero(self):
		arq=0
		arquero=""
		for i in range(len(self.penAta)):
			if self.penAta[i]>=arq:
				arq=self.penAta[i]
				arquero=self.jugadores[i]
		a="Arquero: "+arquero+" "+str(arq)+" penales atajados"
		return print(a)

	def seleccionVolante(self):
		vol=0
		volante=""
		for i in range(len(self.kimRec)):
			if self.kimRec[i]>vol:
				vol=self.kimRec[i]
				volante=self.jugadores[i]
		a="Volante: "+volante+" "+str(vol)+"km. recorridos"
		return print(a)

	def seleccionDelantero(self):
		pro=0
		delantero=""
		promedio=0
		delan=""
		for i in range(len(self.proGol)):
			if self.proGol[i]>pro:
				pro=self.proGol[i]
				delantero=self.jugadores[i]
			if self.proGol[i]>promedio and self.proGol[i]<pro:
				promedio=self.proGol[i]
				delan=self.jugadores[i]

		a="Delantero: "+delantero+" "+str(pro)+" de gol"
		b="Delantero: "+delan+" "+str(promedio)+" de gol"
		return print(a),print(b)


class Seleccion():
	def __init__(self):
		tipo=Jugador()
		tipo.seleccionArquero()
		tipo.seleccionVolante()
		tipo.seleccionDelantero()

sele=Seleccion()