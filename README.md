# digit-recognition-desktop
A desktop app for Keras based digit recognition

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
