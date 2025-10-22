# Simple Concept Learning using Find-S Algorithm
data = [
    (['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'], 'No'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'], 'Yes')
]

hypothesis = ['?' for _ in range(len(data[0][0]))]

for attributes, label in data:
    if label == 'Yes':
        for i in range(len(hypothesis)):
            if hypothesis[i] == '?' or hypothesis[i] == attributes[i]:
                hypothesis[i] = attributes[i]
            else:
                hypothesis[i] = '?'

print("Final Hypothesis:", hypothesis)
