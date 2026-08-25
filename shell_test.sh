#!/bin/bash

# ==============================================================================
# Script Name: sys_utility.sh
# Description: Performs a quick disk space check and simulates a backup task.
# Usage:       ./sys_utility.sh [target_directory]
# ==============================================================================

# Exit immediately if a command exits with a non-zero status
set -e

# Define color codes for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 1. Check if a directory argument was provided; otherwise use default
TARGET_DIR="${1:-$HOME/Documents}"

echo -e "${YELLOW}=== Starting System Utility Script ===${NC}"
echo "Target Directory: $TARGET_DIR"

# 2. Verify if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}Error: Directory '$TARGET_DIR' does not exist.${NC}"
    exit 1
fi

# 3. Perform a disk space check on the root file system
echo -e "\n${YELLOW}--- Checking Disk Usage ---${NC}"
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "Current root partition usage: ${DISK_USAGE}%"

if [ "$DISK_USAGE" -gt 85 ]; then
    echo -e "${RED}Warning: Disk usage is critically high!${NC}"
else
    echo -e "${GREEN}Disk usage is within safe limits.${NC}"
fi

# 4. Simulate a backup process using a loop over files
echo -e "\n${YELLOW}--- Simulating Backup of Text Files ---${NC}"
FILE_COUNT=0

for file in "$TARGET_DIR"/*.txt; do
    # Check if any .txt files actually exist
    if [ -e "$file" ]; then
        echo "Backing up: $(basename "$file")..."
        ((FILE_COUNT++))
    fi
done

if [ "$FILE_COUNT" -eq 0 ]; then
    echo "No .txt files found to back up in $TARGET_DIR."
else
    echo -e "${GREEN}Successfully processed $FILE_COUNT file(s).${NC}"
fi

echo -e "\n${YELLOW}=== Script Completed Successfully ===${NC}"
