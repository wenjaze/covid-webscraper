class Country(object):
	def __init__(
		self,
		name,
		totalCases,
		newCases,
		totalDeaths,
		newDeaths,
		totalRecovered,
		newRecovered,
		activeCases,
		criticalCases,
		casesPerOneMillion,
		deathsPerOneMillion,
		totalTests,
		testsPerOneMillion,
		population,
		oneCaseEveryXPeople,
		oneDeathEveryXPeople,
		oneTestEveryXPeople,
		newCasesPerOneMillion,
		newDeathPerOneMillion,
		activeCasesPerOneMillion,
		):
		self.name = name
		self.totalCases = totalCases
		self.newCases = newCases
		self.totalDeaths = totalDeaths
		self.newDeaths = newDeaths
		self.totalRecovered = totalRecovered
		self.newRecovered = newRecovered
		self.activeCases = activeCases
		self.criticalCases = criticalCases
		self.casesPerOneMillion = casesPerOneMillion
		self.deathsPerOneMillion = deathsPerOneMillion
		self.totalTests = totalTests
		self.testsPerOneMillion = testsPerOneMillion
		self.population = population
		self.oneCaseEveryXPeople = oneCaseEveryXPeople
		self.oneDeathEveryXPeople = oneDeathEveryXPeople
		self.oneTestEveryXPeople = oneTestEveryXPeople
		self.newCasesPerOneMillion = newCasesPerOneMillion
		self.newDeathPerOneMillion = newDeathPerOneMillion
		self.activeCasesPerOneMillion = activeCasesPerOneMillion

	# TODO : __repr__ def __str__(self):