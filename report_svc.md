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
score = ???
