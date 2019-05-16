
# coding: utf-8

# # ML for Reservation Data & Correlation with Houston Census Figures
# 
# import pandas as pd
# import numpy as np
# import xlrd
# import matplotlib.pyplot as plt
# import seaborn as sns


import warnings
warnings.simplefilter('ignore')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import seaborn as sns


from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

Census_Data = pd.read_csv('censuses.csv', index_col=None)
sns.heatmap(Census_Data.isnull(),yticklabels=False,cbar=True,cmap='viridis')

Census_Data.isnull().any()


# In[56]:


Census_Data.columns


# In[57]:


Census_Data = Census_Data[['color_race', 'sex', 'age_at_last_birthday', 'occupation',
       'census_year', 'grouped_occu']]


# In[58]:


Census_Data.isnull().any()


# ## Clean the Age Column

# In[59]:


Census_Data['age_at_last_birthday'].unique()


# In[60]:


def age_clean(data,under_1_value = 1, pandas = 'yes'):
    clean_age = []
    if pandas == 'yes':
        data_lst = data.tolist()
    else:
        data_lst = data
    for datum in data_lst:
        if 'month' in str(datum):
            if 'and' in str(datum):
                clean_age.append(str(datum).split(' ')[0])
            else:
                clean_age.append(str(under_1_value))
        else:
            clean_age.append(datum)
    return clean_age


# In[61]:


dirty_age = Census_Data['age_at_last_birthday']
#dirty_age
clean_age = age_clean(dirty_age,under_1_value = 1, pandas = 'yes')


# In[62]:


Census_Data['Age'] = clean_age


# In[63]:


Census_Data=Census_Data.dropna()
Census_Data['Age'].unique()


# In[64]:


Census_Data.shape


# In[65]:


print(Census_Data[Census_Data.isnull().any(axis=1)].head())


# In[66]:


Census_Data['Age'] = pd.to_numeric(Census_Data['Age'], errors='coerce')


# In[67]:


Census_Data['Age'].unique()


# In[68]:


Census_Data.isnull().any()


# In[69]:


Census_Data=Census_Data.dropna()


# In[70]:


Census_Data.isnull().any()


# In[71]:


Census_Data.shape


# ## Reduce the Race columns to B and W

# In[72]:


Census_Data['color_race'].unique()


# In[73]:


Census_Data['color_race'].replace(['Mu', 'M', 'M/W', 'My'], "B", inplace=True)


# In[74]:


Census_Data['color_race'].unique()


# In[75]:


Census_Data = Census_Data[Census_Data.color_race != 'Jp']
Census_Data['color_race'].unique()


# ## Clean the Gender column to ensure M and F only

# In[76]:


Census_Data['sex'].unique()


# In[77]:


Census_Data = Census_Data[Census_Data.sex != 'FM']
Census_Data['sex'].unique()


# In[78]:


Census_Data['census_year'].unique()


# In[79]:


Census_Data['grouped_occu'].unique()


# In[80]:


Census_Data.shape


# In[81]:


Census_Data.rename(columns={'color_race': 'Race', 'sex': 'Sex', 'census_year':'Year',
                           'grouped_occu':'Occ'}, inplace=True)


# In[82]:


Census_Data.head(10)


# In[83]:


del Census_Data['age_at_last_birthday']
Census_Data.head(5)


# In[84]:


Census_Data.shape


# ## IF AGE <=14 AND OCC ="MISSING OCCUPATIONS" THEN OCC = 'STUDENT'

# In[85]:


Census_Data.loc[ (Census_Data.Age <= 14) & (Census_Data.Occ =='Missing Occupations'),'Occ'] = 'Student'


# In[86]:


Census_Data.shape


# ## Remove 'Missing Occupations'

# In[87]:


Census_Data = Census_Data[Census_Data.Occ != 'Missing Occupations']


# In[88]:


Census_Data.shape


# In[89]:


Census_Data.head(5)


# In[90]:


sns.countplot(x = 'Race',data=Census_Data)
plt.show()


# In[91]:


sns.countplot(x='Year',hue='Race',data=Census_Data,palette='RdBu_r')


# In[92]:


sns.countplot(x = 'Age',data=Census_Data)
plt.show()


# In[93]:


Census_Data['Age'].hist(bins=25,color='darkred',alpha=0.7)


# In[94]:


sns.countplot(x = 'Sex',data=Census_Data)
plt.show()


# In[95]:


sns.countplot(x = 'Year',data=Census_Data)
plt.show()


# ## Group the Age column into Age Groups

# In[96]:


age_ranges= [0,15,55,110]
age_labels = ['0-15','16-55','Above-56']
Census_Data['Age'] = pd.cut(Census_Data['Age'], bins=age_ranges, labels=age_labels)


# In[97]:


Census_Data.head(5)


# In[98]:


sns.countplot(x='Occ',hue='Race',data=Census_Data) #,palette='RdBu_r')


# In[99]:


sns.countplot(x='Year',hue='Occ',data=Census_Data)


# In[100]:


sns.countplot(x = 'Occ',hue='Age',data=Census_Data)
plt.show()


# In[102]:


sns.countplot(x = 'Occ',hue='Sex',data=Census_Data)
plt.show()


# ## Hot encode the Race, Sex, Year and Age columns

# In[103]:


data2 = pd.get_dummies(Census_Data, columns =['Race','Sex', 'Year','Age'])
data2.columns


# In[104]:


data2.head()


# In[105]:


del data2['occupation']
data2 = data2.apply(pd.to_numeric, errors='ignore')
data2.dtypes


# In[106]:


data2.shape


# ## data2 dataframe

# In[107]:


data2.head()


# In[108]:


data3 = data2.copy()
data3['Occ'][data3['Occ']=='Unskilled']=0
data3['Occ'][data3['Occ']=='Skilled Labor']=1
data3['Occ'][data3['Occ']=='Skilled Professionals']=2
data3['Occ'][data3['Occ']=='Student']=3


# ## data3 dataframe has Occ coded with 0,1,2,3:
# [data3['Occ']=='Unskilled']=0
# [data3['Occ']=='Skilled Labor']=1
# [data3['Occ']=='Skilled Professionals']=2
# [data3['Occ']=='Student']=3

# In[109]:


data3.head()


# In[110]:


data3.corr()


# ## data4 dataframe has hot encoded Occ with 1 and 0's in seperate columns

# In[111]:


data4 = pd.get_dummies(data3, columns =['Occ'])


# In[112]:


data4.columns


# In[113]:


data4.head()


# In[114]:


data4.corr(method='spearman')


# ## Filter Using Pearson Correlation

# In[159]:


#Using Pearson Correlation
plt.figure(figsize=(12,10))
cor = data4.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()


# In[160]:


#Correlation with output variable
Occupations = ['Occ_0', 'Occ_1', 'Occ_2','Occ_3']
for i in Occupations:
    cor_target = abs(cor[i])
    #Selecting highly correlated features
    relevant_features = cor_target[cor_target>0.25]
    print(relevant_features)
    print("--------")


# ## Machine learning

# In[117]:


#importing libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# ## Create train/test split of data using data2 dataframe

# In[118]:


train,test = train_test_split(data2,test_size=0.2,random_state=7)


# In[119]:


print ("train shape:   ")
print(train.shape)
print ("test shape:    ")
print(test.shape)
print ("Unique classes with count : ")
print(pd.value_counts(train['Occ']))
print ("data description : ")
#print(train.describe())


# In[120]:


#checking missing values
print (train.info())
#No null values


# In[121]:


#Modelling
train['Occ'][train['Occ']=='Unskilled']=0
train['Occ'][train['Occ']=='Skilled Labor']=1
train['Occ'][train['Occ']=='Skilled Professionals']=2
train['Occ'][train['Occ']=='Student']=3

test['Occ'][test['Occ']=='Unskilled']=0
test['Occ'][test['Occ']=='Skilled Labor']=1
test['Occ'][test['Occ']=='Skilled Professionals']=2
test['Occ'][test['Occ']=='Student']=3

X = train.iloc[:,1:]
y = train.iloc[:,0]
y = pd.to_numeric(y)
y_test=pd.to_numeric(test.iloc[:,0])


# In[122]:


# Spot Check Algorithms
models = []
models.append(('LogisticRegression', LogisticRegression()))
models.append(('DecisionTreeClassifier', DecisionTreeClassifier()))
models.append(('LinearDiscriminantAnalysis', LinearDiscriminantAnalysis()))
models.append(('KNeighborsClassifier', KNeighborsClassifier()))
models.append(('GaussianNB', GaussianNB()))
models.append(('SVC', SVC()))
# evaluate each model in turn
scoring = 'accuracy'


# In[123]:


results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=5)
	cv_results = model_selection.cross_val_score(model, X,y, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)


# ## Warning: Variables are collinear means that the predictors are correlated - Namely M/F and B/W

# ## Remove one of the Collinear variables - both W and F

# In[162]:


data5 = data2.copy()
data5.columns


# In[163]:


columns = ['Occ', 'Race_B', 'Race_W', 'Sex_F', 'Sex_M', 'Year_1900', 'Year_1910',
       'Year_1920', 'Age_0-15', 'Age_16-55', 'Age_Above-56']

data5.drop(['Sex_F','Race_W','Year_1920','Age_Above-56'], axis=1, inplace=True)

data5.head(5)


# In[164]:


train,test = train_test_split(data5,test_size=0.2,random_state=7)


# In[165]:


correlation_matrix = train.corr()
plt.figure(figsize=(10,8))
ax = sns.heatmap(correlation_matrix, vmax=1, square=True, annot=True,fmt='.2f', cmap ='GnBu', cbar_kws={"shrink": .5}, robust=True)
plt.title('Correlation matrix between the features', fontsize=20)
plt.show()


# In[166]:


print ("train shape:   ")
print(train.shape)
print ("test shape:    ")
print(test.shape)
print ("Unique classes with count : ")
print(pd.value_counts(train['Occ']))
print ("data description : ")
#print(train.describe())


# In[167]:


#Modelling
train['Occ'][train['Occ']=='Unskilled']=0
train['Occ'][train['Occ']=='Skilled Labor']=1
train['Occ'][train['Occ']=='Skilled Professionals']=2
train['Occ'][train['Occ']=='Student']=3

test['Occ'][test['Occ']=='Unskilled']=0
test['Occ'][test['Occ']=='Skilled Labor']=1
test['Occ'][test['Occ']=='Skilled Professionals']=2
test['Occ'][test['Occ']=='Student']=3

X = train.iloc[:,1:]
y = train.iloc[:,0]
y = pd.to_numeric(y)
y_test=pd.to_numeric(test.iloc[:,0])


# ## Compare the Results for different classifier models

# In[168]:


results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=15, random_state=7)
	cv_results = model_selection.cross_val_score(model, X,y, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)


# In[169]:


# Make predictions on validation dataset
print ("LogisticRegression Performance")
LR = LogisticRegression()
LR.fit(X,y)
predictions = LR.predict(test.iloc[:,1:])
print(accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))


# In[170]:


# Make predictions on validation dataset
print ("SVC Performance")
SVM = SVC()
SVM.fit(X,y)
predictions = SVM.predict(test.iloc[:,1:])
print(accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))


# In[171]:


print ("KNN Performance")
KNN = KNeighborsClassifier()
KNN.fit(X,y)
predictions = KNN.predict(test.iloc[:,1:])
print (accuracy_score(y_test, predictions))
print (confusion_matrix(y_test, predictions))
print (classification_report(y_test, predictions))


# ## PCA Projection to 2D

# In[410]:


data2.columns


# In[411]:


features = ['Race_B', 'Race_W', 'Sex_F', 'Sex_M', 'Year_1900', 'Year_1910',
       'Year_1920', 'Age_0-15', 'Age_16-55', 'Age_Above-56']


# In[412]:


x = data2.loc[:, features].values


# In[413]:


y = data2.loc[:,['Occ']].values


# In[414]:


pd.DataFrame(data = x, columns = features).head()


# In[415]:


from sklearn.decomposition import PCA
pca = PCA(n_components=2)


# In[416]:


principalComponents = pca.fit_transform(x)


# In[417]:


X_2D = pca.transform(x)


# In[418]:


principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])


# In[419]:


principalDf.head(5)


# In[420]:


data2[['Occ']].head()


# In[421]:


finalDf = pd.concat([principalDf, data2[['Occ']]], axis = 1)
finalDf.head(5)


# In[422]:



sns.lmplot("principal component 1", "principal component 2", hue='Occ', data=finalDf, fit_reg=False);


# In[423]:


plt.scatter(finalDf["principal component 1"], finalDf["principal component 2"],
            edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('rainbow', 10))
#plt.colorbar(label='digit label', ticks=range(10))
#plt.colorbar(ticks=range(10))
plt.clim(-0.5, 9.5);


# In[424]:


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)


targets = ['Unskilled', 'Student', 'Skilled Labor','Skilled Professionals']
colors = ['b', 'r','g','orange']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['Occ'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()


# In[425]:


print(pca.components_)


# In[426]:


pca.explained_variance_ratio_


# In[427]:


pca = PCA().fit(x)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');


# In[428]:


sns.heatmap(np.log(pca.inverse_transform(np.eye(x.shape[1]))), cmap="hot", cbar=False)
plt.ylabel('principal component', fontsize=12);
plt.xlabel('original feature index', fontsize=12);


# In[429]:


pca_inv_data = pca.inverse_transform(np.eye(x.shape[1]))

fig = plt.figure(figsize=(10, 6.5))
plt.plot(pca_inv_data.mean(axis=0), '--o', label = 'mean')
plt.plot(np.square(pca_inv_data.std(axis=0)), '--o', label = 'variance')
plt.legend(loc='lower right')
plt.ylabel('feature contribution', fontsize=12);
plt.xlabel('feature index', fontsize=12);
plt.tick_params(axis='both', which='major', labelsize=12);
plt.tick_params(axis='both', which='minor', labelsize=12);
#plt.xlim([0, 7])
plt.legend(loc='upper left', fontsize=12)


# In[298]:


features


# In[358]:


#x_pca = pca.transform(x)
print("original shape:   ", x.shape)
print("transformed shape:", principalComponents.shape)


# In[347]:


X[:, 0]


# In[348]:


X[:, 1]


# In[349]:


X.shape


# ## Receiver Operating Characteristic (ROC)

# Example of Receiver Operating Characteristic (ROC) metric to evaluate classifier output quality.
# 
# ROC curves typically feature true positive rate on the Y axis, and false positive rate on the X axis. This means that the top left corner of the plot is the “ideal” point - a false positive rate of zero, and a true positive rate of one. This is not very realistic, but it does mean that a larger area under the curve (AUC) is usually better.
# 
# The “steepness” of ROC curves is also important, since it is ideal to maximize the true positive rate while minimizing the false positive rate.

# In[222]:


data2.head()


# In[223]:


#data2["Occ"]=data2["Occ"].astype(int)
data6 = pd.get_dummies(data2, columns =['Occ'])
data6.columns


# In[224]:


import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp


# In[225]:


X = data6.iloc[:,:-4].values
y = data6.iloc[:,-4:].values


# In[226]:


X


# In[227]:


y


# In[228]:


n_classes = 4


# In[229]:


# Add noisy features to make the problem harder
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]


# shuffle and split training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5,
                                                    random_state=0)

# Learn to predict each class against the other
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,
                                 random_state=random_state))
y_score = classifier.fit(X_train, y_train).decision_function(X_test)

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])


# In[230]:


# Compute macro-average ROC curve and ROC area
lw = 2
# First aggregate all false positive rates
all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

# Then interpolate all ROC curves at this points
mean_tpr = np.zeros_like(all_fpr)
for i in range(n_classes):
    mean_tpr += interp(all_fpr, fpr[i], tpr[i])

# Finally average it and compute AUC
mean_tpr /= n_classes

fpr["macro"] = all_fpr
tpr["macro"] = mean_tpr
roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

# Plot all ROC curves
plt.figure()
plt.plot(fpr["micro"], tpr["micro"],
         label='micro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["micro"]),
         color='deeppink', linestyle=':', linewidth=4)

plt.plot(fpr["macro"], tpr["macro"],
         label='macro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["macro"]),
         color='navy', linestyle=':', linewidth=4)

colors = cycle(['aqua', 'darkorange', 'cornflowerblue','green'])
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=lw)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Some extension of Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()


# ## Backward Elimination

# In[385]:


data3.head()


# In[386]:


XG = data3.drop("Occ",1) # feature matrix


# In[392]:


XG.head()


# In[393]:


yG = data3["Occ"]
yG.head()


# In[396]:


import statsmodels.api as sm
#Adding constant column of ones, mandatory for sm.OLS model
X_1 = sm.add_constant(XG)
X_1.head()


# In[402]:


#Fitting sm.OLS model
#model = sm.OLS(yG,X_1).fit()
est = sm.OLS(yG.astype(float), X_1.astype(float)).fit()
est.pvalues


# In[403]:


#Backward Elimination
cols = list(XG.columns)
pmax = 1
while (len(cols)>0):
    p= []
    X_1 = XG[cols]
    X_1 = sm.add_constant(X_1)
    model = sm.OLS(yG.astype(float),X_1.astype(float)).fit()
    p = pd.Series(model.pvalues.values[1:],index = cols)      
    pmax = max(p)
    feature_with_p_max = p.idxmax()
    if(pmax>0.05):
        cols.remove(feature_with_p_max)
    else:
        break
selected_features_BE = cols
print(selected_features_BE)


# ## Embedded Method

# Embedded methods are iterative in a sense that takes care of each iteration of the model training process and carefully extract those features which contribute the most to the training for a particular iteration. Regularization methods are the most commonly used embedded methods which penalize a feature given a coefficient threshold.
# 
# Here we will do feature selection using Lasso regularization. If the feature is irrelevant, lasso penalizes it’s coefficient and make it 0. Hence the features with coefficient = 0 are removed and the rest are taken.

# In[405]:


from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
reg = LassoCV()
reg.fit(XG, yG)
print("Best alpha using built-in LassoCV: %f" % reg.alpha_)
print("Best score using built-in LassoCV: %f" %reg.score(XG,yG))
coef = pd.Series(reg.coef_, index = XG.columns)


# In[406]:


print("Lasso picked " + str(sum(coef != 0)) + " variables and eliminated the other " +  str(sum(coef == 0)) + " variables")


# In[409]:


imp_coef = coef.sort_values()
import matplotlib
matplotlib.rcParams['figure.figsize'] = (4.0, 7.0)
imp_coef.plot(kind = "barh")
plt.title("Feature importance using Lasso Model")

