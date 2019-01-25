// Programming Quantum Computers
//   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
//   O'Reilly Media

// To run this online, go to http://oreilly-qc.github.io?p=6-1

var number_to_flip = 3;
var number_of_iterations = 4;

var num_qubits = 4;
qc.reset(num_qubits);
var reg = qint.new(num_qubits, 'reg')
reg.write(0);
reg.hadamard();

for (var i = 0; i < number_of_iterations; ++i)
{
    // Flip the marked value
    reg.not(~number_to_flip);
    reg.phase(180);
    reg.not(~number_to_flip);

    reg.Grover();

    // Peek at the probability
    prob = reg.peekProbability(number_to_flip);
}
