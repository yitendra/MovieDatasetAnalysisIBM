import pickle
import numpy
import os
pickle_path=os.path.join(os.getcwd(),'myapp',"pickles")

nb = pickle.load(open(os.path.join(pickle_path,"model.pickle"),'rb'))
# vect = open(os.path.join(pickle_path,"pickles","vectorizer.pickle"),'rb')
tfvect = pickle.load(open(os.path.join(pickle_path,"vectorizer.pickle"),'rb'))
