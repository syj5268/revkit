from revkit import netlist, oracle_synth, truth_table
import os
import revkit.export.qiskit
from qiskit.tools.visualization import circuit_drawer

if __name__ == "__main__":
    function = truth_table.from_expression("[(ab)(cd)]") # (a ∧ b) ⊕ (c ∧ d)
    circuit = oracle_synth(function)
    qcircuit = circuit.to_qiskit()

    if not os.path.exists('output'):
        os.makedirs('output')
    # Save the circuit as an image file
    circuit_drawer(qcircuit, output='mpl', filename='output/test.png')