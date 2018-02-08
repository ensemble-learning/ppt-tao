---

@title[Introduction]
### Tao Cheng
### Research Assistant
### JCAP, Caltech

<span style="color: gray">HOR</span>

---

@title[Introduction]
Hydrogen oxidation and evolution reactions (HOR/HER) are two of the key processes in renewable energy conversion and storage devices

---
For as yet unclear reasons, the HOR/HER kinetics on Pt are much slower in alkaline than in acid electrolytes. 

---
100-fold activity decrease going from low to high pH

![](assets/f1.png)  

<span style="font-size: 0.4em">Durst et al. Energy Environ. Sci., 2014, 7, 2255</span>
---
HBE increases with increasing pH

![](assets/f3.png)  

<span style="font-size: 0.4em">Sheng et al.  Nat Commun, 2015, 6</span>

---
HBE increases with increasing pH

![](assets/f4.png)  

<span style="font-size: 0.4em">Sheng et al.  Nat Commun, 2015, 6</span>

---
### Some explainations
- <span style="font-size: 0.6em">Faster formation of H* from H plus than from H2O. (Strmcnik et al. Nano Energy, 2016) </span>
- <span style="font-size: 0.6em">The pH dependence of entropy change from the proton transfer from the bulk solution into the outer Helmholz layer. (Rossmeisl et al. Catalysis Today, 2016)</span>
- <span style="font-size: 0.6em">Partial oxidation of water adsorption on step sites of metals (Schwarz et al. Phys. Chem. Chem. Phys. 2016)</span>
- <span style="font-size: 0.6em">Weakened OH adsorption strength induced by the co-adsorption of cation (McCrum et al. J. Phys. Chem. C, 2016)</span>

---
### Our hypothesis
The pH-dependence of the HBE is from change of water adsorption energy

---
##### Simulate the interface from explicit simulation

<span style="font-size: 0.4em">At pH 0.2 (HClO4), the experiment Hupd peak of Pt(100) appears at about 0.3 V.</span>  
<span style="font-size: 0.4em">At pH 5.2 (Acetate buffer), the experiment Hupd peak of Pt(100) appears at about 0.25 V.</span>  
<span style="font-size: 0.4em">At pH 12.8 (KOH), the experiment Hupd peak of Pt(100) appears at about 0.4 V.</span>  

Thus the voltage we interested with are:  
<span style="font-size: 0.4em"> 4.4 + 0.30 -  0.2 x 0.0592 = 4.69;</span>
<span style="font-size: 0.4em"> 4.4 + 0.25 -  5.2 x 0.0592 = 4.34;</span>
<span style="font-size: 0.4em"> 4.4 + 0.40 - 12.8 x 0.0592 = 4.04;</span>  
<span style="font-size: 0.4em">set 1: 4.69 to 4.04;</span>
<span style="font-size: 0.4em">set 2: 4.89 to 4.24;</span>
<span style="font-size: 0.4em">set 3: 4.40, 3.98, 3.57</span>

simulation results:  
<span style="font-size: 0.4em">00e: 5.0;</span>
<span style="font-size: 0.4em">10e: 4.0;</span>
<span style="font-size: 0.4em">20e: 3.0</span>

simulations
<span style="font-size: 0.4em">04e, 10e, 14e</span>



---
### Reduce the full explicit simulation to semi-explicit simulation

---
### The interface structure from simulation

---
### The rdf 

---
### Github
![Video](https://www.youtube.com/embed/0fHY0tnDgkw)
