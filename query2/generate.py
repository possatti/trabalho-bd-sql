import subprocess

# Nome final do arquivo a ser gerado.
NOME_DO_ARQUIVO_GERADO = 'query2.sql'

# Chama os scripts para gerarem seus arquivos.
subprocess.call(['python3', 'Veiculo.py'])
subprocess.call(['python3', 'VeiculoTipoCarga.py'])
subprocess.call(['python3', 'Telefone.py'])
subprocess.call(['python3', 'Endereco.py'])
subprocess.call(['python3', 'Contato.py'])

# Junta todos os SQLs em um único arquivo.
# Atenção: A ordem importa! Devido as relações entre as tabelas,
#          algumas devem ser preenchidas primeiro.
SQLFiles = [
'SQL Independente/TipoCarga.sql',
'SQL Gerado/Veiculo.sql',
'SQL Gerado/VeiculoTipoCarga.sql',
'SQL Gerado/Contato.sql',
'SQL Gerado/Telefone.sql',
'SQL Gerado/Endereco.sql'
]

with open(NOME_DO_ARQUIVO_GERADO, "w") as arqSaida:
	for SQLFile in SQLFiles:
		with open(SQLFile, "r") as arqEntrada:
			for line in arqEntrada.readlines():
				arqSaida.write(line)
