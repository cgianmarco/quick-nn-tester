# digit-recognition-desktop
A desktop app for Keras based digit recognition

## Installing

```
git clone https://github.com/cgianmarco/keras_tester.git

cd keras_tester

python setup.py install
```

## Usage

```
from keras_tester.tester import Tester

tester = Tester()
```

## Retraining (not tested yet)

```
from keras_tester.trainer import Trainer

trainer = Trainer()

trainer.train()

```
## Retraining with data augmentation(not tested yet)

```
from keras_tester.trainer import Trainer

trainer = Trainer()

trainer.train_augmented()
