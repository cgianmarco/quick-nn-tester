import sys
from PyQt4.Qt import *
from predict import *


class Canvas(QWidget):

    def __init__(self):
        super(Canvas, self).__init__()
        self.pressed = False
        self.passed_points = []

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        painter.setPen(QColor(0, 0, 0))
        painter.setBrush(QColor(0, 0, 0))

        for point in self.passed_points:
            painter.drawEllipse(point, 10, 10)

        painter.end()

    def mousePressEvent(self, QMouseEvent):
        self.pressed = True
        position = QMouseEvent.pos()
        if position not in self.passed_points:
            self.passed_points.append(position)
        self.repaint()

    def mouseMoveEvent(self, QMouseEvent):
        if (self.pressed):
            position = QMouseEvent.pos()
            if position not in self.passed_points:
                self.passed_points.append(position)
            self.repaint()

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressed = False


    def resize(self, pixelmap):
        # resize and convert to Image
        pixelmap = pixelmap.scaledToHeight(28)
        pixelmap = pixelmap.scaledToWidth(28)
        img = pixelmap.toImage()

        # save image
        img.save("../checkpoints/test.png")

        return img

    def get_pixels(self, img):

        pixels = []
        for i in range(28):
            pixels.append([])
            for j in range(28):
                pixels[i].append(1 - QColor(img.pixel(j, i)).getRgbF()[0])

        return pixels

    def process_pixels(self):
        # grab Canvas pixels
        pixelmap = QPixmap.grabWidget(self)

        # resize pixels and convert to Image
        resized_image = self.resize(pixelmap)

        # make prediction with pixels as input
        predict(self.get_pixels(resized_image))

        # empty canvas
        self.passed_points = []
        self.repaint()







class Tester():
    def __init__(self):
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle("Digit Recognizer")
        window.show()

        canvas = Canvas()
        canvas.setPalette(QPalette(QColor(255, 255, 255)))
        canvas.setAutoFillBackground(True)
        canvas.setPalette(QPalette(QColor(255, 255, 255)))
        canvas.setAutoFillBackground(True)
        canvas.setFixedSize(280, 280)

        button = QPushButton('Recognize')
        button.setFixedSize(290, 50)
        button.clicked.connect(canvas.process_pixels)

        layout = QGridLayout(window)
        layout.addWidget(canvas, 0, 0)
        layout.addWidget(button, 1, 0)
        layout.setRowStretch(1, 1)
        window.setGeometry(300, 300, 300, 300)
        sys.exit(app.exec_())
