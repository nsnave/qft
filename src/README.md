Each folder contains the code to convert from the source framework to the intermediate representation and code to convert from the intermediate representation to the source framework.

The driver.py file handles the translation given a source and target framework as input.

Each folder will contain a file for the parser and generator.

Useful Links:
  - https://devblogs.microsoft.com/qsharp/introducing-quantum-intermediate-representation-qir/
  - https://docs.python.org/3/library/ast.html
  - https://github.com/aherlihy/PythonLLVM
  - https://github.com/numba/numba
  - https://github.com/numba/llvmlite

"The Plan":
  - Option 1: Use an existing Python to LLVM IR compiler and then make an LLVM IR to QIR compiler.
    -  Would let the work focus on the quantum compilation.
    -  pyllvm or numba could be used for the Python to LLVM IR part.
    -  but neither pyllvm nor numba can fully convert Python to LLVM and issues might come up when including quantum libraries.
  - Option 2: Create a Python to QIR compiler
    - Full control over compilation but would require more work.
    - Python's AST module would produce the AST for us, which would handle syntactic analysis.
    - We would have to handle the semantic analysis, which would include type inference and checking.
    - Possibly allow for better flexibility when dealing with quantum frameworks.
    - Could use A. Herilhy's PythonLLVM Thesis to get started on semantic analysis.
    - Could use llvmlite to generate QIR. (?)

Leaning toward option 2...
