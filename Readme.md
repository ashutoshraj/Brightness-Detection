# Image Brightness Detector
This project is the Develop a generalized algorithm to detect the brightness of any image. Your algorithm should take an image as input and give a score between (0-10) as output (zero being low bright and 10 being high bright).

### Requirements
- Numpy
- Pillow
- python3
#### For running locally
-   Install Python Packages (pip install -r requirements.txt)
-   python3 main.py --input_path test.png

## Acknowledgments

-   http://alienryderflex.com/hsp.html

-   https://www.whydomath.org/node/wavlets/imagebasics.html

## Pipeline flow

- Check the input image file existence
- Resize all the image to 1280x720, therefore it returns a constant value.
- Create bins of 10 levels from 0 to 255, for quantization of results between 10 levels.
- Get the average pixel level for each channel
- Applied formula of perceived brightness ie. brightness = sqrt( .299 R2 + .587 G2 + .114 B2 )
- Used the binning process in which level it falls. (1 to 10)
