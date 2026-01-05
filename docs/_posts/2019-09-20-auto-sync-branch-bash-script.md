---
title: "Auto Sync Branch Bash Script"
date: 2019-09-20
author: pengjianqing
categories: ['Tech']
tags: ['Bash', 'github']
---

Don't want to wast time to repeat the branch merge actions, like [A]>[B]>[C], so I create the bash script to run it automatically.

- [https://github.com/pjq/auto_sync_branch](https://github.com/pjq/auto_sync_branch)

Script for auto sync/merge the code from branch [A] to [B] with just one click

## Quick Start

```
`chmod +x auto_sync_branch.sh
./auto_sync_banch.sh -f config.txt.example`
```

*But you may have permission issue, as you are not the contributor of the this repo*

## How to update the configurations

```
`cp config.txt.example config.txt`
```

And update the configs to what you want

```
`DEVELOP_BRANCH="develop"
REMOTE_REPO="https://github.com/pjq/auto_sync_branch.git"
LOCAL_REPO="local"
WORKSPACE="./auto_sync_branch_workspace"
RULE="master>develop|develop>pjq/develop|pjq/develop>user/develop"`
```

Then run it

```
`chmod +x auto_sync_branch.sh
./auto_sync_branch.sh -f config.txt`
```

Output

```
`./auto_sync_branch.sh -f config.txt
Config file:config.txt
read config...
Prepare the workspace...
Cloning into 'local'...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 17 (delta 4), reused 12 (delta 4), pack-reused 0
Unpacking objects: 100% (17/17), done.
start sync...
Sync rule master>develop
Start Sync code from master to develop
From https://github.com/pjq/auto_sync_branch
 * branch            master     -> FETCH_HEAD
From https://github.com/pjq/auto_sync_branch
 * branch            develop    -> FETCH_HEAD
Already on 'develop'
Your branch is up to date with 'origin/develop'.
git checkout develop success!
Updating 3f0b2f9..13dae3f
Fast-forward
 auto_sync_branch.sh | 2 +-
 config.txt          | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
Merge master > develop success!
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/pjq/auto_sync_branch.git
   3f0b2f9..13dae3f  develop -> develop
Push to remote success!
Sync master>develop success!
Sync rule develop>pjq/develop
Start Sync code from develop to pjq/develop
From https://github.com/pjq/auto_sync_branch
 * branch            develop    -> FETCH_HEAD
From https://github.com/pjq/auto_sync_branch
 * branch            pjq/develop -> FETCH_HEAD
Branch 'pjq/develop' set up to track remote branch 'pjq/develop' from 'origin'.
Switched to a new branch 'pjq/develop'
git checkout pjq/develop success!
Updating 3f0b2f9..13dae3f
Fast-forward
 auto_sync_branch.sh | 2 +-
 config.txt          | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
Merge develop > pjq/develop success!
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/pjq/auto_sync_branch.git
   3f0b2f9..13dae3f  pjq/develop -> pjq/develop
Push to remote success!
Sync develop>pjq/develop success!
Sync rule pjq/develop>user/develop
Start Sync code from pjq/develop to user/develop
From https://github.com/pjq/auto_sync_branch
 * branch            pjq/develop -> FETCH_HEAD
From https://github.com/pjq/auto_sync_branch
 * branch            user/develop -> FETCH_HEAD
Branch 'user/develop' set up to track remote branch 'user/develop' from 'origin'.
Switched to a new branch 'user/develop'
git checkout user/develop success!
Updating 3f0b2f9..13dae3f
Fast-forward
 auto_sync_branch.sh | 2 +-
 config.txt          | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
Merge pjq/develop > user/develop success!
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/pjq/auto_sync_branch.git
   3f0b2f9..13dae3f  user/develop -> user/develop
Push to remote success!
Sync pjq/develop>user/develop success!`
```

## Update Rules

The rule is simple, define the branch `from>to`, and use "|" to split different rules

```
`RULE="master>develop|develop>pjq/develop|pjq/develop>user/develop"`
```