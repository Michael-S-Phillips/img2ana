# Anaglyph Image Creator

This Python script `img2ana.py` allows you to create an anaglyph image from left and right ISIS cube images. Anaglyph images are typically used for 3D visualization, and they combine two slightly offset images to create a single image with a 3D effect when viewed with red-cyan glasses.

## Installation

### 1. Download the Repository from the Google Drive, and place it in folder that makes sense for your computer. OR clone the repository from github with the following command:
```bash
git clone https://github.com/your-username/img2ana.git
```
### 2. Open the terminal and change directories into img2ana

```bash
cd img2ana
```

### 3. Create and Activate the Environment

Before using the script, you need to create a Conda environment with the required dependencies. The environment is defined in environment.yaml. Run the following commands to set it up:
```bash
chmod +x install_env.sh  # Make the script executable (only needed once)
./install_env.sh        # Create the Conda environment
conda activate img2ana  # Activate the environment
```
### 4. Run the Script
Now that you have activated the environment, you can run the img2ana.py script. Here's how to use it:
```bash
python img2ana.py
```

Follow the prompts to provide the paths for the left and right images and specify the output file name (including the file extension, e.g., .png, .jpg). You will also be asked to enter the amount of rotation in degrees (0-360) for the anaglyph image.

### Dependencies

The script relies on the following Python packages, which are automatically installed when you create the Conda environment using environment.yaml:

numpy
gdal
pillow (PIL)
scipy

### Example Usage

Here's an example of how to create an anaglyph image using the script:

Run the script with python img2ana.py.
Provide the paths to the left and right ISIS cube images.
Specify the output file name (e.g., my_anaglyph.png) and the rotation angle (e.g., 30 degrees).
The anaglyph image will be saved in the same directory as the script.