# pip install transf
 A Math library for finding Laplace transforms for simple expressions. This library uses string modification and pattern evalutaion via lexer and Shunting yard algorithm for its parser which is later converted to Expression nodes to evaluate the given expression. Currently, its under further development. But still its usable for limited purposes.
## Usage
from ltransf import LaplaceOf
expr = LaplaceOf("3*sin(3*t)")
print(expr.evaluate())

> Happy coding ! 
