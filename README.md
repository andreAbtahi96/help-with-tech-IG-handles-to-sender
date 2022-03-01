# help-with-tech-IG-handles-to-sender
As the war rages on in Ukraine, many of us are on the sidelines. We can unite and help, how ever small or big. Together. This repo was created after joining a slack account called "Help Ukraine". This account is devoted to contribute in aid. Any shape or form. As a developer in the works, I feel guilty not helping Ukraine. This repo is to help with a recent assignment. To simply parse through a text file of Instagram handles, populate the sender section of Instagram's messaging feature. The goal would be to reduce time, and ultimately help reduce the disinformation that is happening in Europe. At this moment, I have my eyes set on using python for this task. 

# Run the following commands in a terminal:

If Homebrew is not installed, run:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  -> When finished check the "==> Next steps:" in the console and follow instructions to enable homebrew

# Install Selenium locally and other Python modules:
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
pip3 install selenium
pip3 install pyyaml

# Install Chromedriver:
brew tap homebrew/cask
brew install --cask chromedriver

# To customize the script:
Change the parameters in the "igbot-input.yaml" file, it should be in the same folder as the script to be picked

# To run the script (from the folder where you put the files):
python3 scriptToPopulate.py


NOTE: if the following message appears: "“chromedriver” can’t be opened because Apple cannot check it for malicious software."
    - Click on "Show in finder"
    - Right click the file and select "Open"
    - Then click "Open" again
    - Close the terminal window that appears
    - This should be enough for Apple to trust the webdriver

NOTE 2: this bot works only for the english Instagram interface
