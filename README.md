# Custom swarm plot function

##Situation: 
As part of my BS in Biomolecular Engineering and Bioinformatics, I took an upper-devision/graduate level data visualization class taught by Professor Christopher Vollmers. In this class we parsed through and visualized a variety of complex biological data using Python and Matplotlib. We were taught best practices when it comes to creating plots that are:
1. Easy to read
2. Easy to interpret
3. Not misleading

## Task:
For the fourth assignment, I was tasked to create my own swarm plot function. To do this, I needed to write an algorithm that efficiently places data points that don't overlap, and whose y-axis location is determined by the points that have already been plotted. 

## Action:
I wrote a python script that can be called via the terminal. It accepts three parameters: Input file, output file, and a matplotlib style sheet file. 
1. The file is parsed and the subread quantity and accuracy values are extracted.  
2. Designed the algorithm that plots each point one at a time and in the exact desired location.To the left or right(which ever is more closer to the center) and with no overlaping.
3. A random subset of the data is taken that is suficiently large to provide a good statistical significance. Running 2,000+ points is not recommended. 

## Results:
A swarm plot function that is superior to any premade package available at the time(2020). Not only is the performance phenominal, the fact that I wrote the function means that I have full customizational control over it. 