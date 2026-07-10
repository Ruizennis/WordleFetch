#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define the alias command
ALIAS_CMD="alias wordle='(cd \"$SCRIPT_DIR\" && python Run.py)'"

# Detect the user's shell profile
if [ -n "$ZSH_VERSION" ] || [ -f "$HOME/.zshrc" ]; then
    PROFILE="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    PROFILE="$HOME/.bashrc"
elif [ -f "$HOME/.bash_profile" ]; then
    PROFILE="$HOME/.bash_profile"
else
    PROFILE="$HOME/.profile"
fi

# Check if the alias already exists to prevent duplicate lines
if grep -q "alias wordle=" "$PROFILE"; then
    echo "🔄 'wordle' alias already exists in $PROFILE. Updating it..."
    # Remove the old alias line
    sed -i.bak "/alias wordle=/d" "$PROFILE" && rm -f "${PROFILE}.bak"
fi

#  Append the alias to the profile
echo "$ALIAS_CMD" >> "$PROFILE"

echo "Successfully Added 'wordle' alias to $PROFILE"
echo " Run 'source $PROFILE' or restart your terminal to start using it."
