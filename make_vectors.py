import pickle
import sys
import numpy as np

from sklearn import preprocessing

with open(sys.argv[1], 'rb') as f:
    creatures = pickle.load(f)

le = preprocessing.LabelEncoder()
le.fit([c.species for c in creatures])
species_le = le.transform([c.species for c in creatures]).reshape(-1,1)

enc = preprocessing.OneHotEncoder(sparse=False)
enc.fit(species_le)
species_onehot = enc.transform(species_le)

coords = np.array([[x for x in c.corners.flatten()] for c in creatures])
lead = np.array([c.lead for c in creatures]).reshape(-1,1)

vectors = np.hstack((coords, lead, species_onehot))

with open(sys.argv[2], 'wb') as f:
    pickle.dump(vectors, f)




