#!/bin/bash

LOGFILE="processLog.txt"

logMessage() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$LOGFILE"
}

# Start a long-running process in the background
(
    for i in {1..10}; do
        echo $i
        sleep 1
    done
    logMessage "Process $$ ended"
) &

# Capture the PID of the background process
PID=$!  # Capture the PID of the last background command

# Log the PID
logMessage "Started background process with PID: $PID"

# Give the process some time to run
sleep 3

# Check if the process is still running before trying to kill it
if ps -p $PID > /dev/null; then
    logMessage "Killing the process with PID: $PID"
    kill $PID

    # Optionally wait for the process to terminate
    wait $PID 2>/dev/null
    logMessage "Process with PID $PID has been killed."
else
    logMessage "Process with PID $PID is not running."
fi