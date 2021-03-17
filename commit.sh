printf "What is your default branch(main or master):"
read branch

printf "\nWhat commit message would you like to use:"
read message


git add .
git commit -m "$message"
git push -u origin $branch
