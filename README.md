# Aligner-Application
Team 5


Mitul Garg (2020102026)    
Atharv Sujlegaonkar(2020102025)
# Running the Aligner

This README provides step-by-step instructions for running the aligner and setting up the required environment and dependencies.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- `gcc` (GNU Compiler Collection)
- `ffmpeg`
- `espeak`
- `libespeak-dev`

## Step 1: Install Aeneas Dependencies

Use the following command to install the necessary dependencies, including `ffmpeg`, `espeak`, and `libespeak-dev`. You might need root (sudo) access for this.

```
sudo apt install ffmpeg espeak libespeak-dev
```
## Step 2: Install the Python Environemnt
Inside the folder initialise the Python environment needed for the Aeneas.

```
python -m venv env_align
source env_align/bin/activate
```

# Step 3: Installing Backend Dependencies

Install Flask, which runs our Backend in the Backend Folder.

```
pip install flask 
```
# Step 4: Installing Aeneas Dependencies
```
pip install numpy
pip install aeneas
```
# Step 5: Initiallizing the Frontend 

Inside the frontend folder run :
```
npm i
```

## Step 6: Running the Code

In Backend :

```
python3 main.py
```
In Frontend :

```
npm start
```
