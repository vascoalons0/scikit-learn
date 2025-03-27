from sklearn.metrics import f1_score

# Teste binário — deve usar pos_label
print("Binary:", f1_score([0, 1, 1, 0], [0, 1, 0, 0]))

# Teste multiclasse — deve ignorar pos_label sem erro
print("Multiclass:", f1_score([0, 1, 2, 0, 1, 2], [0, 0, 2, 0, 1, 2], average='macro'))
