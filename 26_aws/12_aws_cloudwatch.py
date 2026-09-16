'''
============================================================
AWS CLOUDWATCH — Monitoring & Observability
============================================================

CloudWatch = AWS monitoring and observability service.

It helps you understand:

    What is happening?
    Is the system healthy?
    Are there errors?
    Is resource usage increasing?


BASIC MODEL
-----------

AWS Resource
     ↓
CloudWatch
     ├── Metrics
     ├── Logs
     ├── Alarms
     └── Dashboards


METRICS
-------

Metrics = Numerical measurements.

Examples:

    CPUUtilization
    NetworkIn
    NetworkOut
    RequestCount
    Latency


Example:

EC2
 ↓
CPU = 85%
 ↓
CloudWatch


LOGS
----

Logs = Records of what happened.

Application
    ↓
Logs
    ↓
CloudWatch Logs


Example:

2026-09-16 ERROR Database connection failed


ALARMS
------

Alarm watches a metric and reacts when
a defined condition is reached.

Example:

CPU > 80%
    ↓
CloudWatch Alarm
    ↓
Notification / Action


DASHBOARD
---------

Dashboard = Visual view of system health.

Example:

┌─────────────────────────┐
│ CPU        65%          │
│ Requests   1200/min     │
│ Errors     2            │
│ Latency    120ms        │
└─────────────────────────┘


OBSERVABILITY
-------------

Three important signals:

Metrics
→ What is happening?

Logs
→ What happened?

Alarms
→ When should we be alerted?


IMPORTANT COMMANDS
------------------

List CloudWatch alarms:

aws cloudwatch describe-alarms


List metrics:

aws cloudwatch list-metrics


Get metric statistics:

aws cloudwatch get-metric-statistics \
    --namespace AWS/EC2 \
    --metric-name CPUUtilization


List log groups:

aws logs describe-log-groups


COST SAFETY
-----------

CloudWatch has both free and paid usage depending
on the feature and amount of data.

Important:

❌ Don't create unnecessary high-volume logs
❌ Don't create excessive custom metrics
❌ Don't keep unnecessary log retention


PRODUCTION PATTERN
------------------

Application
    ↓
Metrics + Logs
    ↓
CloudWatch
    ↓
Alarms
    ↓
Notification
    ↓
Engineer


REMEMBER
--------

CloudWatch
    ↓
Metrics → Numbers
Logs    → Events / Records
Alarms  → Conditions
Dashboard → Visibility

CloudWatch helps answer:

"Is my system healthy, and if not, what is happening?"

============================================================
'''