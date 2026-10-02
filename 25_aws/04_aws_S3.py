'''
============================================================
AWS S3 — Simple Storage Service
============================================================

S3 = Object Storage

Used to store:
    → Images
    → Videos
    → PDFs
    → Logs
    → Backups
    → ML models
    → MLflow artifacts
    → Static files


S3 STRUCTURE
------------

AWS Account
    ↓
Bucket
    ↓
Objects (Files)
    ↓
Object Key (Path/Name)


Example:

Bucket
└── models/
    ├── model.pkl
    └── model.onnx

S3 does NOT use traditional folders.
Folders are represented through object keys.


BUCKET
------

A bucket is a container for objects.

Example:

my-project-data
    ↓
    images/
    models/
    backups/


OBJECT
------

An object = File + Metadata

Example:

models/model.pkl


IMPORTANT S3 FEATURES
---------------------

✅ High durability
✅ Versioning
✅ Encryption
✅ Access control
✅ Lifecycle rules
✅ Public access blocking


S3 vs DATABASE
--------------

S3
→ Stores files/objects

Database
→ Stores structured data


Example:

ML Model File
    ↓
    S3

Model name
Accuracy
Version
Parameters
    ↓
    Database


IMPORTANT COMMANDS
------------------

List buckets:

aws s3 ls


Create a bucket:

aws s3 mb s3://BUCKET_NAME --region REGION


List objects:

aws s3 ls s3://BUCKET_NAME


Upload a file:

aws s3 cp FILE s3://BUCKET_NAME/


Download a file:

aws s3 cp s3://BUCKET_NAME/FILE .


Delete an object:

aws s3 rm s3://BUCKET_NAME/FILE


Using s3api:

aws s3api list-buckets

aws s3api get-bucket-versioning \
    --bucket BUCKET_NAME

aws s3api get-bucket-encryption \
    --bucket BUCKET_NAME


SECURITY
--------

Default mindset:

S3 Bucket
    ↓
Private
    ↓
IAM / Role
    ↓
Application


Avoid:

S3
 ↓
Public Internet
 ↓
Anyone can access


Enable/maintain:

✅ Block Public Access
✅ Encryption
✅ Least-privilege IAM
✅ Versioning when appropriate


S3 + APPLICATION
----------------

Application
    ↓
IAM Role
    ↓
S3
    ↓
Object


S3 + ML
--------

MLflow / Application
        ↓
       S3
        ↓
Model / Artifact


IMPORTANT
---------

S3 is NOT a normal filesystem.

Think:

Bucket → Object → Key


REMEMBER
--------

S3 = Scalable object storage.

Bucket = Container
Object = Stored file/data
Key = Object's name/path

============================================================
'''