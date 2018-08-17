import pickle
import sys
import numpy as np
from sklearn.utils import Bunch 
from sklearn import preprocessing

with open(sys.argv[1], 'rb') as f:
    creatures = pickle.load(f)

#process the species to one-hot-encode and add to feature vectors
species = np.array([c.species for c in creatures])
le = preprocessing.LabelEncoder()
le.fit(species)
species_le = le.transform(species).reshape(-1,1)
enc = preprocessing.OneHotEncoder(sparse=False)
enc.fit(species_le)
species_onehot = enc.transform(species_le)

#process the mfc to make a target array
mfc = np.array([c.mfc for c in creatures])
le2 = preprocessing.LabelEncoder()
le2.fit(mfc)
target = le2.transform(mfc)
target_names = le2.classes_

coords = np.array([[x for x in c.corners.flatten()] for c in creatures])
lead = np.array([c.lead for c in creatures]).reshape(-1,1)

vectors = np.hstack((coords, lead, species_onehot))


out = Bunch(
        data=vectors, 
        data_species=species,
        target=target, 
        target_names=target_names,
        plot_colors=[c.plot_color for c in creatures]
        )
        

with open(sys.argv[2], 'wb') as f:
    pickle.dump(out, f)




