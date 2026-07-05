import math

def calculate_similarity(v1,v2):
    product= [v1[i]*v2[i] for i in range(len(v1))]
    dot_product=sum(product)

    v1_squared=[v1[i]**2 for i in range(len(v1))]
    v1_squared=sum(v1_squared)
    v2_squared=[v2[i]**2 for i in range(len(v1))]
    v2_squared=sum(v2_squared)

    similarity=dot_product/(math.sqrt(v1_squared)*math.sqrt(v2_squared))
    return similarity

if __name__=="__main__":
    print(calculate_similarity([1,2,3],[1,2,4]))
