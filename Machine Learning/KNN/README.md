### K Nearest Neighbor
1. I have two classes and I have feature vectors which are 2d
2. X(sub1) is the 1st axis and X(Sub2) is the 2nd axis
3. I have a training sample 
4. For each new sample I want to classify. I calc the dist between the original sample to each of the training sample
5. I take a look at the nearest neighbors
6. I give a label to the nearest neighbors based on the most common neighbors
7. For example, 2 green classes and a red class therefore the label will be green class
8. To calculate the distance between the samples I use the euclidian distance aka the distance formula

### More general case formula:
- Square root of (summation of (q-subi - p-subi)^2) from i to n where n is the num of dim