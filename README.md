# Automation Execution Framework

This is sample Automation framework to test an Android App.

## Getting Started

This automation framework is a work in process, it was specifically designed to be simple for a candidate to add new features to it.

### Prerequisites

All required libraries are up to date in the projects requirement document.

### Setting up a virtual environment

In Python, each project may have separate libraries that they use. So, it is best to create separate virtual environment for each python project.

To create a virtual environment, navigate to the location where you want the folder to contain the virtual environment libraries to be located and run the commands below

```
python -m venv <virtual environment folder name>
```

Once created, the virtual environment needs to be activated. This can be done by navigating to the newly created folder and locating the 'bin' folder and run the commands below

```
activate.bat
```

Once virtual environments are created, run below to install all required libraries
```
pip install -r requirements.txt
```

#### Other Libraries required

##### Android Studio
We use Android Studio to bring up the Android Emulator to run the Application

[Android Studio Download](https://developer.android.com/studio/index.html)

##### Appium
Appium is the server that is used to connect to Emulator or physical device

[Appium Desktop Download](https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4)

##### Appium Inspector
Appium inspector is used to inspect the elements within the Android App

[Appium Inspector](https://github.com/appium/appium-inspector/releases)

#### Run Configuration
To run the test, simply navigate to the folder with the test cases and run the command below:
```
behave --tags=fav
```
