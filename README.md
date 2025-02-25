# Bouncing Logo Video Generator

This Python script generates a video of a bouncing logo using `Pygame` and `MoviePy`. The logo moves around the screen, bouncing off the edges with random speed and direction variations, creating a dynamic and visually interesting effect.

## Features
- **Customizable Logo**: Use any image file as the bouncing logo.
- **Random Speed and Direction**: The logo's speed and direction vary slightly on each bounce, making the movement more natural and unpredictable.
- **Video Output**: The animation is saved as an MP4 video file.

## Requirements
- Python 3.x
- Pygame
- MoviePy
- NumPy

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pmatty/Bouncing-Logo.git
   cd bouncing-logo-video-generator
   ```

2. **Install Dependencies**:
   Install the required Python packages using `pip`:
   ```bash
   pip install pygame moviepy numpy
   ```

## Usage
1. **Place Your Logo**:
   - Save your logo image file (e.g., `logo.png`) in the same directory as the script.

2. **Run the Script**:
   - Execute the script using Python:
     ```bash
     python bouncing_logo.py
     ```
   - When prompted, enter the name of your image file (e.g., `logo.png`).

3. **Output**:
   - The script will generate a video file named after your input image (e.g., `logo.mp4`) in the same directory.

## Customization
- **Video Settings**:
  - You can adjust the video settings in the script, such as:
    - `WIDTH` and `HEIGHT`: Resolution of the video.
    - `FPS`: Frames per second.
    - `DURATION`: Duration of the video in seconds.
    - `SIZE`: Maximum size of the logo.

- **Speed and Randomness**:
  - Modify the `BASE_SPEED` and `SPEED_VARIATION` variables to control the logo's speed and randomness.

## Example
```bash
python bouncing_logo.py
Enter the image file name: logo.png
Video saved as: logo.mp4
```

## Output Video
The generated video will show your logo bouncing around the screen with random speed and direction variations.

## License
This project is licensed under the MIT License.