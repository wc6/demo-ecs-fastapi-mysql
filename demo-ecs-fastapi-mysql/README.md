#### copilot 部署 ECS FastApi应用

#### 文件夹结构
```bash
.
├── Dockerfile
├── app
│   ├── __init__.py
│   └── main.py
└── requirements.txt
```
```bash
copilot init -a demoapp -t "Load Balanced Web Service" -n "fastmysql" -d ./Dockerfile     
# copilot init -a 应用名 -t "固定类型" -n "Service名字" -d ./Dockerfile

copilot env init --name uat --profile default --import-vpc-id vpc-055dec0736877f582 --import-public-subnets subnet-06f008ada1c41f1a0,subnet-0d7d662a9cb875c44,subnet-0535b256ed654c75a,subnet-018bfac11befe86ad,subnet-03d141d4ea5df2935,subnet-0768d1b7295c8780d 
# copilot env init --name 环境名字 --profile default --import-vpc-id vpc-id --import-public-subnets subnet-id1,id2 

copilot env deploy --name "uat"
# copilot env deploy --name "部署环境"

copilot deploy --name "fastmysql" -e "uat"
# copilot deploy --name "Service名字" -e "环境"
```
#### 运行之后
```bash
.
├── Dockerfile
├── app
│   ├── __init__.py
│   └── main.py
├── copilot
│   ├── environments
│   │   └── uat
│   │       └── manifest.yml
│   └── fastmysql
│       └── manifest.yml
└── requirements.txt
```

![Alt text](image.png)
![Alt text](image-1.png)

上面是未创建RDS的


下午任务
- 创建RDS
- 修改代码，重新部署应用
- 设置传入参数

```bash
echo "# demo-ecs-fastapi-mysql" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/wc6/demo-ecs-fastapi-mysql.git
git push -u origin main
```