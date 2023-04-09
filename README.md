# Scraping

This repository contains various Python scripts to check web scraping techniques for certain sites.

**How we can use on our local machine?**

Make sure your OS has already installed `Python 3.x.x` , that comes with `pip`, `pip` is a package manager for Python and is included by default with the Python installer. It helps to install and uninstall Python packages (such as Django!).

**Setting up a virtual environment:**

After cloning this repo, enter the following command on your terminal:

    python -m venv venv

It will create the virtual environment for the following project, where we will install all our project dependencies. There is a `venv` directory automatically created in your project that Git will not track.

After that we have to activate the virtual environment and install the project dependencies there.

**For Windows:**

Enter the following command at the root of your cloned repo.

    venv\Scripts\activate

**For Unix:**

Enter the following command at the root of your cloned repo.

    . venv\bin\activate

**Install dependencies:**

    pip install -r requirements.txt