'''
============================================================
AWS EBS — Elastic Block Store
============================================================

EBS = Persistent Block Storage for EC2

Think:

EC2
 ↓
EBS Volume
 ↓
Disk / Storage


WHY EBS?
--------

EC2 provides the compute.

EBS provides persistent disk storage.

Example:

EC2
 ├── CPU
 ├── RAM
 └── EBS
       ↓
      Data


IMPORTANT
---------

EBS is different from S3.

EBS
→ Block storage
→ Commonly attached to EC2
→ Behaves like a disk

S3
→ Object storage
→ Stores files/objects
→ Accessed through APIs


BASIC ARCHITECTURE
------------------

EC2 Instance
     ↓
EBS Volume
     ↓
Filesystem
     ↓
Application Data


EBS VOLUME
----------

A volume is a virtual disk.

Example:

EC2
 ↓
100 GB EBS Volume
 ↓
/data


PERSISTENCE
-----------

If an EC2 instance is stopped:

    EC2 → stopped
    EBS → normally remains

If an EC2 instance is terminated:

    EBS behavior depends on
    DeleteOnTermination setting.


SNAPSHOT
--------

Snapshot = Point-in-time backup of an EBS volume.

EBS Volume
    ↓
 Snapshot
    ↓
 Backup / Restore


IMPORTANT COMMANDS
------------------

List EBS volumes:

aws ec2 describe-volumes


Check snapshots:

aws ec2 describe-snapshots \
    --owner-ids self


Check volumes attached to an instance:

aws ec2 describe-volumes \
    --filters Name=attachment.instance-id,Values=INSTANCE_ID


COST SAFETY
-----------

EBS is BILLABLE storage.

Important:

❌ Don't create unnecessary volumes
❌ Don't keep unused volumes/snapshots
❌ Check resources before deleting anything


EC2 STORAGE MODEL
-----------------

EC2
 │
 ├── Compute
 │    ├── CPU
 │    └── RAM
 │
 └── EBS
      └── Persistent Disk


REMEMBER
--------

EC2 = Compute
EBS = Block Storage
S3  = Object Storage
Snapshot = EBS backup

============================================================
'''