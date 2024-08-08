#!/bin/bash

# Install pyinstaller
pip install pyinstaller

# Create the executable
pyinstaller --onefile game.py

# Move the executable to the dist folder
mv dist/game ./game-executable

# Upload the executable to S3
aws s3 cp ./game-executable s3://builddb/game
