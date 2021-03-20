from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

print(qc.draw('text'))

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=8)
result = job.result()

counts = result.get_counts(qc)
print(counts)


'''
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
print(result.get_statevector(qc, decimals=3))
'''
