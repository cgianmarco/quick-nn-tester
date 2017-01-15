# quick-nn-tester
A desktop app for Keras based digit recognition

Here's what it looks like:

https://github.com/cgianmarco/quick-nn-tester/blob/master/www.GIFCreator.me_U4Llz9%20(1).gif



## Installing

```
git clone https://github.com/cgianmarco/quick-nn-tester.git

cd quick-nn-tester

python setup.py install
```

## Usage

```
from NNTester.tester import Tester

tester = Tester()
```

## Retraining

```
from NNTester.trainer import Trainer

trainer = Trainer()

trainer.train()

```
## Retraining with data augmentation

```
from NNTester.trainer import Trainer

trainer = Trainer()

trainer.train_augmented()


