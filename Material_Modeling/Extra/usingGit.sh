
#!/bin/bash  

#credits to :  https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

#Creating a local Repository and connecting it to Remote repository (online)
# 1. To create a local repository Modeling
# 2. Initialize the local directory as a Git repository.
# 3. Add SSH key to your GitHub account online
#    3.1 Checking for existing SSH keys
#    3.2 If you don't have an existing public and private key pair, then generate a new SSH key.
#    3.3 Generating a new SSH key
#        Note1: When you're prompted to "Enter a file in which to save the key," press Enter. 
#        Note2: paraphrases is Password
#    3.4 Add your SSH key to the ssh-agent
#    3.5 Add the SSH key to your GitHub account online
#        3.5.1 Copy the SSH key to your clipboard.
#        3.5.2 Go to online repository and in Profile settings, add ssh keys, paste your SSH key
# 4. Add URL for the remote repository (online) where your local repository will be pushed
# 5. Make changes and add changes
# 6. Commit changes
# 7. push your changes in local repository(head) to remote reposotory(origin)
#    Note: head is th head of your local branch (can be at master or at development local) and origin is online (can be at master or at development local)

mkdir  Modeling 
cd Modeling
git init
ls -al ~/.ssh                                                                                                # Lists the files in your .ssh directory, if they exist
ssh-keygen -t rsa -b 4096 -C "navyanthkusam@gmail.com"                                                     # This creates a new ssh key, using the provided email as a label.
eval $(ssh-agent -s)                                                                                       # start the ssh-agent in the background
ssh-add ~/.ssh/id_rsa                                                                                      # Add your SSH private key to the ssh-agent
clip < ~/.ssh/id_rsa.pub                                                                                   # Copies the contents of the id_rsa.pub file to your clipboard
 
git remote add origin "git@github.com:navyanthkusam/materialModeling.git"
git checkout Development
git pull                           

git add newfileLocal.txt                                                                                 # Adds the files in the local repository and stages them for commit.
                                                                                                         # To unstage a file, use 'git reset HEAD YOUR-FILE'.
git commit -m "my first commit"
git push origin master                                                                     # Commits the tracked changes and prepares them to be pushed to a remote repository. 
                                                                                           #To remove this commit and modify the file, use 'git reset --soft HEAD~1' 

git checkout Development                                                                    #to different branch
 















