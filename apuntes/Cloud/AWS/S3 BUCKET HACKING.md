
## Region enumeration

**Literally just ping**

![[Pasted image 20211025212041.png]]


### Items Listing

```bash
aws s3 ls s3://flaws.cloud/ --no-sign-request --region us-west-2
2017-03-13 22:00:38       2575 hint1.html
2017-03-02 23:05:17       1707 hint2.html
2017-03-02 23:05:11       1101 hint3.html
2020-05-22 13:16:45       3162 index.html
2018-07-10 11:47:16      15979 logo.png
2017-02-26 20:59:28         46 robots.txt
2017-02-26 20:59:30       1051 secret-dd02c7c.html
```

**If we don't actually now the region or for some reason we want to enumerate without it**

```bash
aws s3 --endpoint-url http://s3.bucket.htb ls s3://<bucket_name>>/
```

