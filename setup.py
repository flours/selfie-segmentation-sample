import setuptools


setuptools.setup(
    name="selfieSegmentationSample",
    version="0.1.0",
    author="flours",
    description="selfie segmentation sample",
    url="https://github.com/flours/selfie-segmentation-sample",
    install_requires=["opencv-python","numpy","mediapipe"],
    package_data={'selfie_segmentation_sample':['*.mp4']},
    packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    entry_points = {
        'console_scripts': ['selfie_segmentation=selfie_segmentation_sample.main:main']
    },
    python_requires='>=3.1',
)
