alpha = ['a','b','c']
beta = [0.3, 2.14, 4.2154]
index = [1,2,3]
tf = [True, False]

a_i = list(zip(alpha, index))
print(a_i)

a_b_i = list(zip(alpha, beta, index))
print(a_b_i)

a_b_i_t = list(zip(tf, index))
print(a_b_i_t)