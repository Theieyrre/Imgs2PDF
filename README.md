![badge](https://img.shields.io/static/v1?label=CODE&message=RUNNING&color=green&style=for-the-badge&logo=appveyor)

# Imgs2PDF

Simple Python script to read multiple images in a directory to create a multi-page PDF file  
Images can be JPG, JPEG or PNG  
Doesn't support recursive directories

# How to use

## Requirements

- Python3.10+

Run line below to install dependiencies

```
pip install -r requirements.txt
```

To run create PDF file

```
python run.py <directory-name> <filename>
```

will create \<filename> in the active directory  
Make sure to add .pdf in filename

If there are seperate directories use multi run

```
python multi_run.py <main-directory-name> <output-directory>
```

will create pdf file with name of each sub-directory in output-directory

If nested directories exist run recursive_run

```
python recursive_run.py <main-directory-name> <output-directory>
```

will read nested directories, create and merge pdfs to crete \<main-directory-name>.pdf
