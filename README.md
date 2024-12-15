# ppe-detection
ppe-detection-project

To create an iOS app with the provided Kivy-based Python code, you need to follow these steps using the Kivy framework and `kivy-ios`. The `kivy-ios` toolchain is used to compile Kivy apps for iOS devices.

### Steps to Build an iOS App with Kivy

#### 1. **Set Up Your Environment**
   - **macOS Requirement**: You must have a Mac with Xcode installed to build iOS apps.
   - **Install Xcode**: Download Xcode from the Mac App Store.
   - **Command-Line Tools**: Open a terminal and run:
     ```bash
     xcode-select --install
     ```

#### 2. **Install `kivy-ios`**
   - Install `kivy-ios` to create an iOS-specific build of your app:
     ```bash
     git clone https://github.com/kivy/kivy-ios
     cd kivy-ios
     python3 -m pip install -r requirements.txt
     python3 toolchain.py build python3 kivy pillow cv2 ultralytics
     ```

   This will build the necessary dependencies, including Python, Kivy, and the libraries used in your app (`ultralytics`, `cv2`, etc.).

#### 3. **Prepare Your Project**
   - Place your Kivy app code (`main.py`) in a directory. Include any additional resources, such as model weights (`yolov8n.pt`), images, and the `results` folder.
   - Ensure your project structure is as follows:
     ```
     MyApp/
       main.py
       yolov8n.pt
       results/
     ```

#### 4. **Create the iOS Project**
   - Navigate to the `kivy-ios` directory and create an Xcode project for your app:
     ```bash
     python3 toolchain.py create MyApp ~/Desktop/MyApp
     ```
   - Replace `MyApp` with your desired app name. The second argument is the path to your app directory.

#### 5. **Build the iOS App**
   - Use `toolchain.py` to build the app:
     ```bash
     python3 toolchain.py build MyApp
     ```
   - After building, the `.xcodeproj` file for your app will be created in the specified directory.

#### 6. **Open in Xcode**
   - Open the generated Xcode project:
     ```bash
     open ~/Desktop/MyApp-ios/MyApp.xcodeproj
     ```
   - In Xcode:
     - Set the **Team** in the Signing & Capabilities tab to your Apple Developer Account.
     - Ensure the deployment target matches your connected iOS device.

#### 7. **Run the App on iOS**
   - Connect your iOS device to the Mac.
   - Select your device as the build target in Xcode.
   - Click **Run** to build and deploy the app to your iOS device.

#### 8. **Test Your App**
   - Launch the app on your iOS device.
   - The app will allow you to select an image, process it with YOLOv8, and display the results with bounding boxes.

### Notes
- Ensure all dependencies (e.g., `ultralytics`, `cv2`) are successfully built for iOS during the `toolchain.py build` step.
- If you encounter issues with library compatibility, you may need to adjust the build settings or provide alternative dependencies.