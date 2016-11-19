- SVM with linear kernel function and changing the C value

configuration:
  - kernel linear
  - C = 1
  - max_iter 200
score = 0.8854
             precision    recall  f1-score   support

          0       0.92      0.96      0.94       460
          1       0.94      0.98      0.96       571
          2       0.90      0.86      0.88       530
          3       0.85      0.87      0.86       500
          4       0.88      0.91      0.90       500
          5       0.83      0.82      0.82       456
          6       0.92      0.91      0.91       462
          7       0.89      0.88      0.88       512
          8       0.83      0.80      0.82       489
          9       0.88      0.85      0.86       520

avg / total       0.88      0.89      0.88      5000

configuration:
  - kernel linear
  - C = 0.5
  - max_iter 200
score = 0.886
             precision    recall  f1-score   support

          0       0.93      0.97      0.95       460
          1       0.94      0.98      0.96       571
          2       0.90      0.86      0.88       530
          3       0.86      0.88      0.87       500
          4       0.88      0.91      0.89       500
          5       0.83      0.82      0.83       456
          6       0.92      0.91      0.91       462
          7       0.89      0.88      0.88       512
          8       0.83      0.80      0.82       489
          9       0.87      0.85      0.86       520

avg / total       0.89      0.89      0.89      5000

configuration:
  - kernel linear
  - C = 0.1
  - max_iter 200
score = 0.8898
             precision    recall  f1-score   support

          0       0.91      0.98      0.94       460
          1       0.94      0.98      0.96       571
          2       0.91      0.88      0.89       530
          3       0.88      0.88      0.88       500
          4       0.87      0.90      0.89       500
          5       0.84      0.84      0.84       456
          6       0.92      0.90      0.91       462
          7       0.90      0.88      0.89       512
          8       0.85      0.80      0.82       489
          9       0.87      0.84      0.85       520

avg / total       0.89      0.89      0.89      5000

configuration:
  - kernel linear
  - C = 0.01
  - max_iter 200
score = 0.883
             precision    recall  f1-score   support

          0       0.90      0.98      0.94       460
          1       0.92      0.98      0.95       571
          2       0.91      0.87      0.89       530
          3       0.87      0.88      0.88       500
          4       0.85      0.90      0.88       500
          5       0.85      0.81      0.83       456
          6       0.90      0.91      0.91       462
          7       0.88      0.87      0.87       512
          8       0.87      0.79      0.83       489
          9       0.86      0.83      0.85       520

avg / total       0.88      0.88      0.88      5000

- As we saw the best accuracy was reached when the value of C was set to 0.1

- Now we will change the kernel function and see how it will affect the accuracy

configuration:
  - kernel poly
  - C = 0.1
  - max_iter 200
score = 0.838
             precision    recall  f1-score   support

          0       0.72      0.97      0.83       460
          1       0.81      0.99      0.89       571
          2       0.89      0.82      0.85       530
          3       0.79      0.90      0.84       500
          4       0.94      0.81      0.87       500
          5       0.95      0.61      0.74       456
          6       0.78      0.89      0.83       462
          7       0.82      0.84      0.83       512
          8       0.90      0.75      0.82       489
          9       0.91      0.79      0.85       520

avg / total       0.85      0.84      0.84      5000

configuration:
  - kernel rbf
  - C = 0.1
  - max_iter 200
score = 0.8188
             precision    recall  f1-score   support

          0       0.85      0.96      0.91       460
          1       0.76      0.98      0.85       571
          2       0.89      0.77      0.83       530
          3       0.74      0.87      0.80       500
          4       0.81      0.88      0.84       500
          5       0.88      0.55      0.67       456
          6       0.80      0.90      0.85       462
          7       0.78      0.85      0.81       512
          8       0.86      0.68      0.76       489
          9       0.91      0.72      0.81       520

avg / total       0.83      0.82      0.81      5000

configuration:
  - kernel sigmoid
  - C = 0.1
  - max_iter 200
score = 0.775
             precision    recall  f1-score   support

          0       0.81      0.96      0.88       460
          1       0.67      0.98      0.80       571
          2       0.89      0.71      0.79       530
          3       0.69      0.85      0.76       500
          4       0.82      0.85      0.83       500
          5       0.87      0.43      0.57       456
          6       0.74      0.88      0.81       462
          7       0.70      0.84      0.77       512
          8       0.88      0.59      0.71       489
          9       0.92      0.64      0.75       520

avg / total       0.80      0.78      0.77      5000

As we can see the best accuracy 88.98% was reached when using the linear kernel function with C = 0.1

Now since the best kernel was the linear we will try it with a higher value C = 10

configuration:
  - kernel linear
  - C = 10
  - max_iter 200
score = 0.8768
             precision    recall  f1-score   support

          0       0.91      0.94      0.93       460
          1       0.94      0.98      0.96       571
          2       0.89      0.84      0.86       530
          3       0.82      0.86      0.84       500
          4       0.89      0.89      0.89       500
          5       0.84      0.82      0.83       456
          6       0.92      0.90      0.91       462
          7       0.89      0.87      0.88       512
          8       0.81      0.79      0.80       489
          9       0.87      0.85      0.86       520

avg / total       0.88      0.88      0.88      5000



This is the plotting for the validation and training errors when using SVC with linear kernel and C = 10

* IMAGE GOES HERE
