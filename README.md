RandomHashBenchmarker
=====================

Overview
--------

A Python tool which is useful for benchmarking a computer's CPU power. Spawns one random hash computation process per CPU core.

Usage
-----

`benchmarker.py [secondsToRun] [requiredBenchmark]`

* `[secondsToRun]` number of seconds for which to run the script
* `[requiredBenchmark]` required number of hashes to compute within the specified amount of time

Why?
----

I created this tool since not all Amazon AWS EC2 instances of the same type are created equal; some perform measurably worse than others. This little benchmarking script computes a number of random hashes within the specified amount of time [secondsToRun]. It's intended to be run immediately after EC2 instance startup to measure performance. If the results are not favorable (less than [requiredBenchmark]), then the instance can be terminated and replaced.

I suggest trying it on several copies of a particular instance type to get a feel for an appropriate [requiredBenchmark] number to use.
