from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ, BasicAer
import math

for i in range (0, 20000):
    for j in range (0, 64):
        reg_q = QuantumRegister(1, name='reg_q')
        reg_c = ClassicalRegister(1, name='regc')
        qc = QuantumCircuit(reg_q, reg_c)

        qc.reset(reg_q)          # Init qubit
        qc.h(reg_q)              # H-gate for qubit
        qc.measure(reg_q, reg_c) # Read qubit

        backend = BasicAer.get_backend('statevector_simulator')
        job = execute(qc, backend)
