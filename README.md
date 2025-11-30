# MapReduce WordCount Project

This repository contains two implementations of the WordCount program using Hadoop.

## 1. Java MapReduce (Maven Project)
The Maven project implements WordCount with the Hadoop MapReduce API.

**Main components:**
- `TokenizerMapper.java` — emits `(word, 1)`
- `IntSumReducer.java` — sums occurrences
- `WordCount.java` — configures and runs the job
- `pom.xml` — includes Hadoop dependencies (HDFS, Common, MapReduce Client)

**Build and run:**
```bash
mvn clean package
hadoop jar mapreduce-app.jar input output
```

## 2. Python MapReduce (Hadoop Streaming)
Two Python scripts reproduce WordCount using Hadoop Streaming.

**mapper.py
Reads lines from STDIN, splits into words, outputs:
```bash
word    1
 ```
**reducer.py
Aggregates counts for each word and prints totals.

Run with Hadoop Streaming:
```bash
hadoop jar hadoop-streaming.jar \
  -files mapper.py,reducer.py \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -input /input/data.txt \
  -output /output/result
```

This project demonstrates both Java-based MapReduce and Python Hadoop Streaming for distributed text processing.
