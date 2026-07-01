#!/bin/bash
THRESHOLD=85
USAGE=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "[ALERT $(date +%H:%M:%S)] Disk usage is ${USAGE}% (threshold: ${THRESHOLD}%)"
    echo "$(date): DISK ${USAGE}%" >> logs/disk_alerts.log
else
    echo "Disk OK: ${USAGE}% used"
fi
