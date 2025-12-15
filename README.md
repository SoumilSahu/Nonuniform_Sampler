---------------------------
Soumil Sahu @ 2025
---------------------------

We wish to map uniform samples $x$ from a uniform distribution $U(x;a,b) = \frac{1}{b-a}$, to the samples $y$ from the desired distribution $f(y;a,b)$. 

$y \in [a,b]$ for $x \in [a,b]$.

The idea is that the probability in the range $dx$ for $U(x)$ should match $dy$ for $f(y)$

$\implies U(x;a,b)dx = f(y;a,b)dy$. The boundary condition here is that $x=a$ corresponds to $y=a$. 

$\implies \int^y_a f(y';a,b)dy' = \frac{x-a}{b-a} \hspace{3mm} \implies x = a + (b-a)\int^y_a f(y';a,b)dy'$

As $f$ is normalized, $\int^b_a f(y';a,b)dy' = 1$ and for RHS to be $1$ it automatically means $x=b$. So, $y=b$ corresponds to $x=b$ by condition of normalcy.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

import the module nonuniform_sampler using

        >> import nonuniform_sampler as nus

use your defined normalised distibution function, for example g(x), for a range of $x \in [a,b]$ to make an sampler object using

        >> sampler_object = nus.sampler(g,a,b)

Now generate N samples from the distribution using

        >> sampler_object.samples(N)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The module has a function "num_bins". It uses the Freedman Diagonis formula to calculate optimal number of bins in case of plotting a histogram of a sample set.