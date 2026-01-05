---
title: "Bash Function for ChatGPT API Calls in Command Line"
date: 2023-02-07
author: pengjianqing
categories: ['Tech']
tags: ['AI', 'ChatGPT', 'OpenAI']
---

Write one bash function to call the ChatGPT API in the command line

```
`function .gpt3 {
if [ "$#" = 2 ];then
        KEYWORD="$1"
        TEMPERATURE=$2
elif [ "$#" = 1 ];then
        KEYWORD="$1"
        TEMPERATURE=1.0
else
        .log "Usage $0 "Question" [Temperature] "
        return -1
fi
echo "Keyword: ${KEYWORD}"
echo "Temperature: $TEMPERATURE"

curl=`cat 

So I can run it in my terminal

```
`.gpt3 "Write the strategy about Mobile Performance testing"`
```

```
`Keyword: Write the strategy about Mobile Performance testing
Temperature: 1.0
curl https://api.openai.com/v1/completions   -H 'Content-Type: application/json'   -H "Authorization: Bearer sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"   -d '{
  "model": "text-davinci-003",
  "prompt": "Write the strategy about Mobile Performance testing",
  "max_tokens": 4000,
  "temperature": 1.0

}' --insecure | jq -r '.choices[]'.text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1818    0  1673  100   145    140     12  0:00:12  0:00:11  0:00:01   525

1. Establish Performance Testing Goals and Objectives: Start by assessing the overall performance needs of the mobile application, including response times, memory usage, battery life, and other key factors. Establish performance testing goals and objectives based on these assessments, and document them accordingly.

2. Select Performance Testing Platforms and Tools: Based on the performance objectives, choose performance testing platforms and tools that best suited to measure the desired performance criteria.

3. Test Mobile Client Performance: Run and test the performance of the mobile client side of the application, including stress tests on file size and networking, as well as responsiveness and memory usage.

4. Test Mobile Server Performance: Assess the mobile server’s performance by measuring response times, scalability, and system load.

5. Analyze Performance Test Results: Analyze the performance test results and compare them to the desired performance objectives. Take steps to fix any performance issues that are found.

6. Fine-Tune Performance: Fine-tune the performance tests and revise them, if necessary, to address any changes to the application that may have occurred on either the client or server side.

7. Repeat Performance Tests: Repeat performance tests on a regular basis, to ensure that the mobile application continues to meet performance objectives.`
```