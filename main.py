from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image as KivyImage
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
import cv2

from model import yolov8_image_processing


class YOLOApp(App):
    def __init__(self, **kwargs):
        super().__init__()
        self.image_display = None
        self.process_button = None
        self.filechooser = None
        self.label = None
        self.layout = None
        self.output_dir = None
        self.model_path = None

    def build(self):
        self.model_path = "model/trained_model.pt"  # Path to YOLOv8 model weights
        self.output_dir = "results"  # Directory to save processed images
        self.layout = BoxLayout(orientation="vertical")

        self.label = Label(text="Select an image to process")
        self.layout.add_widget(self.label)

        self.filechooser = FileChooserIconView()
        self.layout.add_widget(self.filechooser)

        self.process_button = Button(text="Process Image")
        self.process_button.bind(on_press=self.process_image)
        self.layout.add_widget(self.process_button)

        self.image_display = KivyImage()
        self.layout.add_widget(self.image_display)

        return self.layout

    def process_image(self, instance):
        selected = self.filechooser.selection
        if selected:
            input_image_path = selected[0]
            self.label.text = f"Processing: {input_image_path}"
            try:
                # Process the image using YOLOv8
                processed_image_path = yolov8_image_processing(model_path=self.model_path, source=input_image_path, output_dir=self.output_dir, conf=0.50)

                # Load and display the processed image
                img = cv2.imread(processed_image_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb')
                texture.blit_buffer(img.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
                texture.flip_vertical()
                self.image_display.texture = texture

                self.label.text = f"Processed image saved to: {processed_image_path}"
            except Exception as e:
                self.label.text = f"Error: {str(e)}"

if __name__ == "__main__":
    YOLOApp().run()
