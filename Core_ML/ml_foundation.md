Dataset is divided into three parts.
1. Training dataset: mostly training data. 70-80% of total dataset.
2. Testing dataset: Left untouch.
3. Validation dataset: it is part of training dataset for validation purpose.

---

Types of Cross Validation:
- Leave one out Cross validation: In this method, we always leave 1 row of data out from whole training data for validation. if we have dataset of size 1300, where 300 is testing. 10000 is training data then, we need 1000 iterations to create our validation data. It **overfits** and very slow and tedious. No one uses it.

- Hold out Cross Validation: We use random_state to randomly select the data for validation. It can either be overfitting or underfitting.

- K-Fold Cross Validation: We divide the training data into k parts (chunks). where 1 of k chunks is validation data whereas (k-1) chunks is training data. It is very popular and very efficient. K is a hyperparameter and generate value of k is set between **5-10**. It may sound similar to LOOCV but in this we iteration till K<sup>th</sup> whereas in LOOCV we do iteration till N<sup>th</sup>. for the average of accuracy, we calculate it by average of CV1 + CV2 + ...+ CVK
still it will not work with imbalanced dataset.

- Stratified Cross Validation: In this cross validation we tend to have the data with equal or near equal no of outcomes. like if have all together 100 data in validation dataset, i tend to have 50 true, 50 false or 60 true and 40 false like that. It **works with imbalanced dataset** too and tends to fix it at some extend.

- Time Series Cross Validation: Time series data **requires sequential data based on time**. It mimics real-world scenarios by ensuring the model only learns from the past to predict the immediate future, making the evaluation more reliable for time-dependent data. 

---

**Bias (Underfitting)**

What it is: A model makes strong, incorrect assumptions about the data, failing to capture the true underlying relationship.
Result: High error on both training and testing data; the model is too simple.

Analogy: A straight line trying to fit a curved pattern. 

**Variance (Overfitting)**

What it is: A model learns the training data too well, including its random noise and quirks, becoming overly complex and sensitive to small changes.

Result: Great performance on training data but poor performance on new data; it doesn't generalize.

Analogy: A jagged, wiggly line that perfectly hits every training point but misses new ones. 

**The Tradeoff**

You can't have both low bias and low variance easily; reducing one often increases the other.
The goal is to find the sweet spot (the bias-variance tradeoff) where the model is complex enough to learn patterns but simple enough to generalize well to unseen data. 

---

**Feature Scaling**

- Feature scaling makes features comparable so the model learns patterns, not numbers.
