#!/bin/bash

# Store the current directory
initial_dir=$(pwd)

# Change to the ../extras/tailwind directory
cd ../extras/tailwind

# Function to execute when the script is interrupted
cleanup() {
  # Return to the initial directory
  cd "$initial_dir"
}

# Register the cleanup function to be executed on interrupt
trap cleanup SIGINT

# Run npm run dev
npm run dev

# Return to the initial directory when npm run dev finishes
cleanup

