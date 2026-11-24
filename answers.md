# CMPS 6610 Problem Set 6
## Answers

**Name:**$\underline{\hspace{1in}\text{Rob Hartley}\hspace{1in}}$


Place all written answers from this assignment here for easier grading.




- **1a. (7 pts)**  
  
  Markov's Inequality:    
  
  $P[X \geq \alpha] \leq \frac{E[X]}{\alpha}$  
  
  Quicksort Expected Comparisons:  
  
  $E[X] = O(n \log n)$  

  Number of Comparisons We're Interested In:  

  $\alpha = cn^2$, $c > 0$  

  Substitute into the Equation:  

  $P[X \geq cn^2] \leq \frac{O(n \log n)}{cn^2}$  

  $\boxed{P[X \geq cn^2] \leq O\left(\frac{\log n}{n}\right)}$  

  The probability that Quicksort makes $\Omega(n^2)$ comparisons is at most $O\left(\frac{\log n}{n}\right)$.

- **1b. (8 pts)**  
  
  Markov's Inequality:    
  
  $P[X \geq \alpha] \leq \frac{E[X]}{\alpha}$  
  
  Quicksort Expected Comparisons:  
  
  $E[X] = O(n \log n)$  

  Number of Comparisons We're Interested In:  

  $\alpha = 10^cn \ln n$, $c > 0$  

  Substitute into the Equation:  

  $P[X \geq 10^cn \ln n] \leq \frac{O(n \log n)}{10^cn \ln n}$  

  $\boxed{P[X \geq 10^cn \ln n] \leq O\left(\frac{1}{10^c}\right)}$  

  The probability that Quicksort makes at least $10^cn \ln n$ comparisons is at most $O\left(\frac{1}{10^c}\right)$. As $c$ increases the upper probability bound decreases exponentially. This indicates that much of the expected work is concentrated below $10^cn \ln n$ comparisons.




- **2a. (10 pts)**




- **2b. (10 pts)**




- **3b. (5 pts)**




- **3c. (5 pts)**
