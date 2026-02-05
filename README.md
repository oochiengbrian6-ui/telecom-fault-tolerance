# telecom-fault-tolerance
Fault Tolerance 
# Telecom Fault Tolerance Assignment

## Dataset

| Node | CPU (%) | Memory (GB) | Latency (ms) | Throughput (Mbps) | FailureType | Services |
|------|---------|-------------|--------------|-------------------|-------------|----------|
| Edge1 | 45 | 4 | 12 | 500 | Crash | RPCCall, DataReplication |
| Edge2 | 50 | 4.5 | 15 | 470 | Omission | RPCCall, Migration |
| Core1 | 65 | 8 | 8 | 980 | Byzantine | TransactionCommit |
| Core2 | 58 | 7 | 10 | 950 | Crash | Recovery, LoadBalancing |
| Cloud1 | 72 | 16 | 22 | 1250 | Omission | Analytics, RPCCall |

## Files
- analysis.txt - Task (a)
- failover.py - Task (b)
- file_system.py - Task (c)
- integration.py - Task (d)
```

4. **Scroll down**, commit message: `update readme`
5. Click **"Commit changes"**

---

### **Step 3: Task (a) - Analysis**

1. Click **"Add file"** → **"Create new file"**
2. **Name:** `analysis.txt`
3. **Paste:**
```
Task (a): Identify nodes most likely to cause system failure

ANALYSIS:

1. Core1 - HIGHEST RISK
   - Byzantine failure type is the most dangerous
   - Can send wrong data to other nodes
   - Handles TransactionCommit which is critical
   - Byzantine faults are hard to detect

2. Cloud1 - HIGH RISK  
   - Using 72% CPU (highest in system)
   - High latency at 22ms
   - If it fails, Analytics and RPCCall services go down
   - Omission failures mean requests get dropped

3. Core2 - MEDIUM RISK
   - Runs Recovery and LoadBalancing services
   - If recovery system crashes, we can't recover from other failures
   - Creates single point of failure

4. Edge2 - LOW-MEDIUM RISK
   - Omission failures on migration could lose data during transfers
   - 50% CPU is manageable

5. Edge1 - LOWEST RISK
   - Only 45% CPU usage
   - Crash failures are easiest to detect and fix
   - Best latency at 12ms

CONCLUSION:
Core1 Byzantine failure is most critical because it can corrupt the whole system.
Cloud1 is overloaded and needs backup.
