from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_window import Ui_window
from PySide6.QtCore import *
import os
import time
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction, get_prediction
import os
import glob
from PIL import Image  # 需要安装Pillow库



class DraggableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Drag an image here")
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() and len(event.mimeData().urls()) == 1:
            url = event.mimeData().urls()[0]
            if url.isLocalFile() and QImageReader.imageFormat(url.toLocalFile()):
                event.acceptProposedAction()

    def dropEvent(self, event):
        url = event.mimeData().urls()[0]
        if url.isLocalFile():
            file_path = url.toLocalFile()
            self.load_image(file_path)   # 当拖拽的数据被放下时会被触发。它从拖拽事件中获取第一个URL，并检查是否是本地文件。

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            self.setPixmap(pixmap)
            self.setScaledContents(True)
            self.setText("")  # Clear the text   的 load_image 方法用于加载图像文件并在 DraggableLabel 上显示图像

        else:
            self.setText("Invalid image file")


class NotDraggableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Result")  # 创建一个简单的标签，用于显示结果或其他文本信息，而不支持拖拽操作。


class InferenceResultDialog(QDialog):   # 你提供的代码定义了一个名为 InferenceResultDialog 的自定义 QDialog 子类。QDialog 是 PyQt 或 PySide 中的一个小部件，用于创建对话框窗口，通常用于显示一些用户界面元素和接收用户输入。
    def __init__(self, inference_results, duration, confidence, model):  #   继承自 QDialog，用于显示推理结果的对话框窗口。我会逐一解释这段代码的各个部分以帮助你理解它的功能：
        super().__init__()

        self.setWindowTitle("Inference Results")
        self.setLayout(QVBoxLayout())  # Set the dialog layout
        self.layout().setContentsMargins(20, 20, 20, 20)  # Add margins for spacing

        # Set a rounded and modern background color
        self.setStyleSheet("background-color: rgb(192, 192, 192); border: 1px solid rgb(128, 128, 128);")

        info_box = QGroupBox()
        info_box.setStyleSheet(
            "QWidget { border: 1px solid rgb(0, 122, 204); background-color: rgb(173, 216, 230); border-radius: 0px; }")

        info_layout = QVBoxLayout()

        # Add labels for confidence, duration, and resolution
        settings_label = QLabel("Settings")
        settings_label.setStyleSheet(" font-weight: bold; font-size: 16px;")
        model_label = QLabel(f" Model :  {model} ")
        confidence_label = QLabel(f" Confidence Treshold :  {confidence} ")
        duration_label = QLabel(f" Duration:  {duration:.2f}  seconds")

        # Add labels to the info layout
        info_layout.addWidget(settings_label)
        info_layout.addWidget(model_label)
        info_layout.addWidget(confidence_label)
        info_layout.addWidget(duration_label)

        # Set the layout for the info box
        info_box.setLayout(info_layout)

        # Add the info box to the main layout
        self.layout().addWidget(info_box)

        # Seperator
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setLineWidth(2)
        line.setStyleSheet(
            "background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));")
        self.layout().addWidget(line)

        # results
        inference_label = QLabel("Inference Results ")
        inference_label.setStyleSheet(" font-weight: bold; font-size: 16px;")
        self.layout().addWidget(inference_label)

        for result in inference_results:
            object_name = result.category.name
            probability = result.score.value

            result_layout = QVBoxLayout()  # Layout for each result row

            object_label = QLabel(object_name)

            result_layout.addWidget(object_label)

            # Add a spacer item for spacing between object name and progress bar
            spacer = QSpacerItem(
                20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
            result_layout.addItem(spacer)

            progress_bar = QProgressBar()
            progress_bar.setRange(0, 100)
            progress_bar.setValue(int(probability))
            progress_bar.setFormat(f"{probability * 100:.2f}%")
            progress_bar.setStyleSheet("""
                            QProgressBar {
                                background-color: white;
                                border: 2px solid #dcdcdc; /* 边框颜色需要加 solid */
                                height: 2px;
                                text-align: center;
                            }
                            QProgressBar::chunk {
                                background-color: #00FFFF; /* 青色 */
                                width: 20px; /* 细线宽度 */
                                height: 2px;
                                margin: 0px;
                                border-radius: 0px; /* 取消圆角 */
                            }
            """)

            result_layout.addWidget(progress_bar)

            # Create a widget for each result row
            result_widget = QWidget()
            result_widget.setStyleSheet(
                "QWidget { border: 1px solid rgb(0, 122, 204); background-color: rgb(173, 216, 230); border-radius: 0px; }")

            result_widget.setLayout(result_layout)
            self.layout().addWidget(result_widget)
        # Create QDialogButtonBox with OK and Save buttons
        button_box = QDialogButtonBox()
        ok_button = QPushButton("OK")
        save_button = QPushButton("Save")
        self.button_style(ok_button)
        self.button_style(save_button)

        # Connect buttons to respective functions
        ok_button.clicked.connect(self.accept)
        # Connect to the new function
        save_button.clicked.connect(self.save_dialog_image)

        button_box.addButton(ok_button, QDialogButtonBox.AcceptRole)
        button_box.addButton(save_button, QDialogButtonBox.ActionRole)

        # Add button box to the layout
        self.layout().addWidget(button_box)

    def save_dialog_image(self):   # 于保存对话框中显示的图像
        dialog_image = self.get_dialog_image()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Inference Results", "", "Image Files (*.png *.jpg *.jpeg)", options=options)

        if file_name:
            dialog_image.save(file_name)

    def get_dialog_image(self):  # 目的是捕获对话框中的图像，以便后续保存或进行其他操作
        pixmap = QPixmap(self.size())
        self.render(pixmap)
        return pixmap.toImage()

    def button_style(self, button):
        button.setStyleSheet(
            "QPushButton {"
            "   background-color: yellow;"
            "   border-radius: 10px;"
            "   color: red;"
            "   padding: 10px 20px;"
            "   font-size: 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: red;"
            "}"
        )


class window(QMainWindow, Ui_window):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("YOLOV8 GUI")
        self.char_label.setText('Detection')
        # self.undo_button.deleteLater()
        self.lineEdit_4.deleteLater()
        self.lineEdit.deleteLater()
        self.label_6.setText('Resolutions')
        self.label_7.setText('Objects')
        self.lineEdit_2.deleteLater()
        self.lineEdit_3.deleteLater()
        self.label_2 = QLabel('--')
        self.label_2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_2.setStyleSheet(
            "color: black; font-weight: bold; font-size: 16px;")
        self.verticalLayout_10.addWidget(self.label_2)
        self.label_3 = QLabel('--')
        self.label_3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_3.setStyleSheet(
            "color: black; font-weight: bold; font-size: 16px;")
        self.verticalLayout_12.addWidget(self.label_3)

        # The QLabel that holds the input image

        self.pre_image = DraggableLabel(self.splitter)
        self.pre_image.setObjectName(u"pre_image")
        self.pre_image.setMinimumSize(QSize(200, 100))
        font3 = QFont()
        font3.setPointSize(25)
        self.pre_image.setFont(font3)
        self.pre_image.setAcceptDrops(True)
        self.pre_image.setStyleSheet(u"background-color: white;\n"
                                     "border:2px solid rgb(255, 255, 255);\n"
                                     "border-radius:0 ")
        self.pre_image.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.pre_image)

        # The QLabel that holds the result image

        self.res_image = NotDraggableLabel(self.splitter)
        self.res_image.setObjectName(u"res_image")
        self.res_image.setMinimumSize(QSize(200, 100))
        font3 = QFont()
        font3.setPointSize(25)
        self.res_image.setFont(font3)
        self.res_image.setStyleSheet(u"background-color: white;\n"
                                     "border:2px solid rgb(255, 255, 255);\n"
                                     "border-radius:0")
        self.res_image.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.res_image)
        # progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("Waiting For Image ...")
        self.progress_bar.setStyleSheet(
            "QProgressBar {"
            "   background-color: white;"
            "   border: none;"
            "   border-radius: 5px;"
            "   height: 20px;"
            "   text-align: center;"
            "}"
            "QProgressBar::chunk {"
            "   background-color: #8bc34a;"
            "   border-radius: 5px;"
            "}"
        )
        # Increase the font size for the progress bar's text
        font = QFont()
        font.setPointSize(15)
        self.progress_bar.setFont(font)
        self.verticalLayout_16.addWidget(self.progress_bar)
        # Combo box
        self.combo_box = QComboBox()
        self.combo_box.addItem("YOLOv8")
        # self.combo_box.addItem("YOLOv8")
        #  self.combo_box.addItem("YOLO-NAS")
        # self.combo_box.addItem("YOLO-NAS + SAHI")

        # Apply a modern stylesheet to the combo box
        self.combo_box.setStyleSheet("""
                    QComboBox {
                        border: 1px solid black; /* 添加1像素的黑色边框 */
                        padding: 5px;
                        background-color: white; /* 将背景颜色设置为白色 */
                        selection-background-color: #3498db;
                        font-size: 14px;
                        color: white;
                        font-weight: bold;
                        text-align: center;
                    }

                    QComboBox::drop-down {
                        width: 30px;                    
                    }

                    QComboBox::down-arrow {
                        image: url(:/all/img/box_down.png);
                        width: 0;
                        height: 0;
                        border-left: 5px solid transparent;
                        border-right: 5px solid transparent;
                    }
                """)

        self.verticalLayout_14.addWidget(self.combo_box)
        # Confidence Slider
        self.label = QLabel("0.01")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 16px; ")
        self.verticalLayout_8.addWidget(self.label)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)  # Map 0.3 to 30
        slider.setMaximum(100)  # Map 1.0 to 100
        slider.valueChanged.connect(self.slider_value_changed)

        # Apply modern and rounded stylesheet to slider
        slider.setStyleSheet("""
            QSlider {
                background-color: transparent;
                height: 30px;
            }

            QSlider::groove:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #dcdcdc, stop:1 #f0f0f0);
                height: 6px;
                border-radius: 3px;
            }

            QSlider::handle:horizontal {
                background-color: white;
                width: 22px;
                height: 2px;
                border-radius: 11px;
                margin: -8px 0; /* Adjust handle position */
            }
        """)
        self.verticalLayout_8.addWidget(slider)
        # # Undo Button
        # self.undo_button = QPushButton(QIcon("img/stop.png"), "")
        # self.undo_button.setIconSize(QSize(68, 50))  # Set the icon size
        # self.verticalLayout_2.addWidget(self.undo_button)
        # self.undo_button.setStyleSheet("""
        #     QPushButton {
        #         background-color: white; /* Transparent background */
        #         border: none; /* No border */
        #     }
        #
        #     QPushButton:hover {
        #         background-color: white; /* Color when the mouse hovers over the button */
        #     }
        #
        #     QPushButton:pressed {
        #         background-color: white; /* Color when the button is pressed */
        #     }
        # """)

        # Buttons
        self.start_button.pressed.connect(self.loading)
        self.start_button.clicked.connect(self.start_inference)
        self.start_button.clicked.connect(self.text_progress)
        self.save_button.clicked.connect(self.save_image)
        self.files_button.clicked.connect(self.choose_image)
        # self.undo_button.clicked.connect(self.undo)

        # Progress of the bar
        self.inference_running = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0

    def show_inference_results_dialog(self, results, duration, confidence, model):
        results_dialog = InferenceResultDialog(
            results, duration, confidence, model)
        results_dialog.exec()    # 用于显示推理结果的对话框

    def slider_value_changed(self, value):
        scaled_value = value / 100.0
        self.label.setText(f"{scaled_value:.2f}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 滑块控件的值发生变化时的操作

    def text_progress(self):
        try:
            self.progress_bar.setFormat(
                "Displaying Image : %p%")  # Format with percentage

        except Exception as e:
            self.show_error_message(f"Error: {str(e)}")   #  设置了进度条的文本格式，显示图像显示进度的百分比

    def start_inference(self):
        if not self.inference_running:
            self.progress_value = 0  # self.progress_value 设置为0
            self.progress_bar.setValue(self.progress_value)  # 这一行代码将进度条控件的值设置为当前的进度值，即0%
            self.inference_running = True  # self.inference_running = True
            self.start_button.setEnabled(False)  #  将 "start_button" 控件设置为不可用状态，以防止用户在推理过程中再次启动。
            self.timer.start(100)  # 每100毫秒触发一次计时器事件。这个计时器通常用于更新推理的进度。
            self.run_inference()  # 开始实际的推理过程。这是一个自定义的方法，用于执行推理操作。

    def update_progress(self):  #  用于更新推理的进度
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)

        if self.progress_value >= 100:
            self.timer.stop()
            self.inference_running = False
            self.start_button.setEnabled(True)

    def undo(self):  #   方法用于执行撤销操作，恢复到最初的状态。
        if self.pre_image.pixmap():  #  控件是否包含了一个 pixmap（像素图像），如果包含，表示之前有图像被加载。
            self.pre_image.setText("Drag and Drop an Image")
            self.res_image.setText("Result Image Displayed Here")
            self.char_label.setText("Detection")
            self.label_2.setText("---")
            self.label_3.setText("---")
            # Progress of the bar
            self.inference_running = False
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_progress)
            self.progress_value = 0
            self.progress_bar.setFormat("Waiting For Image")

    def choose_image(self):   # 方法用于让用户选择并加载图像。
        # Open a file dialog to get the image path
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Choose Image", "", "Images (*.png *.jpg *.jpeg);;All Files (*)", options=options)

        # If the user cancels the file dialog or doesn't choose an image, return
        if not file_path:
            return

        # Load and display the chosen image in the pre_image QLabel
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            self.pre_image.setPixmap(pixmap)
            self.pre_image.setScaledContents(True)

    def save_image(self):  #  方法用于保存图像。
        # Get the pixmap from the res_image QLabel

        pixmap = self.res_image.pixmap()
        if pixmap is None:
            return

        # Open a file dialog to get the save path
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "Images (*.png *.jpg *.jpeg);;All Files (*)", options=options)

        # If the user cancels the file dialog or doesn't provide a file name, return
        if not file_path:
            return

        # Save the pixmap to the chosen file
        pixmap.save(file_path)

    def loading(self):  #  用于在进行推理之前显示加载状态
        try:
            if self.pre_image.pixmap():
                self.res_image.setText('Loading ...')
                self.progress_bar.setFormat("Preparing for Inference ...")
            else:
                self.res_image.setText('Please Insert an Image ')
                self.undo()
        except Exception as e:
            self.show_error_message(f"Error: {str(e)}")

    def run_inference(self):  # 方法是一个执行推理操作的方法，涉及多个步骤，包括图像处理、模型推理、结果显示等。

        try:
            # Disable the button to prevent multiple inferences
            self.start_button.setEnabled(False)
            # Extract the image from the input QLabel
            input_pixmap = self.pre_image.pixmap()
            self.label_2.setText(" {} x {}".format(
                input_pixmap.width(), input_pixmap.height()))
            if input_pixmap is None:
                self.show_error_message("Error: No input image found.")
                return

            # Convert the pixmap to a PIL Image
            input_image = input_pixmap.toImage()
            image_path = 'demo_data/image.jpg'  # Replace with the desired output image path
            input_image.save(image_path)

            # Perform inference on the image   模型推理

            selected_option = self.combo_box.currentText()
            if selected_option == 'YOLOv8 + SAHI':
                output_image_path, results, duration, confidence, model = self.yolov8_inference_sahi(
                    image_path)  # Perform inference

            elif selected_option == "YOLOv8":
                output_image_path, results, duration, confidence, model = self.yolov8_inference(
                    image_path)

            elif selected_option == "YOLO-NAS":
                output_image_path, results, duration, confidence, model = self.yolo_nas_inference(
                    image_path)

            elif selected_option == "YOLO-NAS + SAHI":
                output_image_path, results, duration, confidence, model = self.yolo_nas_inference_sahi(
                    image_path)

            if output_image_path:
                # Display the output image in the output QLabel
                # progress
                for _ in range(100):
                    time.sleep(0.1)
                    self.update_progress()
                    self.progress_bar.setFormat(
                        "Displaying the Result: %p%")  # Format with percentage
                    self.char_label.setText("Result Image Ready ")
                output_pixmap = QPixmap(output_image_path)
                self.res_image.setPixmap(output_pixmap)
                self.res_image.setScaledContents(True)
                self.res_image.setText("")
                self.start_button.setEnabled(True)

                if selected_option == 'YOLOv8 + SAHI':

                    self.show_inference_results_dialog(
                        results, duration, confidence, model)

                elif selected_option == "YOLOv8":

                    self.show_inference_results_dialog(
                        results, duration, confidence, model)

                elif selected_option == "YOLO-NAS":

                    self.show_inference_results_dialog(
                        results, duration, confidence, model)

                elif selected_option == "YOLO-NAS + SAHI":

                    self.show_inference_results_dialog(
                        results, duration, confidence, model)

        except Exception as e:
            self.progress_bar.setValue(100)
            self.timer.stop()
            self.inference_running = False
            self.start_button.setEnabled(True)
            self.progress_bar.setStyleSheet(
                "QProgressBar {"
                "   background-color: rgb(220, 20, 60);")
            self.progress_bar.setFormat("Inference Failed")
            self.show_error_message("Error: Inference failed.")
            self.char_label.setText('Detection Failed')
            self.progress_bar.setFormat("Failed ")
            self.show_error_message(f"Error: {str(e)}")
        finally:

            # Deletes Images after inference
            os.remove(output_image_path)
            os.remove(image_path)

    # The YOLOv8-SAHI function

    def yolov8_inference_sahi(self, image_path):

        yolov8_model_path = 'models/yolov8l.pt'

        detection_model = AutoDetectionModel.from_pretrained(
            model_type='yolov8',
            model_path=yolov8_model_path,
            confidence_threshold=float(self.label.text()),
            device="cuda:0",  # or 'cpu'
        )

        result = get_sliced_prediction(
            image_path,
            detection_model,
            slice_height=200,
            slice_width=200,
            overlap_height_ratio=0.7,
            overlap_width_ratio=0.7
        )
        confidence_threshold = float(self.label.text())
        model_type = 'yolov8 + sahi'
        output_image_path, results, duration = self.inference_infos(result)
        return output_image_path, results, duration, confidence_threshold, model_type  #  YOLOv8 模型与 SAHI 后处理的图像推理操作

    def yolov8_inference(self, image_path):  # 用于执行 YOLOv8 模型的图像推理操作
        yolov8_model_path = 'models/yolov8l.pt'

        detection_model = AutoDetectionModel.from_pretrained(
            model_type='yolov8',
            model_path=yolov8_model_path,
            confidence_threshold=float(self.label.text()),
            device="cuda:0",  # or 'cpu'
        )
        model_type = 'yolov8'
        confidence_threshold = float(self.label.text())
        result = get_prediction(image_path, detection_model)
        output_image_path, results, duration = self.inference_infos(result)
        return output_image_path, results, duration, confidence_threshold, model_type

    # Note: For Windows, You should have installed Microsoft Visual C++ Build Tools to install super-gradients properly (required for pycocotools)
    def yolo_nas_inference(self, image_path):  # YOLO-NAS 模型的图像推理操作。

        detection_model = AutoDetectionModel.from_pretrained(
            model_type="yolonas",
            model_name="yolo_nas_s",
            confidence_threshold=float(self.label.text()),
            device="cpu",
        )
        confidence_threshold = float(self.label.text())
        model_type = 'yolonas'
        result = get_prediction(image_path, detection_model)
        output_image_path, results, duration = self.inference_infos(result)
        return output_image_path, results, duration, confidence_threshold, model_type

    def yolo_nas_inference_sahi(self, image_path):
        detection_model = AutoDetectionModel.from_pretrained(
            model_type="yolonas",
            model_name="yolo_nas_s",
            confidence_threshold=float(self.label.text()),
            device="cpu",
        )
        result = get_sliced_prediction(
            image_path,
            detection_model,
            slice_height=200,
            slice_width=200,
            overlap_height_ratio=0.7,
            overlap_width_ratio=0.7
        )
        confidence_threshold = float(self.label.text())
        model_type = 'yolo-nas + sahi'
        output_image_path, results, duration = self.inference_infos(result)
        return output_image_path, results, duration, confidence_threshold, model_type   #   用于执行 YOLO-NAS 模型与 SAHI 后处理的图像推理操作。

    def inference_infos(self, result):  # 处理目标检测结果并返回相关信息。
        result.export_visuals(export_dir="demo_data/")
        duration = result.durations_in_seconds["prediction"]
        results = result.object_prediction_list
        number_of_objects_detected = len(result.object_prediction_list)
        self.label_3.setText(f"{number_of_objects_detected}")
        output_image_path = "demo_data/prediction_visual.png"
        return output_image_path, results, duration

    def show_error_message(self, message):  # 用于显示错误消息对话框。
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle('Error')
        msg_box.setText(message)
        msg_box.exec()


