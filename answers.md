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

  The probability that Quicksort makes at least $10^cn \ln n$ comparisons is at most $O\left(\frac{1}{10^c}\right)$. As $c$ increases the upper probability bound decreases exponentially. This indicates that the actual number of comparisions is increasingly unlikely to greatly exceed the expected number of comparisons as c grows.




- **2a. (10 pts)**  
  
  Algorithm  $A'(I)$

  1\. Define maximum number of cycles allowed as $k$. $k$ value selection is determined by the desired probability of success $\delta$.  
  2\. Run $A(I)$.  
  3\. Check the result by using $C(A(I))$.  
  4\. If the reult is correct, return the result and report success. END  
  5\. Decrement $k$ by 1.  
  6\. If $k = 0$, return no result and report failure.  END  
  7\. Restart the process at step 2.

  Probability Equation  

  Desired Probability of success: $\delta$  
  Probability of success for one run: $\epsilon$  
  Probability of failure for one run: $(1 - \epsilon)$  
  Probability that all runs fail: $(1 - \epsilon)^k$  
  Probability of at least one successful run: $1 - (1 - \epsilon)^k$  

  Solve for $k$:  

  $1 - (1 - \epsilon)^k \geq \delta$  
  $(1 - \epsilon)^k \leq 1 - \delta$  
  $k \cdot \log(1 - \epsilon) \leq \log(1 - \delta)$  
  $k \geq \frac{\log(1 - \delta)}{\log(1 - \epsilon)}$  

  $\boxed{k = \left\lceil\frac{\log(1 - \delta)}{\log(1 - \epsilon)}\right\rceil}$  

  Work for $A'(I)$  

  The total worst case work for one cycle of $A(I)$ and C(A(I)): $O(W(n))$  
  Maximum number of cycles: $\lceil\frac{\log(1 - \delta)}{\log(1 - \epsilon)}\rceil$  

  $\boxed{W_{A'}(n, \delta, \epsilon) \in O\left(W(n)\cdot \left\lceil\frac{\log(1 - \delta)}{\log(1 - \epsilon)}\right\rceil\right)}$




- **2b. (10 pts)**




- **3b. (5 pts)**




- **3c. (5 pts)**
