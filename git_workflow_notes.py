
# DAY 12: GIT PRACTICE
# Git keeps a record of the changes made to your code.
# Git: Helps you track code changes on your computer.
# GitHub: Keeps your code online and helps developers work together.
# mkdir: Creates a new folder.
# cd: Moves the terminal into another folder.
# git init: Creates a Git repository in the current folder.
# git status: Shows the current state of your repository.
# git diff: Displays the changes made to your files.
# git add: Selects changes to include in the next commit.
# git commit: Saves the selected changes in Git history.
# git branch: Lists the branches in your repository.
# git switch: Moves you from one branch to another.
# -c: Creates a new branch and switches to it.
# git push: Uploads local commits to GitHub.
# git pull: Downloads and integrates changes from GitHub.
# Pull Request: Allows changes to be reviewed before merging.

# DAY 12: GIT & PULL REQUEST WORKFLOW
# Goal: Practise branches, commits, GitHub push, and Pull Requests.
# Run Git commands in the VS Code terminal, not in this Python file.

# STEP 1: Check Git and repository information
# git --version
# git status
# git branch
# git log --oneline

# STEP 2: Create and switch to a feature branch
# Our feature branch is feature/git-workflow-practice.
# We created this branch after making the initial commit.
# Command used:
# git switch -c feature/git-workflow-practice

# STEP 3: Create and update git_practice.py
# We added a new print statement to the existing file.
# The following is the final code in git_practice.py:
# print("Welcome to Git")
# print("Understanding version control")
# print("I am practicing Git commands")
# print("Learning how branches and pull requests work")
# print("My first feature branch is ready")

# STEP 4: Run the Python file
# Command: python git_practice.py
# This command runs the Python file and displays its output.

# STEP 5: Review, stage, and commit changes
# git status
# git diff
# git add git_practice.py
# git commit -m "Add feature branch message"
# git log --oneline --graph --all

# STEP 6: Connect the local repository to GitHub
# Create an empty GitHub repository first.
# Replace YOUR_USERNAME with your GitHub username.
# git remote add origin https://github.com/YOUR_USERNAME/Day12_Git_Pull_Request_Workflow.git
# git remote -v

# STEP 7: Push the branches to GitHub
# git push -u origin master
# git push -u origin feature/git-workflow-practice
# These commands upload both branches to GitHub.

# STEP 8: Create a Pull Request on GitHub
# Base branch: master
# Compare branch: feature/git-workflow-practice
# Title: Add feature branch message
# Review the changed files before merging the Pull Request.
# Merge only after the review and any required approvals.

# STEP 9: Update the local master branch after merging
# git switch master
# git pull origin master

# STEP 10: Verify the final result
# python git_practice.py
# git log --oneline --graph --all
# git status

# EXPECTED OUTPUT:
# Welcome to Git
# Understanding version control
# I am practicing Git commands
# Learning how branches and pull requests work
# My first feature branch is ready

# IMPORTANT:
# Check git status before switching branches.
# If the feature branch already exists, use:
# git switch feature/git-workflow-practice
# Resolve any merge conflicts before continuing.
# Never force-push or overwrite existing work.
# Keep virtual environments and unnecessary files out of Git.
